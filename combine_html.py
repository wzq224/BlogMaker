#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import sys
import time


class BlogDO(object):
    """docstring for BlogDO"""
    __slots__ = ('id','title','content','cate','createTime','chgTime','name','path','url')
    def __init__(self,path):
        #pathArr = list(reversed(path.split('/')))
        pathArr = path.split('/')[::-1]
        
        self.name = pathArr[0]
        self.title = pathArr[0]
        if len(pathArr) >= 3:
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
        return self.cate+'-'+self.title+'.html'

class CateDO(object):
    """docstring for CateDO"""
    __slots__ = ('id','name','path','url')
    def __init__(self, path):
        pathArr = path.split('/')[::-1]  
        self.name = pathArr[0]
        if os.path.isdir('content/'+path):
            self.url = self.name+'-list.html'
        else:
            self.url = 'index-'+self.name+'.html'
        self.path = path
    def getUrl(self):
        return self.url    

def code(s):
    return s.decode('gbk').encode('utf-8')

def copyFileContent(reader,writer,n=-1):
    if n == -1:
        for r in reader:
            writer.write(r)
    else:
        for i in range(0,n):
            writer.write(reader.readline())


def insertInfo(mark,line,writer,readerPath):
    tmpArr = line.split(mark)
    reader = open(readerPath,'r')
    if len(tmpArr) == 2:
        writer.write(tmpArr[0])
        copyFileContent(reader,writer)
        writer.write(tmpArr[1])
    elif len(tmpArr) == 1:
        if line.startswith(mark):
            copyFileContent(reader,writer)
            writer.write(tmpArr[0])
        elif line.endswith(mark):
            writer.write(tmpArr[0])
            copyFileContent(reader,writer)
    else:
        copyFileContent(reader,writer)
    reader.close()

#把html组装成template
def combineHtml(htmlName):
    print htmlName
    writeFile = open('template/'+htmlName,'w')
    readeFile = open('template-html/'+htmlName,'r')
    for line in readeFile:
        if '<insert>' in line and '</insert>' in line :
            mark = line
            line = line.replace('<insert>','').replace('</insert>','').replace('\n','').replace('\t','')
            readerPath = 'template-html/common/'+line+'.html'
            insertInfo(mark,mark,writeFile,readerPath)
        else:
            writeFile.write(line)
    readeFile.close()
    writeFile.close()
    


def getCateList(pathName):
    cateList = []
    fileOrFolder = os.listdir(pathName)
    for ff in fileOrFolder:
        cateList.append(CateDO(ff))
    return cateList


#获取所有的BlogDO 按时间排序
def getIndexBlogList(pathName):
    blogList = []
    fileOrFolder = os.listdir(pathName)
    for ff in fileOrFolder:
        path = pathName+'/'+ff
        if os.path.isdir(path):
            fileOrFolder2 = os.listdir(path)
            for ff2 in fileOrFolder2:
                path2 = path+'/'+ff2
                if False == os.path.isdir(path2):
                    blogList.append(BlogDO(path2))
        else:
            blogList.append(BlogDO(path))
    return blogListSortByTime(blogList)

def blogListSortByTime(blogList):
    def sortedByTime(x,y):
        return cmp(y.getCreateTime(),x.getCreateTime())
    return sorted(blogList,sortedByTime)   

def createTemplate():
    fileOrFolder = os.listdir('template-html/')
    for ff in fileOrFolder:
        path =  'template-html/'+ff
        #print path
        if False == os.path.isdir(path):
            combineHtml(ff)

def writeList(contentList,listLine,writer,listType):
    tab1 = '<'+listType+'>'
    tab2 = '</'+listType+'>'
    tabA = listLine.replace('\t','').replace('\n','').replace(tab1,'').replace(tab2,'')
    for cl in contentList:
        line = tabA
        if '#url#' in line:
            line = line.replace('#url#',cl.getUrl())
        if '#date#' in line:
            line = line.replace('#date#',cl.getCreateDate())
        if '#name#' in line:
            line = line.replace('#name#',cl.name)
        writer.write(code(line))

   
    
#生成index.html 按时间排序的所有博文
def makeIndex():
    blogList = getIndexBlogList('content')
    cateList = getCateList('content')
    indexFile = open('blog/index.html','w')
    templateFile = open('template/list.html','r')
    for line in templateFile:
        if '<bloglist>' in line:
            writeList(blogList,line,indexFile,'bloglist')
        elif '#title#' in line:
            indexFile.write(line.replace('#title#','home'))
        elif '<catelist>' in line:
            writeList(cateList,line,indexFile,'catelist')
        else:
            indexFile.write(line)
    templateFile.close()
    indexFile.close()


#根据BlogDO生成blog
def makeBlog(blog):
    tempFile = open('template/blog.html','r')
    blogFile = open('blog/'+blog.getUrl(),'w')
    cateList = getCateList('content')
    for line in tempFile:
        if '#title#' in line:
            blogFile.write(line.replace('#title#',code(blog.title+'-'+blog.cate)))
        elif '#content#' in line:
            insertInfo('#content#',line,blogFile,blog.path)
        elif '<catelist>' in line:
            writeList(cateList,line,blogFile,'catelist')
        # elif '#cate#' in line:
        #     makeCateList(line,blogFile)
        else:
            blogFile.write(line)
    tempFile.close()
    blogFile.close()

#生成所有博客
def makeAllBlog():
    blogList = getIndexBlogList('content')
    for b in blogList:
        makeBlog(b)

def main():
    cateList = getCateList('content')
    for c in cateList:
        print c.url

def main2():
    createTemplate()
    makeIndex()
    makeAllBlog()



if __name__ == '__main__':
    main2()