# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:22:07 2018
可以上传一个文件夹中所有子文件
@author: Z
"""
from qiniu import Auth, put_file, etag
import qiniu.config
import os

#TODO 填写参数
path = '' 
access_key = ''
secret_key = ''
#要上传的空间
bucket_name = ''

#构建鉴权对象
q = Auth(access_key, secret_key)

def dfsFile(path,func=print):
    for file in os.listdir(path):
        fullPath = os.path.join(path,file)
        if os.path.isdir(fullPath):
            dfsFile(fullPath,func)
        else:
            func(file,fullPath)

def upload(file,fullPath):
    key = 'CASIA-FaceV5/{}'.format(file)
    token = q.upload_token(bucket_name,key)
    localfile = fullPath
    ret, info = put_file(token, key, localfile)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)
    
dfsFile(path,upload)

#上传到七牛后保存的文件名
#key = 'my-python-logo.png'
#生成上传 Token，可以指定过期时间等
#token = q.upload_token(bucket_name, key, 3600)
#要上传文件的本地路径
#localfile = './sync/bbb.jpg'
#ret, info = put_file(token, key, localfile)
#print(info)
#assert ret['key'] == key
#assert ret['hash'] == etag(localfile)