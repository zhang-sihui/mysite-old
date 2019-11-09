1. 一个blog有搜索功能实在是再正常不过了，今天就来看看如何实现一个简单的blog搜索功能。 
2. 搜索就是输入关键词搜索与标题相关的文章，先构思搜索功能的一般流程：前端一个输入栏，一个搜索按钮，输入关键词，提交；后端获取关键词，再数据库中搜索标题中含有关键词的标题，然后将搜索到的结果展示到前端。大致就是这样的流程。
3. 具体实现如下：
	1. 搜索函数的实现：  
	`def search(request):  
		q = request.GET.get('q')  
    	contexts = Article.objects.all().order_by('-pub_date')[:5]
    	search_list = Article.objects.filter(title__icontains=q)
    	error_msg = 'No result'
    	return render(request, 'blog/search.html', {'search_list': search_list,
                                                'error_msg': error_msg,
                                                'contexts': contexts})`
	
		'q'是前端input标签name属性的名字，稍后再说。代码第二行就是获取前端输入框里关键字。第三、四行是在数据库中查询，第三行查询所有文件，第四行查询标题中包含关键词的内容。有的文章中有判断q是否为空，其实完全没有必要，在前端html代码中会说明。

	2. 数据模型的实现：  
	`class Article(models.Model):  
	    title = models.CharField(max_length=200)  
	    category = models.CharField(max_length=100, default='programming')
    	body = MDTextField()
    	pub_date = models.DateTimeField('datepublished',default=timezone.now)

    	def __str__(self):  
        	return self.title`  

		模型中创建的几个字段，标题，分类，主体内容，发布时间。

    3. 前端html实现：  
    `<form method="get" action="{% url 'blog:search' %}">
                {% csrf_token %}
                <input class="txt" type="search" name="q" placeholder="Search" required>
                <button type="submit" value="Search">Search</button>
            </form>`

    	注意到input标签中name的值q与搜索方法中的q相同，还有一个required，这个值说明输入该不能为空，有个这个值，后端的搜索方法中就不需要判断q是否为空。action设置url。

	4. urld的实现：  
	`path('search/', views.search, name='search'),
	`
	
	5. 最后是获取的文章展示：  
	`{% if search_list %}
        {% for search in search_list %}
			{{ search }}
		{% endfor %}
	{% else %}
		{{ error_msg }}
	{% endif %}`
			
			