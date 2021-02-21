import os
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from . import base_dir


# Create your views here.

@cache_page(60 * 60 * 24)
def play_music(request):
    file_dir = os.path.join(base_dir, 'music', 'static', 'music')
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    files = os.listdir(file_dir)
    files_set = set()
    for file in files:
        if file[-3:] == 'mp3':
            files_set.add(file)
    return render(request, 'music/music.html', locals())


@cache_page(60 * 60 * 24)
def get_music_lyric(request, filename):
    file_dir = os.path.join(base_dir, 'music', 'static', 'music')
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
