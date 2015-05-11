#!/usr/bin/python
#coding=utf-8
import os

def main():
    fw = open('test.html','w')
    files = os.listdir('./')
    for f in files:
        print f
        fw.write('<a href="#">%s</a><br/>' % f.decode('gbk').encode('utf-8'))
    
    fw.close()

if __name__ == '__main__':
    main()