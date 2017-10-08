# coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import json

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
