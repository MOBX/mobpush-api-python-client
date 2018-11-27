#!/usr/bin/env python
# encoding: utf-8

'''
@Created: 2018年2月7日
@author: hlliu
@site: http://wiki.mob.com/mobpush-rest-api-接口文档/#map-0
@version: 1.0.0
@note: 获取地理位置列表信息
'''

from mob import tools
import json

class area():
    
    baseUrl = "http://api.push.mob.com" 
    
    # 获取地理位置列表 -- 子级列表
    def getArea(self, parentId = '0'): 
        path = '%s%s%s' % (self.baseUrl , "/area/" , parentId)
        result=tools().web_get(path,'')
        return result
     