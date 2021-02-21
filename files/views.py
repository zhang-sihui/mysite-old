import os
from django.http import FileResponse
from django.utils.encoding import escape_uri_path
from django.shortcuts import render
from .models import File
from . import base_dir


# Create your views here.

def files(request):
    """
        先从文件夹获取文件，反向从数据库获取id，拼接称字典，
        不直接从数据库获取文件名传入前端，原因是：如果存储文件的文件夹过大及想要删除一些文件时，
        文件夹中没有文件，数据库中有文件名，信息不匹配，导致前端会有一些文件无法下载。
        通过文件夹里的文件反向获取id,可以避免此问题。如此，文件的上传与下载可以统一化。
        上传的文件可以从页面支持下载，不需要修改源代码。
    """
    file_dir = os.path.join(base_dir, 'files', 'manage_files')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    files_name = os.listdir(file_dir)
    files_name_size = []
    ids = []
    if not files_name:
        not_files = '暂时没有文件。'
        return render(request, 'files/files.html', locals())
    else:
        for file_name in files_name:
            file_info = File.objects.get(file_name=file_name)
            ids.append(file_info.id)
            files_name_size.append(file_name + ' -- ' + str(os.path.getsize(file_dir + '/' + file_name) // 1024) + ' KB')
        # id 与 name 合成字典，一边传入前端，此 id 用来下载文件。【如果在前端直接传入文件名在数据库中搜索，似乎不在需要 id】
        files_dict = dict(zip(ids, files_name_size))
        return render(request, 'files/files.html', locals())


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
                success_upload = '上传成功，可以继续'
                return render(request, 'files/upload.html', locals())
            else:
                handle_uploaded_file(get_file, str(get_file))
                success_upload = '上传成功，可以继续'
                return render(request, 'files/upload.html', locals())
    return render(request, 'files/upload.html', locals())


def handle_uploaded_file(file, filename):
    file_upload_path = os.path.join(base_dir, 'files', 'manage_files')
    if not os.path.exists(file_upload_path):
        os.makedirs(file_upload_path)
    with open(file_upload_path + '/' + filename, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)


def uploaded_files(request):
    files = File.objects.all()
    not_files = '暂时没有文件'
    return render(request, 'files/uploaded.html', locals())


# 这里可以传入文件名，直接在数据库中搜索文件名，甚至直接在文件中搜索，但是不能统计下载次数
def download_file(request, file_id):
    file = File.objects.get(id=file_id)
    file_name = file.file_name
    file.downloads_count += 1
    file.save()
    file_path = os.path.join(base_dir, 'files', 'manage_files', file_name)
    file_ = open(file_path, 'rb')
    response = FileResponse(file_)
    response['Content-Type'] = 'application/octet-stream'
    # 文件名为中文时无法识别，使用 UTF-8 和 escape_uri_path 处理
    response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(escape_uri_path(file_name))
    return response
