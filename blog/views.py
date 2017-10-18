# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import json
import models

def index(request):
	''' 直接返回文本 ''' 
	return HttpResponse('Hello index')

def hello(request):
	''' 渲染页面 '''
	return render(request, 'blog/hello.html')

def json_data(request):
	''' 模拟数据返回 '''
	resp = {'title': '张三', 'score': 30}
	return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type='application/json; charset=utf-8')

def article_json(request):
	article = models.Article.objects.get(id=1)
	return HttpResponse(article.toJSON(), content_type='application/json; charset=utf-8')

def article(request, article_id):
	''' 渲染model '''
	article = models.Article.objects.get(id=article_id)
	return render(request, 'blog/article.html', {'article': article})

def article_list(request):
	''' 获取所有的文章 '''
	articles = models.Article.objects.all()
	return render(request, 'blog/articleList.html', {'articles': articles})

def edit(request, article_id):
	article = None
	if str(article_id) != '0' :
		article = models.Article.objects.get(id=article_id)
	return render(request, "blog/edit.html", {'article': article})

def edit_action(request):
	article_id = request.POST.get('article_id')
	title = request.POST.get('title', 'title demo')
	content = request.POST.get('content', 'content')
	if article_id == None:
		models.Article.objects.create(title=title, content=content)
	else:
		article = models.Article.objects.get(pk=article_id)
		article.title = title
		article.content = content
		article.save()
	articles = models.Article.objects.all()
	return render(request, 'blog/articleList.html', {'articles': articles})