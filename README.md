# Introduction

## A personal website

### 开发环境

- Windows 10
- PyCharm 2019
- Python 3.7.3
- Django 2.2

### 终端操作

- Terminal: Go to mysite folder（终端：进入 mysite 文件夹）。
- Enter the following command, then enter：（输入以下命令，回车运行。）
    - `python manage.py runserver`

### 浏览器输入

- User UI(用户)：http://127.0.0.1:8000
- Admin UI(管理)：http://127.0.0.1:8000/admin

### 版本说明

- Version 0.0.1 is the official Django tutorial content，starting with version 1.0.0 for personal website content.
- 版本 0.0.1 为 Django 官方教程内容，从版本 1.0.0 开始，为个人网站内容。

### Table of content

- v0.0.1
    - Django 官方教程，一个调查投票应用。
- v1.0
    - v1.0.0：
        - 在 v0.0.1 基础上，构建个人网站，主要包括：
            - 官方的投票应用。
            - 文件上传与下载。
    - v1.1.0：
        - 增加 blog 应用
    - v1.2.0：
        - 完善文件上传与下载功能，之前的版本中，文件下载功能只能下载我添加的文件，
        这一版本，文件的上传与下载一体化，上传的文件下载通过 Web 端实现。
        - 前端部分页面开始使用 Bootstrap4，改进页面展示。
    - v1.3.0：
        - 增加用户登录，登录、注册、修改密码、重置密码。
        - 调整了文件上传功能页面的展示，修复一些问题。
        - 博客功能中增加功能：后台添加提示。
    - v1.4.0：
        - 将 polls 应用中的 image 改成单独的应用 photos。
    - v1.5.0：
        - 增加 watchlist 应用。
        - 去除 polls 应用中的 film 功能。
        - 优化 html 文件代码。
    - v1.6.0：
        - 增加 messageboard app,留言功能。
        - 数据库文件为空文件，所以如果你要运行这个版本代码，需要在终端 mysite 目录下运行两条命令迁移数据库：
            - `python manage.py makemigrations`，`python manage.py migrate`，再启动服务。
- v2.0：
	- v2.0.0：
        - 删除了一些功能，添加了一些功能，修改了一些功能。
        - 前端完全采用 Bootstrap4.4.0 重写。
    - v2.1.0：
        - 文件下载次数统计、blog 浏览次数统计。
        - 增加音乐播放器功能。
    - v2.1.1：
        - 修复留言回复后时间不更新问题，留言后台管理界面展示留言内容。
        - 修改一些 URL 格式。
        - AboutMe 界面下的 Email 链接格式修改为文字格式。
    - v2.2.0：
        - 修复 watchlist 下电影分类中，多条内容页面展示错乱的问题，为 HTML 文件中循环条件错误。
        - 音乐实时性较强，给音乐应用加上缓存功能，使用 python-memcached 模块。
        - 观影清单中应该展示时间，在 HTML 中插入查询时间字段值即可。
        - 处理没有上传音乐歌词文件时出现的服务器错误，代码加入逻辑判断是否有歌词文件。
        - 对 blog 中的文章进行年份归档。
        - 修改部分代码中的命名问题，以及删除多余注释。
        - 用户登录中，增加 notice 通知 model。
        - user 注册、登录等的页面标题太靠上，优化。
    - v2.2.1：
        - 在文件下载中，增加可下载文件的大小，全部以 KB 表示。
    - v2.2.2：
        - 修复 bug：clone 代码到本地后，运行发现无法访问 file，这是因为 mysite\polls\manage_files\download 下有两个文件，而数据库中没有记录，因为数据库是空数据库，所以需要删除这两个文件，即可访问。这个问题具体是从哪个版本开始的，暂时不太清楚，clone 最新的代码即可。
