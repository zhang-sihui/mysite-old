import os
from os import path
from PIL import Image
from . import base_dir
from .models import Photo
from django.shortcuts import render
from django.http import FileResponse
from django.utils import timezone
from django.utils.encoding import escape_uri_path
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def display_photo(request):
    db_photo_list = Photo.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    paginator = Paginator(db_photo_list, 6)
    try:
        num = request.GET.get('index', '1')
        page = paginator.page(num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'photo/display.html', locals())


# 图片上传
def upload_photo(request):
    if request.method == 'POST':
        up_photo = request.FILES.get('file')  # 获取图片
        if not up_photo:  # 未选择文件
            error_message = '未选择文件！！'
            return render(request, 'photo/upload.html', locals())
        else:
            # 这里filter不替换为get，因为get查询不到会报错，而filter查询不到，会返回空列表，
            # 而我们上传的图片，数据库中很可能不存在（存在也不要上传了），这时代码会报错，而不是返回空列表
            # 所以应该使用filter查询。
            db_photo = Photo.objects.filter(photo_name=up_photo)
            if not db_photo:  # 判断数据库中是否已有正在上传的文件名
                Photo.objects.create(photo_name='%s' % up_photo)  # 如果没有，图片名存入数据库
                handle_uploaded_photo(up_photo, str(up_photo))  # 处理图片
                success_message = "上传成功，请继续！"
                return render(request, 'photo/upload.html', locals())
            else:  # 数据库中已存在，直接处理图片
                handle_uploaded_photo(up_photo, str(up_photo))  # 处理图片
                success_message = "上传成功，请继续！"
                return render(request, 'photo/upload.html', locals())
    return render(request, 'photo/upload.html')


# 处理上传的图片
def handle_uploaded_photo(file, filename):
    photo_path = path.join(base_dir, 'photos', 'images', 'upload')
    # res_path = path.join(base_dir, 'photos', 'images', 'modified', '')
    if not path.exists(photo_path):  # 判断存储图片的路径是否存在
        os.mkdir(photo_path)
    with open(photo_path + '/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    # 对图片按长宽比缩放，以高度180为准
    # for picName in os.listdir(photo_path):
    #     pic_path = os.path.join(photo_path, picName)
    #     with Image.open(pic_path) as img:
    #         width, height = img.size
    #         new_height = 180
    #         new_width = new_height * width // height
    #         img1 = img.resize((new_width, new_height), Image.ANTIALIAS)
    #         img1.save(os.path.join(res_path + picName))


# 下载，为前端获取图片http路径而设置
def download(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    photo_name = photo.photo_name
    photos_path = os.path.join(base_dir, 'photos', 'images', 'upload', photo_name)  # 获取图片
    photos = open(photos_path, 'rb')
    response = FileResponse(photos)
    response['Content-Type'] = 'application/octet-stream'
    # 图片名为中文时无法识别，使用UTF-8和escape_uri_path处理
    response["Content-Disposition"] = "attachment; " \
                                      "filename*=UTF-8''{}".format(escape_uri_path(photo_name))
    return response
