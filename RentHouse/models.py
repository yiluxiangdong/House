#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class BaseModel(models.Model):
    delete_flag = models.CharField(max_length=4, verbose_name='删除标志',default='1')
    class Meta:
        abstract=True


class  HostInfo(BaseModel):
    ip = models.CharField(max_length=100,  verbose_name='服务器ip')
    createTime=models.CharField(max_length=100,  verbose_name='创建时间')
    def __str__(self):
        return self.ip
