1. pythonanywhere项目中，admin管理站点CSS不展示的解决方法
2. 由于admin app的html模板是直接继承admin/base.html，导致在pythonanywhere上部署项目时，缺少css文件，所以admin界面不显示css格式。
3. 解决方法如下：
	0. 说明：mysite(项目主目录，下简称【主】)，mysite（主）下有mysite（次目录）文件夹，次目录文件夹含有配置文件settings。
	1. 在settings(mysite[次])中设置STATIC_ROOT，STATIC_ROOT = "/home/myusername/myproject/static"，或者STATIC_ROOT = os.path.join(BASE_DIR, "static")。这时你的配置文件中可能存在Django自建的STATIC_URL = '/static/'，但是没关系，直接在它下面新配置即可。
	2. 在mysite(主)下，运行python3.7 manage.py collectstatic (或者 python2.7 或 python3.6，换上你的python版本)。这个命令会在mysite（主）下创建static文件夹，当然可能你已经含有，命令成功后，文件夹会多出一些文件，这些文件就是命令收集到的css文件，用以渲染admin前端界面的。
	3. 完成以上步骤，在"Web"中，设置静态文件路径（Static files）。URL设置/static/即可，Directory设置为/home/username/mysite/static即可。回到最顶上，重新加载项目，即可访问网页。
	4. 注意：以上username是你的pythonanywhere用户名，mysite是你的项目名，记得修改。
4. 你可以查看官方文档：[pythonanywhere help](https://help.pythonanywhere.com/pages/DjangoStaticFiles)