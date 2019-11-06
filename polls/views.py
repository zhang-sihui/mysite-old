import os
from os import path
from django.http import HttpResponseRedirect, FileResponse, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import escape_uri_path
from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question, File
from . import base_dir


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
        up_file = request.FILES.get('file')  # 获取文件
        if not up_file:  # 未选择文件
            return render(request, 'files/upload.html',
                          {'error_message': 'no file. please choose a file.'})
        else:
            db_file = File.objects.get(file_name=up_file)
            if not db_file:  # 判断数据库中是否已有正在上传的文件名
                File.objects.create(file_name='%s' % up_file)  # 如果没有，文件名存入数据库
                handle_uploaded_file(up_file, str(up_file))  # 处理文件
                return render(request, 'files/upload.html',
                              {'success_message': 'upload success. please continue.'})
            else:   # 数据库中已存在，直接处理文件
                handle_uploaded_file(up_file, str(up_file))  # 处理文件
                return render(request, 'files/upload.html',
                              {'success_message': 'upload success. please continue.'})
    return render(request, 'files/upload.html')


# 处理上传的文件
def handle_uploaded_file(file, filename):
    file_path = path.join(base_dir, 'polls', 'manage_files', 'download')
    if not path.exists(file_path):  # 判断存储文件的路径是否存在
        os.mkdir(file_path)
    with open(file_path + '/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


# 展示上传的文件
def uploaded(request):
    test = File.objects.filter(id=7).delete()
    print(test)
    # 获取数据库存储的所有文件名及对应id,格式为[("",""),("","")]
    db_files_list = File.objects.values_list()
    print(db_files_list)
    file_name_list = []
    for db_file in db_files_list:  # 获取单个文件名及id元组("id", "name")
        file_name = db_file[1]  # 获取数据库文件名
        file_name_list.append(file_name)  # 数据库文件名存储列表中
    return render(request, 'files/uploaded.html', {'file_name_list': file_name_list})


# 展示可供下载的文件()
def show(request):
    """
        先从文件夹获取文件，反向从数据库获取id，拼接称字典，
        不直接从数据库获取文件名传入前端，原因是：如果存储文件的文件夹过大及想要删除一些文件时，
        文件夹中没有文件，数据库中有文件名，信息不匹配，导致前端会有一些文件无法下载。
        通过文件夹里的文件反向获取id,可以避免此问题。如此，文件的上传与下载可以统一化。
        上传的文件可以从页面支持下载，不需要修改源代码。
    """
    dir_file_path = os.path.join(base_dir, 'polls', 'manage_files', 'download')
    dir_file_list = os.listdir(dir_file_path)  # 获取文件夹里的文件，可以下载的文件
    id_list = []
    if not dir_file_list:  # 判断文件夹中是否存在文件
        return render(request, 'files/show.html', {'dir_file_list': dir_file_list})
    else:
        for file in dir_file_list:
            file_info = File.objects.get(file_name=file)  # 通过文件夹里的文件名获取文件在数据库里的文件信息
            id_list.append(file_info.id)  # 获取文件在数据库里文件的id,并存入列表
        files_dict = dict(zip(id_list, dir_file_list))  # id与name合成字典，一边传入前端，此id用来下载文件
        return render(request, 'files/show.html', {'dir_file_list': dir_file_list,
                                                   'files_dict': files_dict})


# 文件下载
def download(request, file_id):
    file = File.objects.get(id=file_id)
    file_name = file.file_name
    files_path = os.path.join(base_dir, 'polls', 'manage_files', 'download', file_name)  # 获取文件
    files = open(files_path, 'rb')
    response = FileResponse(files)
    response['Content-Type'] = 'application/octet-stream'
    # 文件名为中文时无法识别，使用UTF-8和escape_uri_path处理
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
