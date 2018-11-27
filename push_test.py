import unittest

from mob.push import push
from mob.tools import tools

appkey = "28cab3f162ef8"


# appSecret = "9148284e3337396201415fe78be0f05a"

class PushTest(unittest.TestCase):
    def test1(self):
        print("【条件】不传appkey或appSecret", end='')
        # 初始化推送
        panel = push().initPush(appkey=None, content='content test', plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=1, tags=None, alias=None, registrationIds=None, city=None, block=None)
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1)
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test2(self):
        print("【条件】错误的appkey或appSecret", end='')
        # 初始化推送
        panel = push().initPush(appkey="aaaaaaaa", content='content test', plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=1, tags=None, alias=None, registrationIds=None, city=None, block=None)
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1)
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test3(self):
        print("【条件】不传plat或者错误的plat", end='')
        # 初始化推送
        panel = push().initPush(appkey="aaaaaaaa", content='content test', plats=[])
        # 设置推送范围
        target = push().buildTarget(target=1, tags=None, alias=None, registrationIds=None, city=None, block=None)
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1)
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test4(self):
        print("【条件】target=1 广播", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='content test', plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=1, tags=None, alias=["alias_1", "alias_2"], registrationIds=None, city=None,
                                    block=None)
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')

        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1)
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test5(self):
        print("【条件】target=2 别名推送", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='content test', plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=2, tags=None, alias=["alias_1", "alias_2"], registrationIds=None, city=None,
                                    block=None)
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')

        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1)
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test6(self):
        print("【条件】target=3 标签推送", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='content test', plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=3, tags=["tag_1", "tag_2"], alias=None, registrationIds=None, city=None,
                                    block=None)
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1)
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test7(self):
        print("【条件】target=4 regid推送", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='content test', plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=4, tags=["tag_1", "tag_2"], alias=None,
                                    registrationIds=["5bf22f1266ffeffe19f93998"], city=None,
                                    block=None)
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1)
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test8(self):
        print("【条件】target=5 地理位置金华推送", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='content test', plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=5, tags=["tag_1", "tag_2"], alias=None,
                                    registrationIds=["5bf22f1266ffeffe19f93998"], city="金华",
                                    block=None)
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1)
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test9(self):
        print("【条件】target=5 地理位置杭州推送", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='content test', plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=5, tags=["tag_1", "tag_2"], alias=None,
                                    registrationIds=["5bf22f1266ffeffe19f93998"], city="杭州",
                                    block=None)
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1)
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test10(self):
        print("【条件】target=6 用户分群推送", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='content test', plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=6, tags=["tag_1", "tag_2"], alias=None,
                                    registrationIds=["5bf22f1266ffeffe19f93998"], city="杭州",
                                    block="1")
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1)
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test11(self):
        print("【条件】moblink推送", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='content test', plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=4, tags=["tag_1", "tag_2"], alias=None,
                                    registrationIds=["5bf22f1266ffeffe19f93998"], city="杭州",
                                    block="1")
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1, scheme="mlink://com.mob.mobpush.link", data='{"key1":"value"}')
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test12(self):
        print("【条件】推送内容为空", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='', plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=4, tags=["tag_1", "tag_2"], alias=None,
                                    registrationIds=["5bf22f1266ffeffe19f93998"], city="杭州",
                                    block="1")
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1, scheme="mlink://com.mob.mobpush.link", data='{"key1":"value"}')
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test13(self):
        print("【条件】自定义消息推送", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='content test', push_type=2, plats=[1, 2])
        # 设置推送范围
        target = push().buildTarget(target=4, tags=["tag_1", "tag_2"], alias=None,
                                    registrationIds=["5bf22f1266ffeffe19f93998"], city="杭州",
                                    block="1")
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1, scheme="mlink://com.mob.mobpush.link", data='{"key1":"value"}')
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test14(self):
        print("【条件】超过1000个标签推送", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='content test', push_type=1, plats=[1, 2])
        # 设置推送范围
        number = 0
        tag = []
        while number < 1002:
            number = number + 1
            tag.append("tag_{number}".format(number=number))
        target = push().buildTarget(target=3, tags=tag, alias=None,
                                    registrationIds=["5bf22f1266ffeffe19f93998"], city="杭州",
                                    block="1")
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1, scheme="mlink://com.mob.mobpush.link", data='{"key1":"value"}')
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test15(self):
        print("【条件】超过1000个别名推送", end='')
        # 初始化推送
        panel = push().initPush(appkey=appkey, content='content test', push_type=1, plats=[1, 2])
        # 设置推送范围
        number = 0
        alias = []
        while number < 1002:
            number = number + 1
            alias.append("alias_{number}".format(number=number))
        target = push().buildTarget(target=2, tags=None, alias=alias,
                                    registrationIds=["5bf22f1266ffeffe19f93998"], city="杭州",
                                    block="1")
        # 设置Android定制信息
        android = push().buildAndroid(androidTitle='安卓标题')
        # 设置iOS 定制信息
        ios = push().bulidIos(iosTitle='ios 标题')
        # 设置推送扩展信息
        extra = push().buildExtra(unlineTime=1, scheme="mlink://com.mob.mobpush.link", data='{"key1":"value"}')
        js = tools().json_join(panel, target)
        js = tools().json_join(js, android)
        js = tools().json_join(js, ios)
        js = tools().json_join(js, extra)
        res = push().sendPush(js)
        print("【结果】：", end='')
        print(res)

    def test16(self):
        print("【条件】传入正确workno查询", end='')
        workno = "230714933537218560"
        res = push().getPushByWorkno(workno)
        print("【结果】：", end='')
        print(res)

    def test17(self):
        print("【条件】传入正确batchId查询", end='')
        batchId = "5bfcf48666ffeffe1a03a04c"
        res = push().getPushByBatchId(batchId)
        print("【结果】：", end='')
        print(res)


if __name__ == '__main__':
    unittest.main()
