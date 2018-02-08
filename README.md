# [MobPush API for Python](http://wiki.mob.com/mobpush-rest-api-接口文档/)

![image](https://github.com/MOBX/MOB-SMS-WEBAPI/blob/master/doc/images/logo.png)

**[MobPush API for Python](http://wiki.mob.com/mobpush-rest-api-接口文档/)** 
为了帮助开发者更方便接入MobPush免费推送SDK，提供完整的API接口的python实现，包含设备操作相关接口、推送操作相关接口以及公共接口。

了解更多 [MobPush 免费推送SDK.](http://mobpush.mob.com)


## 优势

**免费使用**、**自定义UI**、**稳定服务**、**流程体验**、**数据同步**、**专业技术团队服务**

## 接口
* 推送接口
	* 发送推送
	* 查询推送（根据batchId）
	* 查询推送（根据workno）
* 推送统计接口
	* 查询推送统计（根据batchId）
	* 查询推送统计（根据workno）
* 别名操作接口
	* 查询别名
	* 设置别名
* 标签操作接口
	* 查询标签
	* 设置标签
* 公共接口
	* 地理位置信息接口	

 
## 使用注意事项
* 初始化appkey、appSecret , 可以在 mob目录下tools.py 设置
* 错误码请参考 
  [MobPush Api 错误码](http://wiki.mob.com/mobpush-rest-api-接口文档/#map-6)

## 使用DEMO 

发送推送示例片段代码

```xml    
    # 初始化推送
    panel = push().initPush(appkey='moba6b6c6d6', content = 'content test', plats = [1,2]) 
    # 设置推送范围
    target = push().buildTarget(target = 1, tags = None, alias = None, registrationIds = None, city = None, block = None)
    # 设置Android定制信息
    android = push().buildAndroid(androidTitle = '安卓标题')    
    # 设置iOS 定制信息
    ios= push().bulidIos(iosTitle = 'ios 标题')
    # 设置推送扩展信息   
    extra = push().buildExtra(unlineTime = 1) 

    js = tools().json_join(panel, target)
    js = tools().json_join(js,android)
    js = tools().json_join(js,ios) 
    js = tools().json_join(js,extra) 
    res = push().sendPush(js)
    print(res)

 
```