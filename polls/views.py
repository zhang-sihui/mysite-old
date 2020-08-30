import os
from os import path
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import escape_uri_path
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import cache_page
from .models import Choice, Question, File
from . import base_dir


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/vote.html'
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


def upload_file(request):
    if request.method == 'POST':
        get_file = request.FILES.get('file')
        if not get_file:
            not_file = '尚未选择文件，请选择文件。'
            return render(request, 'files/upload.html', locals())
        else:
            file = File.objects.filter(file_name=get_file)
            if not file:
                File.objects.create(file_name='%s' % get_file)
                handle_uploaded_file(get_file, str(get_file))
                success_upload = '上传成功，可以继续。'
                return render(request, 'files/upload.html', locals())
            else:
                handle_uploaded_file(get_file, str(get_file))
                success_upload = '上传成功，可以继续。'
                return render(request, 'files/upload.html', locals())
    return render(request, 'files/upload.html')


def handle_uploaded_file(file, filename):
    file_upload_path = path.join(base_dir, 'polls', 'manage_files', 'download')
    if not path.exists(file_upload_path):
        os.mkdir(file_upload_path)
    with open(file_upload_path + '/' + filename, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)


def uploaded_files(request):
    files = File.objects.filter(pub_date__lte=timezone.now())
    not_files = '暂时没有文件。'
    return render(request, 'files/uploaded.html', locals())


def show_files(request):
    """
        先从文件夹获取文件，反向从数据库获取id，拼接称字典，
        不直接从数据库获取文件名传入前端，原因是：如果存储文件的文件夹过大及想要删除一些文件时，
        文件夹中没有文件，数据库中有文件名，信息不匹配，导致前端会有一些文件无法下载。
        通过文件夹里的文件反向获取id,可以避免此问题。如此，文件的上传与下载可以统一化。
        上传的文件可以从页面支持下载，不需要修改源代码。
    """
    file_dir = os.path.join(base_dir, 'polls', 'manage_files', 'download')
    files = os.listdir(file_dir)
    ids = []
    if not files:
        not_files = '暂时没有文件。'
        return render(request, 'files/show.html', locals())
    else:
        for file in files:
            file_info = File.objects.get(file_name=file)
            ids.append(file_info.id)
        # id 与 name 合成字典，一边传入前端，此 id 用来下载文件。【如果在前端直接传入文件名在数据库中搜索，似乎不在需要 id】
        files_dict = dict(zip(ids, files))
        return render(request, 'files/show.html', locals())


  # 这里可以传入文件名，直接在数据库中搜索文件名，甚至直接在文件中搜索，但是不能统计下载次数
def download_file(request, file_id):
    file = File.objects.get(id=file_id)
    file_name = file.file_name
    file.downloads_count += 1
    file.save()
    file_path = os.path.join(base_dir, 'polls', 'manage_files', 'download', file_name)
    file_ = open(file_path, 'rb')
    response = FileResponse(file_)
    response['Content-Type'] = 'application/octet-stream'
    # 文件名为中文时无法识别，使用 UTF-8 和 escape_uri_path 处理
    response["Content-Disposition"] = "attachment; " \
                                      "filename*=UTF-8''{}".format(escape_uri_path(file_name))
    return response


@cache_page(60 * 60 * 24)
def play_music(request):
    file_dir = os.path.join(base_dir, 'polls', 'static', 'music')
    files = os.listdir(file_dir)
    files_set = set()
    for file in files:
        if file[-3:] == 'mp3':
            files_set.add(file)
    return render(request, 'music/music.html', locals())


@cache_page(60 * 60 * 24)
def get_music_lyric(request, filename):
    file_dir = os.path.join(base_dir, 'polls', 'static', 'music')
    files = os.listdir(file_dir)
    files_set = set()
    for file in files:
        if file[-3:] == 'mp3':
            files_set.add(file)
    file_name = filename[:-4] + '.lrc'
    try:
        with open(file_dir + '/' + file_name, 'r', encoding='utf8') as f:
            lyrics = f.readlines()
    except:
        not_lyric = '暂无歌词文件。'
    return render(request, 'music/music_lyric.html', locals())
