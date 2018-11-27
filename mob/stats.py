#!/usr/bin/env python
# encoding: utf-8

'''
@Created: 2018年2月7日
@author: hlliu
@site: http://wiki.mob.com/mobpush-rest-api-接口文档/#map-0
@version: 1.0.0
@note: 推送统计信息
'''

import json

from mob.tools import tools


class stats():
    statsUrl = "http://api.push.mob.com"

    # 获取统计数据(根据workno查询)
    def getStatsByWorkno(self, workno):
        if workno.strip() == '':
            return {'status': -1, 'error': 'workno is null'}
        path = '%s%s%s' % (self.statsUrl, "/stats/workno/", workno)
        result = tools().web_get(path, '')
        return result

    #  获取统计数据(根据batchId查询) 
    def getStatsByBatchId(self, batchId):
        if batchId.strip() == '':
            return {'status': -1, 'error': 'batchId is null'}
        path = '%s%s%s' % (self.statsUrl, "/stats/id/", batchId)
        result = tools().web_get(path, '')
        return result
