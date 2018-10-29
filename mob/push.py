#!/usr/bin/env python
# encoding: utf-8

'''
@Created: 2018年2月7日
@author: hlliu
@site: http://wiki.mob.com/mobpush-rest-api-接口文档/#map-0
@version: 1.0.0
@note: 发送推送、查询推送详情
'''

from tools import tools
import json

class push():
    
    pushUrl = "http://api.push.mob.com" 
    
    # 推送详情（根据workno查询）
    def getPushByWorkno(self, workno):
        if workno.strip() == '':
            return {'status':-1,'error':'workno is null'}
        path = '%s%s%s' % (self.pushUrl , "/push/workno/" , workno)
        result=tools().web_get(path,'')
        return result
    
    # 推送详情（根据batchId查询）
    def getPushByBatchId(self, batchId):
        if batchId.strip() == '':
            return {'status':-1,'error':'batchId is null'}
        path = '%s%s%s' % (self.pushUrl , "/push/id/" , batchId)
        result=tools().web_get(path,'')
        return result
    
    
    # 发送推送
    def sendPush(self,pushwork):
        print('')
        if pushwork is None:
            return {'status':-1,'error':'pushwork is null'}
        appkey = pushwork['appkey']
        if appkey is None or appkey.strip() == '':
            return {'status':-1,'error':'appkey is null'}
        target = pushwork['target']
        if target is None:
            return {'status':-1,'error':'target is null'}
        type = pushwork['type']
        if type is None:
            return {'status':-1,'error':'type is null'} 
        content = pushwork['content']
        if content is None:
            return {'status':-1,'error':'content is null'} 
        path = '%s%s' % (self.pushUrl , "/v2/push")
        result=tools().web_post(path,pushwork)
        return result
    
      
    # push消息初始化
    # type = 1 通知， type = 2 自定义
    # plats 数组格式，包含 android 和 iOS 为 [1,2]
    def initPush(self, appkey, workno = None, plats = [1,2], content = None, push_type = 1):
        panel = {}
        if appkey is not None:
            panel['appkey'] = appkey
        if workno is not None:
            panel['workno'] = workno    
        if plats is not None:
            panel['plats'] = plats
        if content is not None:
            panel['content'] = content    
        if push_type is not None:
            panel['type'] = push_type
        return panel
        
    # 设置扩展信息    
    def buildExtra(self, unlineTime = 1, extras = None, iosProduction = 1):
        panel = {} 
        if extras is not None:
            panel['extras'] = extras     
        return panel
         
    # 设置推送范围 
    # target:推送范围:1广播；2别名；3标签；4regid；5地理位置;6用户分群
    # tags 、alias 、     registrationIds是数组方式
    def buildTarget(self, target = 1, tags = None, alias = None, registrationIds = None, city = None, block = None):
        panel = {}
        if target is None:
            return panel 
        panel['target'] = target
        if target == 1:
            return panel
        elif target == 2:
            if alias is not None:
                panel['alias'] = alias
        elif target == 3:
            if tags is not None:
                panel['tags'] = tags
        elif target == 4:
            if registrationIds is not None:
                panel['registrationIds'] = registrationIds
        elif target == 5:
            if city.strip() == '':   
                panel['city'] = city
        elif target == 6:
            if block.strip() == '':   
                panel['block'] = block     
		panel['target'] = target				
        return panel   
        
    # 设置Android信息
    # androidTitle : 0(普通通知)，1(大段文字内容)，2(大图模式),3(横幅通知) 
    # androidContent 样式具体内容： 0、默认通知无； 1、长内容则为内容数据； 2、大图则为图片地址； 3、横幅则为多行内容
    def buildAndroid(self, androidTitle = None, androidstyle = None, androidContent = None,
                     androidVoice = None, androidShake = None, androidLight = None):
        panel = {}
        if androidTitle is not None:
            panel['androidTitle'] = androidTitle
        if androidstyle is not None:
            panel['androidstyle'] = androidstyle
        if androidContent is not None:
            panel['androidContent'] = androidContent
        if androidVoice is not None:
            panel['androidVoice'] = androidVoice
        if androidShake is not None:
            panel['androidShake'] = androidShake
        if androidLight is not None:
            panel['androidLight'] = androidLight 
        return panel

    # 设置IOS信息
    def bulidIos(self, iosTitle = None, iosSubtitle = None, iosSound = 'default', iosBadge = 1, iosCategory = None,
             iosSlientPush = None, iosContentAvailable = None, iosMutableContent = None):
        panel = {}
        if iosTitle is not None:
            panel['iosTitle'] = iosTitle
        if iosSubtitle is not None:
            panel['iosSubtitle'] = iosSubtitle
        if iosSound is not None:
            panel['iosSound'] = iosSound
        if iosBadge is not None:
            panel['iosBadge'] = iosBadge
        if iosCategory is not None:
            panel['iosCategory'] = iosCategory
        if iosSlientPush is not None:
            panel['iosSlientPush'] = iosSlientPush
        if iosContentAvailable is not None:
            panel['iosContentAvailable'] = iosContentAvailable
        if iosMutableContent is not None:
            panel['iosMutableContent'] = iosMutableContent  
        return panel
        
 
 
