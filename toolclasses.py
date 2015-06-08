#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import sys
import time


class BlogDO(object):
    """docstring for BlogDO"""
    __slots__ = ('id','title','content','cate','createTime','chgTime','name','path','url')
    def __init__(self,path):
        pathArr = path.split('/')[::-1]
        idname = pathArr[0].split('-')
        if len(idname) >= 2:
            self.name = idname[1]
            self.title = idname[1]
        else:
            self.name = pathArr[0]
            self.title = pathArr[0]

        self.cate = ''
        if len(pathArr) >= 3:
            idcate = pathArr[1].split('-')
            if len(idcate) >= 2:
                self.cate = idcate[1]
            else:
                self.cate = pathArr[1]

        else:
            self.cate = 'index'
        stat = os.stat(path)
        self.createTime = stat.st_ctime
        self.chgTime = stat.st_mtime
        self.path = path

    def getCreateTime(self):
        return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(self.createTime))

    def getCreateDate(self):
        return time.strftime("%Y/%m/%d",time.localtime(self.createTime)) 

    def getChgTime(self):
        return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(self.chgTime))

    def getUrl(self):
        return self.cate+'-'+self.name+'.html'

class CateDO(object):
    """docstring for CateDO"""
    __slots__ = ('id','name','path','url')
    def __init__(self, path):
        pathArr = path.split('/')[::-1]
        idname = pathArr[0].split('-')
        if len(idname) >= 2:
            self.id = int(idname[0])
            self.name = idname[1]
        else:
            self.name = pathArr[0]
            self.id = 0
        if os.path.isdir('content/'+path):
            self.url = self.name+'.html'
        else:
            self.url = 'index-'+self.name+'.html'
        self.path = path

    def getUrl(self):
        return self.url    

