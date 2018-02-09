#!/usr/bin/env python
# encoding: utf-8

'''
@Created: 2018年2月7日
@author: hlliu
@site: http://wiki.mob.com/mobpush-rest-api-接口文档/#map-0
@version: 1.0.0
@note: 公共工具
'''

from requests import get, post
import json
import hashlib
 
# 公共工具
class tools(object):

    # 需要配置的 APPKEY 需要先设置此数据，怎样获取appkey，请查看http://bbs.mob.com/forum.php?mod=viewthread&tid=8212&extra=page%3D1
    appkey=""
    # 需要配置APPKEY对应秘钥，需要填写
    appSecret=""
    http_status_200=200
    http_status_400=400
    default_error_code=-1
     
    def __init__(self):
        self.appkey = tools.appkey
        self.appSecret = tools.appSecret

    # MD5签名
    def sign_fun(self, jsondata, appsecret):
        if jsondata is None or jsondata == '':
            str_org=appsecret
        else:
            str_org='%s%s' % (json.dumps(jsondata), appsecret)
        md5_str=hashlib.md5(str_org.encode('utf-8')).hexdigest()
        return md5_str

    #HTTP POST 返回JSON格式，正常返回仅返回数据体，错误返回json错误内容
    def web_post(self, url, jsondata):
        if url.strip() == '':
            return {'status':-1,'error':'url is null'}
        if self.appkey.strip() == '':
            return {'status':-1,'error':'appkey is null'}
        if self.appSecret.strip() == '':
            return {'status':-1,'error':'appSecret is null'}
        sign = self.sign_fun(jsondata,self.appSecret)
        header = {'key':self.appkey,'sign':sign}
        req = post(url=url,data=json.dumps(jsondata),headers=header) 
        if req.json().get("status") == 200 :
            return req.json().get("res")
        else:
            return req.json()
    
    #HTTP GET 返回JSON格式，正常返回仅返回数据体，错误返回json错误内容
    def web_get(self, url, data): 
        if url.strip() == '':
            return {'status':-1,'error':'url is null'}
        if self.appkey.strip() == '':
            return {'status':-1,'error':'appkey is null'}
        if self.appSecret.strip() == '':
            return {'status':-1,'error':'appSecret is null'}
        sign = self.sign_fun(data,self.appSecret)
        header = {'key':self.appkey,'sign':sign}
        req = get(url=url,params=data,headers=header) 
        if req.json().get("status") == 200 :
            return req.json().get("res")
        else:
            return req.json()
    
 
    # JSON 拼接
    def json_join(self, json1 = None, json2 = None):
        jsondata = {}
        if json1 is not None:
            for index,item in enumerate(json1):  
                jsondata[item] = json1[item]
        if json2 is not None:  
            for index,item in enumerate(json2):  
                jsondata[item] = json2[item]
        return jsondata  
