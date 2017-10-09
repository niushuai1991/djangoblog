# coding:utf-8
'''
Created on 2017年10月8日

@author: niushuai
'''
from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=64)
    content = models.TextField(null=True)
    
    def __unicode__(self):
        return self.name
    
    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]), ensure_ascii=False)
