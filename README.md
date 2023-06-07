# Brief introduction

A personal website by Django.

## Development environment

- Windows 10
- Python 3.7.3
- Django 3.0

## Preparation for runserver

- 安装模块：
    - 按照 requirements.txt 文件安装需要的模块，可以单个 `pip install xxx`；也可以一次全部安装，不过需要在项目文件夹路径下执行 `pip install -r requirements.txt`。
- 创建超级用户：
    - 在项目路径下：输入 `python manage.py createsuperuser`，进入超级用户（即管理员）创建终端。
    - 依次提示输入用户名，邮箱（可为空），密码，验证密码，即可成功创建。
- 初始化数据库：
    - 在项目路径下，执行两条命令即可初始化数据库：`python manage.py makemigrations`，`python manage.py migrate`。

## Runserver

- 终端下，进入 mysite 项目文件夹。
- 输入以下命令，回车运行启动服务：`python manage.py runserver`。

## Browser search

- User UI(用户)：http://127.0.0.1:8000
- Admin UI(管理)：http://127.0.0.1:8000/admin

## Version Description

- 版本 0.0.1 为 Django 官方教程内容，从版本 1.0.0 开始，为个人网站内容。

## Update details

### v3.0.0 series

- v3.0.2:
    - 调整 font-awesome、jquery、bootstrap 的 cdn 数据源。
    - html 中删除一些应用链接。
- v3.0.1:
    - 修复年份归档与通过标签获取的文章列表事件不倒序排列的问题。
    - 调整 aboutSite 页面展示。
    - 留言添加一个名字字段。
    - 上传界面中上传框居中，修复不对其问题。
- v3.0.0:
    - 升级 Django 3.0。
    - 更新 readme.md 格式。
    - bootstrap 使用集成的 bootstrap.bundle.min.js。
    - 文章信息展示的格式修改为：posted @ 2020-12-31 19:22 xxx。
    - blog 标签与年份链接一个文字可点，一个列表可点，格式统一。
    - 修改 watchlist 的 UI 风格。
    - 登录中验证码功能及 UI 风格。
    - 修改部分 url 格式。
    - 将 about_me（about_site）的内容写入数据库，通过 admin 管理。
    - blog 新加字段，草稿、发布，决定文章是否发布。
    - 拆分 polls 下的三个功能（polls，files，music），即新建 files，music 两个 app。
    - 增加数据库 ip 归属地自动查询。

---

### v2.0.0 series

- v2.4.2：
    - 修复：空数据库按年份获取文章，数据表中没有年份字段时报错。
- v2.4.1：
    - MEDIA_ROOT 目前在 blog 下，改为项目根目录 mysite 下。
    - 当前没有文章时，blog 的时间标签从指定的 2019 开始。现在可以用 django.db.models 中的 Min、Max 函数找到 Article 时间字段的最小值及最大值来设置时间归档的始末时间点。
    - 一个新的项目下，有的文件夹暂时为空，如 photos/images/upload、polls/manage_files/download、polls/static/music，暂时没有上传图片、没有上传文件以供下载、以及没有添加可以播放的 .mp3 音乐文件，在上传 github 时空文件夹不能上传，之前没有新建过程，clone 的代码缺少文件夹报错，现在改为自动新建，使用 os.makedirs 递归创建目录。
    - Tips：之前各个版本的代码中，如有报错，大概是缺少文件夹或者有多余的文件出错。主要是 photos/images/upload、polls/manage_files/download 这两个文件夹，git clone 后注意，如果文件夹有文件需要清空，如果没有文件夹，就新建。目前音乐播放界面展示的歌曲，需要直接添加到文件夹中，歌曲为 mp3 文件，歌词为 lrc 文件。
