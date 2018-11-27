#!/usr/bin/env python
# encoding: utf-8

'''
@Created: 2018年2月7日
@author: hlliu
@site: http://wiki.mob.com/mobpush-rest-api-接口文档/#map-0
@version: 1.0.0
@note: 设备相关接口实现： 别名查询、别名设置、别名清除、标签查询、标签新增、标签删除、标签清除
'''

import json

from mob.tools import tools


class device:
    deviceUrl = 'http://api.push.mob.com'

    # 获取设备别名,返回别名
    def getDeviceAlias(self, registrationId):
        if registrationId.strip() == '':
            return {'status': -1, 'error': 'registrationId is null'}
        path = '%s%s%s' % (self.deviceUrl, '/alias/', registrationId)
        req = tools().web_get(path, '')
        alias = req.get("alias")
        return alias

    # 设置设备别名
    def setDeviceAlias(self, registrationId, alias):
        if registrationId.strip() == '':
            return {'status': -1, 'error': 'registrationId is null'}
        path = '%s%s' % (self.deviceUrl, '/alias')
        jsondata = {'alias': alias, 'registrationId': registrationId}
        req = tools().web_post(path, jsondata)
        error = req.get("error")
        if error is None or error.strip() == '':
            return json.dumps({'status': 200});
        else:
            return req;

    # 清除设备别名
    def cleanDeviceAlias(self, registrationId):
        return self.setDeviceAlias(registrationId, '')

    # 获取设备标签    
    def getDeviceTags(self, registrationId):
        if registrationId.strip() == '':
            return {'status': -1, 'error': 'registrationId is null'}
        path = '%s%s%s' % (self.deviceUrl, '/tags/', registrationId)
        req = tools().web_get(path, '')
        tags = req.get("tags")
        return tags

    # 绑定设置设备标签    
    def addDeviceTags(self, tags, registrationId):
        if tags is None:
            return {'status': -1, 'error': 'tags is null'}
        if registrationId.strip() == '':
            return {'status': -1, 'error': 'registrationId is null'}
        path = '%s%s' % (self.deviceUrl, '/tags')
        jsondata = {'tags': tags, 'registrationId': registrationId, "opType": 1}
        req = tools().web_post(path, jsondata)
        error = req.get("error")
        if error is None or error.strip() == '':
            return json.dumps({'status': 200});
        else:
            return req;

    # 解绑设备标签 
    def removeDeviceTags(self, tags, registrationId):
        if tags is None:
            return {'status': -1, 'error': 'tags is null'}
        if registrationId.strip() == '':
            return {'status': -1, 'error': 'registrationId is null'}
        path = '%s%s' % (self.deviceUrl, '/tags')
        jsondata = {'tags': tags, 'registrationId': registrationId, "opType": 2}
        req = tools().web_post(path, jsondata)
        error = req.get("error")
        if error is None or error.strip() == '':
            return json.dumps({'status': 200});
        else:
            return req;

    # 清除设备标签 
    def cleanDeviceTags(self, registrationId):
        if registrationId.strip() == '':
            return {'status': -1, 'error': 'registrationId is null'}
        path = '%s%s' % (self.deviceUrl, '/tags')
        jsondata = {'registrationId': registrationId, "opType": 3}
        req = tools().web_post(path, jsondata)
        error = req.get("error")
        if error is None or error.strip() == '':
            return json.dumps({'status': 200});
        else:
            return req;
