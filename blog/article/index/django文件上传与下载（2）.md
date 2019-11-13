0.这篇文章我默认你对Django已经有所了解，即熟悉基本项目目录，url设置，以及各代码所在文件夹。
只是不知如何具体操作，这里提供借鉴。Python3.7,Django2.1。
1.文件上传与下载，仅通过web端实现上传与下载，上传的文件展示并下载，并不是很难，下面就说说怎么做。
2.上传前端代码：upload.html
<body>
<form action="" method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            <input type="file" name="file"/>
            <input type="submit"value="Upload"/>
</form>
{% if error_message %}
        <strong>{{ error_message }}</strong>
        {% endif %}
        {% if success_message %}
        <strong>{{ success_message }}</strong>
{% endif %}
</body>
上传表单，input标签内的name值file传入后端即获取的文件名，下面的代码是上传错误与成功的反馈信息。

3.后端获取文件名，并处理app/views：
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
        for chunk in file.chunks():  # 分块写入文件
            destination.write(chunk)


# app/models
class File(models.Model):
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name

上面两个函数处理上传的文件有相应注释，第三段是数据模型，仅用来储存文件名，没有储存文件路径，
有兴趣和尝试。

4.展示数据库存储的文件名 app/views：
# 展示上传的文件
def uploaded(request):
    test = File.objects.filter(id=7).delete()
    # 获取数据库存储的所有文件名及对应id,格式为[("",""),("","")]
    db_files_list = File.objects.values_list()
    file_name_list = []
    for db_file in db_files_list:  # 获取单个文件名及id元组("id", "name")
        file_name = db_file[1]  # 获取数据库文件名
        file_name_list.append(file_name)  # 数据库文件名存储列表中
    return render(request, 'files/uploaded.html', {'file_name_list': file_name_list})
	
前端代码：uploaded.html
<html lang="en">
<body>
{% if file_name_list %}
    <ul>
        {% for file in file_name_list %}
        <li>{{ file }}</li>
        {% endfor %}
    </ul>
    {% else %}
    <p>No file.</p>
    {% endif %}
</body>
</html>

5.展示可供下载的文件，文件夹中存储的文件，和上一步的区别在于，文件的文件被删除，数据库仍有记录，
所以以文件夹为准。请看注释。
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

对应前端代码：show.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>File list</title>
</head>
<body>
    {% if dir_file_list %}
    <ul>{% for id, file in files_dict.items %}
        <li>
            <a href="polls/download/{{ id }}/">
			{{ file }}
            </a>
        </li>
        {% endfor %}
    </ul>
    {% else %}
    <p>No File.</p>
    {% endif %}
    <br>
</body>
</html>

6.文件下载实现：
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


7.urls.py设置：
from django.urls import path, re_path

app_name = 'polls'

urlpatterns = [
	# ...
    # files
    path('upload/', views.upload, name='upload'),
    path('uploaded/', views.uploaded, name='uploaded'),
    path('show/', views.show, name='show'),
    re_path('download/(?P<file_id>\\d+)/', views.download, name='download'),
]

8.为简化代码，获取项目目录路径，设置在__init__.py中：
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

9.[app]/views中需要导入一些包和方法。
import os
from os import path
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import escape_uri_path
from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import File
from . import base_dir
以上文件视情况导入。