#1.概述

基于七牛API及Plupload开发的前端JavaScript SDK

示例：七牛JavaScript SDK 示例网站 - 配合七牛Node.js SDK

源码：https://github.com/qiniupd/qiniu-js-sdk/

下载：https://github.com/qiniupd/qiniu-js-sdk/releases

本SDK适用于IE8+、Chrome、Firefox、Safari 等浏览器，基于 七牛云存储官方API 构建，其中上传功能基于 Plupload 插件封装。开发者使用本 SDK 可以方便的从浏览器端上传文件至七牛云存储，并对上传成功后的图片进行丰富的数据处理操作。本 SDK 可使开发者忽略上传底层实现细节，而更多的关注 UI 层的展现。


##功能简介

上传
html5模式大于4M时可分块上传，小于4M时直传
Flash、html4模式直接上传
继承了Plupload的功能，可筛选文件上传、拖曳上传等
下载(公开资源)
数据处理（图片）
imageView2（缩略图）
imageMogr2（高级处理，包含缩放、裁剪、旋转等）
imageInfo （获取基本信息）
exif （获取图片EXIF信息）
watermark （文字、图片水印）
pipeline （管道，可对imageView2、imageMogr2、watermark进行链式处理）

###SDK构成介绍

*Plupload ，建议 2.1.1 及以上版本
qiniu.js，SDK主体文件，上传功能\数据处理实现*