- v2.4.0：
    - `mysite/mysite/__init__.py` 中的 pymysql 要删除，历史遗留问题，测试 MySQL 时使用，而此后没有用到 MySQL，对于没有安装 pymysql 包的系统，还需要安装才能运行，故删除，之前版本的代码想要运行，可以安装此库，也可以删除此文件中两行代码。
    - requirements.txt 文件中删除 Python 和 Django 版本两行，对于 Django 的开发，可能已存在其他版本的 Django，并且其他项目在使用，如果安装不同的 Django 版本可能使原先的项目出现问题，这里交给开发者判断如何安装 Django，而 requirements.txt 只保存 Django 项目中使用到的第三方库。
    - requirements.txt 中第三方库的格式需要修改，目前的格式既不能一次安装所有指定版本库，单个安装时直接复制每行内容也有问题，需将 `-` 改为 `==`，则能一次安装所有指定版本第三方库。安装命令为 `pip install -r requirements.txt`。
    - 留言内容在一定长度时，留言时间的显示有问题。
    - `index/views` 去掉用 datetime 表示 localtime，使用 timezone.now()。去掉无用的 utc_to_iso 函数。
    - 主页增加每日访问量，实质是页面刷新次数（一对多），全部访问量即所有每日访问量之和。去掉访问人数，实质是储存访问者 ip，并非真实人数（一对一）。
    - blog 增加修改时间。同时修改每个文章列表中作者、时间、标签信息的大小、格式等。
- v2.3.0：
    - 修改 index 主页面及各 app 的主页面，index 页面导航栏链接改成卡片式链接。其他 app 去掉页面不同的 title，一个 app 统一为相同 title。
    - 主页面的各地时间，仅留下北京时间，其他删除。
    - 在手机页面中，因宽度太小导致 blog 部分标签溢出屏幕，标签不能自动换行。现改为将分类与归档并入其他 blog 子页面，并同时统计其数量，减少不必要标签、归档的页面跳转。
    - 添加一些图标，辅助表示其小标题内容。
- v2.2.2：
    - 修复 bug：clone 代码到本地后，运行发现无法访问 file，这是因为 mysite\polls\manage_files\download 下有两个文件，而数据库中没有记录，因为数据库是空数据库，所以需要删除这两个文件，即可访问。这个问题具体是从哪个版本开始的，暂时不太清楚，clone 最新的代码即可。
- v2.2.1：
    - 在文件下载中，增加可下载文件的大小，全部以 KB 表示。
- v2.2.0：
    - 修复 watchlist 下电影分类中，多条内容页面展示错乱的问题，为 HTML 文件中循环条件错误。
    - 音乐实时性较强，给音乐应用加上缓存功能，使用 python-memcached 模块。
    - 观影清单中应该展示时间，在 HTML 中插入查询时间字段值即可。
    - 处理没有上传音乐歌词文件时出现的服务器错误，代码加入逻辑判断是否有歌词文件。
    - 对 blog 中的文章进行年份归档。
    - 修改部分代码中的命名问题，以及删除多余注释。
    - 用户登录中，增加 notice 通知 model。
    - user 注册、登录等的页面标题太靠上，优化。
- v2.1.1：
    - 修复留言回复后时间不更新问题，留言后台管理界面展示留言内容。
    - 修改一些 URL 格式。
    - AboutMe 界面下的 Email 链接格式修改为文字格式。
- v2.1.0：
    - 文件下载次数统计、blog 浏览次数统计。
    - 增加音乐播放器功能。
- v2.0.0：
    - 删除了一些功能，添加了一些功能，修改了一些功能。
    - 前端完全采用 Bootstrap4.4.0 重写。

---

### v1.0.0 series

- v1.6.0：
    - 增加 messageboard app,留言功能。
    - 数据库文件为空文件，所以如果你要运行这个版本代码，需要在终端 mysite 目录下运行两条命令迁移数据库：`python manage.py makemigrations`，`python manage.py migrate`，再启动服务。
- v1.5.0：
    - 增加 watchlist 应用。
    - 去除 polls 应用中的 film 功能。
    - 优化 html 文件代码。
- v1.4.0：
    - 将 polls 应用中的 image 改成单独的应用 photos。
- v1.3.0：
    - 增加用户登录，登录、注册、修改密码、重置密码。
    - 调整了文件上传功能页面的展示，修复一些问题。
    - 博客功能中增加功能：后台添加提示。
- v1.2.0：
    - 完善文件上传与下载功能，之前的版本中，文件下载功能只能下载我添加的文件，这一版本，文件的上传与下载一体化，上传的文件下载通过 Web 端实现。
    - 前端部分页面开始使用 Bootstrap4，改进页面展示。
- v1.1.0：
    - 增加 blog 应用。
- v1.0.0：
    - 在 v0.0.1 基础上，构建个人网站，主要包括：
        - 官方的投票应用。
        - 文件上传与下载。

---

### v0.0.0 series

- v0.0.1
    - Django 官方教程，一个调查投票应用。
    - 地址：https://docs.djangoproject.com/zh-hans/3.1/intro/tutorial01/
