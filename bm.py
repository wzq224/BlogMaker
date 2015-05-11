#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import sys


BASH_PATH = sys.path[0]
TEMPLATE_PATH = BASH_PATH+'/template/'
BLOG_PATH = BASH_PATH+'/blog/'
CONTENT_PATH = BASH_PATH+'/content/'


def code(s):
    return s.decode('gbk').encode('utf-8')

def copyFileContent(reader,writer,n=-1):
    if n == -1:
        for r in reader:
            writer.write(r)
    else:
        for i in range(0,10):
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


def makeBlogListOnCate():  
    fileOrFolder = os.listdir(CONTENT_PATH)
    for ff in fileOrFolder:
        ffPath = CONTENT_PATH+ff
        blogListName = BLOG_PATH+ff+'-list.html'
        blogListTemp = open(TEMPLATE_PATH+'blog-list-on-cate.html','r')
        if os.path.isdir(ffPath):
            blogListFile = open(blogListName,'w')
            blogs = os.listdir(ffPath)
            for line in blogListTemp:
                if '#title#' in line:
                    blogListFile.write(line.replace('#title#',ff+'-list'))
                elif '#blog_list#'in line:
                    for blogName in blogs:
                        url = '%s-%s.html' % (ff,blogName)
                        tabA = '<a href="%s">%s</a>' % (code(url),code(blogName))
                        print tabA
                        blogListFile.write(line.replace('#blog_list#',tabA))
                else:
                    blogListFile.write(line) 
            blogListFile.close()
        blogListTemp.close()

def makeBlog(tempPath,contentPath,blogPath,mark,cateName,blogName):
    tempFile = open(tempPath,'r')
    blogFile = open(blogPath,'w')
    for line in tempFile:
        if '#title#' in line:
            blogFile.write(line.replace('#title#',blogName+cateName))
        elif mark in line:
            insertInfo(mark,line,blogFile,contentPath)
        elif '#cate#' in line:
            makeCateList(line,blogFile)
        else:
            blogFile.write(line)
    tempFile.close()
    blogFile.close()

def makeAllBlogs():
    blogTempPath = TEMPLATE_PATH+'blog-content.html'
    fileOrFolder = os.listdir(CONTENT_PATH)
    for ff in fileOrFolder:
        ffPath = CONTENT_PATH+ff
        
        if os.path.isdir(ffPath):
            files = os.listdir(ffPath)
            for f in files:
                makeBlog(blogTempPath,ffPath+'/'+f,BLOG_PATH+ff+'-'+f+'.html','#content#',ff,f)
        else:
            makeBlog(blogTempPath,ffPath,BLOG_PATH+ff+'.html','#content#',ff,'')


def makeCateList(line,writer,mark='#cate#'):
    cates = os.listdir(CONTENT_PATH)
    for cate in cates:
        if os.path.isdir(CONTENT_PATH+cate):
            url = cate+'-list.html'
        else:
            url = cate+'.html'
        tabA = '<a href="%s">%s</a>' % (url,cate)
        writer.write(line.replace(mark,tabA))
    

    

def getAllBlogs():
    blogList = []
    cates = os.listdir(CONTENT_PATH)
    for cate in cates:
        if os.path.isdir(CONTENT_PATH+cate):
            blogs = os.listdir(CONTENT_PATH+cate)
            for blog in blogs:
                blogList.append(os.stat(CONTENT_PATH+cate+'/'+blog))
        else:
            blogList.append(os.stat(CONTENT_PATH+cate))
    
    fw = open('tmp.html','w')
    for blog in blogList:
        fw.write('<h2><a href="#">%s</a><h2>' % str(blog))
    fw.close()

def main():
    getAllBlogs()
    #makeBlogListOnCate()
    #makeAllBlogs()

if __name__ == '__main__':
    main()