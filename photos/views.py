import os
from os import path
from . import base_dir
from .models import Photo
from django.shortcuts import render
from django.http import FileResponse
from django.utils import timezone
from django.utils.encoding import escape_uri_path
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def display_photos(request):
    photos = Photo.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    paginator = Paginator(photos, 6)
    try:
        num = request.GET.get('index', '1')
        page = paginator.page(num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    not_photos = '还没有图片！'
    return render(request, 'photo/display.html', locals())


def upload_photo(request):
    if request.method == 'POST':
        get_photo = request.FILES.get('file')
        if not get_photo:
            not_photo = '未选择文件！'
            return render(request, 'photo/upload.html', locals())
        else:
            photos = Photo.objects.filter(photo_name=get_photo)
            if not photos:
                Photo.objects.create(photo_name='%s' % get_photo)
                handle_uploaded_photo(get_photo, str(get_photo))
                success_upload = '上传成功，请继续！'
                return render(request, 'photo/upload.html', locals())
            else:
                handle_uploaded_photo(get_photo, str(get_photo))
                success_upload = '上传成功，请继续！'
                return render(request, 'photo/upload.html', locals())
    return render(request, 'photo/upload.html')


def handle_uploaded_photo(file, filename):
    photo_upload_path = path.join(base_dir, 'photos', 'images', 'upload')
    if not path.exists(photo_upload_path):
        os.mkdir(photo_upload_path)
    with open(photo_upload_path + '/' + filename, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)


def download(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    photo_name = photo.photo_name
    photo_path = os.path.join(base_dir, 'photos', 'images', 'upload', photo_name)
    photo_ = open(photo_path, 'rb')
    response = FileResponse(photo_)
    response['Content-Type'] = 'application/octet-stream'
    # 图片名为中文时无法识别，使用 UTF-8 和 escape_uri_path 处理
    response['Content-Disposition'] = "attachment; " \
                                      "filename*=UTF-8''{}".format(escape_uri_path(photo_name))
    return response
