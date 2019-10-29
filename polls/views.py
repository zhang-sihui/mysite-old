import os
from os import path
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import escape_uri_path
from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question


# Create your views here.


# 网站主页面
def home(request):
    return render(request, 'main/home.html')


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions.(not including
        those set to be published in the future)."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# 文件上传
def upload(request):
    if request.method == 'POST':
        up_file = request.FILES.get('file')
        if not up_file:
            return render(request, 'files/upload.html',
                          {'error_message': 'no file.. please choose a file...'})
        else:
            handle_uploaded_file(up_file, str(up_file))
            return render(request, 'files/upload.html',
                          {'success_message': 'upload success.. please continue..'})
    return render(request, 'files/upload.html')


# 处理上传的文件
def handle_uploaded_file(file, filename):
    # if not os.path.exists('polls/manage_files/upload/'):
    #     os.mkdir('polls/manage_files/upload/')
    # with open('polls/manage_files/upload/' + filename, 'wb+') as destination:
    #     for chunk in file.chunks():
    #         destination.write(chunk)
    base_dir = path.dirname(path.realpath(__file__))
    file_path = path.join(base_dir, 'manage_files', 'upload')
    if not path.exists(file_path):
        os.mkdir(file_path)
    with open(file_path + '/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


# 展示上传的文件
def uploaded(request):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'manage_files', 'upload')
    file_list = os.listdir(file_path)
    return render(request, 'files/uploaded.html', {'file_list': file_list})


# 展示可供下载的文件文件
def show(request):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'manage_files', 'download')
    file_list = os.listdir(file_path)
    number = []
    for i in range(1, 4):
        number.append(i)
    file_dict = dict(zip(number, file_list))
    return render(request, 'files/show.html', {'file_list': file_list, 'file_dict': file_dict})


# 文件下载
def download(request, id):
    data = [
        {"id": "1", "file": "Django1.8中文文档.pdf"},
        {"id": "2", "file": "Flask+Web开发：基于Python的Web应用开发实战.pdf"},
    ]
    file_name = ''
    for i in data:
        if i['id'] == id:
            file_name = i['file']
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
    file_path = os.path.join(base_dir, 'polls', 'manage_files', 'download', file_name)  # 下载文件的绝对路径
    files = open(file_path, 'rb')
    response = FileResponse(files)
    response['Content-Type'] = 'application/octet-stream'
    response["Content-Disposition"] = "attachment; " \
                                      "filename*=UTF-8''{}".format(escape_uri_path(file_name))
    return response


# 图片
def image(request):
    return render(request, 'interest/image.html')


# 电影
def film(request):
    return render(request, 'interest/film.html')


# 音乐
def music(request):
    return render(request, 'interest/music.html')


# 404
def page_not_founds(request):
    return render(request, "error/404.html")


# 500
def server_error(request):
    return render(request, "error/500.html")
