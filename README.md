#### Introduction

A personal website

Terminal: Go to mysite folder(终端：进入mysite文件夹)  
Enter the following command, then enter（输入以下命令，回车运行）  
"python manage.py runserver"
  
http://127.0.0.1:8000/  
user UI(用户)  
http://127.0.0.1:8000/admin/  
admin UI(管理)

Version 0.0.1 is the official Django tutorial content,  
starting with version 1.0.0 for personal website content.  
(版本0.0.1为Django官方教程内容，从版本1.0.0开始，为个人网站内容)


##### Table of Content
- v0.0.1  
    * Django官方教程,一个调查投票应用
- v1.0
    * v1.0.0:  
        在v0.0.1基础上，构建个人网站，主要包括：
        1. 官方的投票应用
        2. 文件上传与下载
    * v1.1.0:  
        1. 增加blog应用
    * v1.2.0:  
        1. 完善文件上传与下载功能，之前的版本中，文件下载功能只能下载我添加的文件，
        这一版本，文件的上传与下载一体化，上传的文件下载通过web端实现。 
        2. 前端部分页面开始使用bootstrap4，改进页面展示。        
    * v1.3.0:
        1. 增加用户登录，登录、注册、修改密码、重置密码。
        2. 调整了文件上传功能页面的展示，修复一些问题。
        3. 博客功能中增加功能：后台添加提示。
    * v1.4.0:
        1. 将polls应用中的image改成单独的应用photos。
    * v1.5.0:
        1. 增加watchlist应用。
        2. 去除polls应用中的film功能。
        3. 优化html文件代码。