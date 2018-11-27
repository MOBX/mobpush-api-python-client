import unittest

from mob.device import device
from mob.push import push
from mob.tools import tools

appkey = "28cab3f162ef8"
rid = "5bf22f1266ffeffe19f93998"


# appSecret = "9148284e3337396201415fe78be0f05a"

class DeviceTest(unittest.TestCase):
    def test1(self):
        print("【条件】传入rid查询别名", end='')
        panel = device()
        res = panel.getDeviceAlias(rid)
        print("【结果】：", end='')
        print(res)

    def test2(self):
        print("【条件】传入rid设置,修改别名", end='')
        panel = device()
        res = panel.setDeviceAlias(rid, "alias_1")
        print("【结果】：", end='')
        print(res)

    def test3(self):
        print("【条件】传入rid清除别名", end='')
        panel = device()
        res = panel.cleanDeviceAlias(rid)
        print("【结果】：", end='')
        print(res)

    def test4(self):
        print("【条件】传入rid查询标签", end='')
        panel = device()
        res = panel.getDeviceTags(rid)
        print("【结果】：", end='')
        print(res)

    def test5(self):
        print("【条件】传入rid设置修改标签", end='')
        panel = device()
        res = panel.addDeviceTags(["tag_1"], rid)
        print("【结果】：", end='')
        print(res)

    def test6(self):
        print("【条件】传入rid清除标签", end='')
        panel = device()
        res = panel.cleanDeviceTags(rid)
        print("【结果】：", end='')
        print(res)


if __name__ == '__main__':
    unittest.main()
