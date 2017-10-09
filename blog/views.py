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
	resp = {'name': '张三', 'score': 30}
	return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type='application/json; charset=utf-8')

def article_json(request):
	article = models.Article.objects.get(id=1)
	return HttpResponse(article.toJSON(), content_type='application/json; charset=utf-8')

def article(request):
	''' 渲染model '''
	article = models.Article.objects.get(id=1)
	return render(request, 'blog/article.html', {'article': article})

def articleAll(request):
	''' 获取所有的文章 '''
	articles = models.Article.objects.all()
	return render(request, 'blog/articleList.html', {'articles': articles})