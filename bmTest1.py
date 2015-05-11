#!/usr/bin/python
# -*- coding:utf8 -*-

import os
import sys

def main1():
    path = sys.path[0]+'/md/'
    files = os.listdir(path)
    for f in files:
        print files
        if os.path.isdir(path + '/md/' + f):
            #print "floder",os.stat(f)
            pass
        #else:
            #print "file",os.stat(f).st_mtime
        


def copyFileContent(reader,writer,n=-1):
    if n == -1:
        for r in reader:
            writer.write(r)
    else:
        for i in range(0,10):
            writer.write(reader.readline())


def insertInfo(mark,line,writer,readerPath):
    tmpArr = line.split('#content#')
    reader = open(readerPath,'r')
    if len(tmpArr) == 2:
        writer.write(tmpArr[0])
        copyFileContent(reader,writer)
        writer.write(tmpArr[1])
    elif len(tmpArr) == 1:
        if line.startswith('#content#'):
            copyFileContent(reader,writer)
            writer.write(tmpArr[0])
        elif line.endswith('#content#'):
            writer.write(tmpArr[0])
            copyFileContent(reader,writer)
    else:
        copyFileContent(reader,writer)
    reader.close()



def getContentView():
    fileOrFolder = os.listdir(sys.path[0]+'/content/')
    for ff in fileOrFolder:
        if os.path.isdir('content/'+ff):
            files = os.listdir('content/'+ff)
            for f in files:
                templateFile = open(sys.path[0]+'/template/content.html','r')
                contentFile = open(sys.path[0]+'/blog/'+ff+'/'+f+'.html','w')
                for line in templateFile:
                    if '#content#' in line:
                        insertInfo('#content#',line,contentFile,'content/'+ff+'/'+f)
                    else:
                        contentFile.write(line)
                templateFile.close()
                contentFile.close()


        else:
            templateFile = open(sys.path[0]+'/template/content.html','r')
            contentFile = open(sys.path[0]+'/blog/'+ff+'.html','w')
            for line in templateFile:
                if '#content#' in line:
                    insertInfo('#content#',line,contentFile,'content/'+ff)
                else:
                    contentFile.write(line)
            templateFile.close()
            contentFile.close()
       

def getCateList():
    
    listFile = open(sys.path[0]+'/blog/cate_list.html','w')
    bashPath = sys.path[0]
    contentPath = bashPath+'/content/'
    cates = os.listdir(contentPath)
    #cateUrlTemplate = '%s/index.html'
    for c in cates:
        if os.path.isdir(contentPath+c):
            cateUrl = c+'/index.html'
        else:
            cateUrl = c+'.html'
        tabA = '<a href="%s">%s</a>\n' % (cateUrl,c)
        listFile.write(tabA)

    listFile.close()

def getAllBlogList():
    bashPath = sys.path[0]
    contentPath = bashPath+'/content/'
    cates = os.listdir(contentPath)
    for c in cates:
        if os.path.isdir(contentPath+c):
            catePath = 'blog/'+c
            if os.path.exists(catePath) == False:
                os.mkdir(catePath)
            blogListFile = open('blog/'+c+'/index.html','w')
            
            blogs = os.listdir('content/'+c)
            for b in blogs:
                blogUrl = '%s.html' % b
                #blogUrl = 'blog/%s/%s.html' % (c,b)
                tabA = '<a href="%s">%s</a><br/>' % (blogUrl,b)
                blogListFile.write(tabA)

            blogListFile.close()


def main():
    
    getCateList()
    getAllBlogList()
    getContentView()

if __name__ == '__main__':
    #print os.path.isdir('content/tmp')
    main()