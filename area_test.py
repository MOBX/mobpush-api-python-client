import unittest

from mob.area import area
from mob.device import device
from mob.push import push
from mob.stats import stats
from mob.tools import tools

appkey = "28cab3f162ef8"
rid = "5bf22f1266ffeffe19f93998"


# appSecret = "9148284e3337396201415fe78be0f05a"

class DeviceTest(unittest.TestCase):
    def test1(self):
        print("【条件】无", end='')
        panel = area()
        res = panel.getArea()
        print("【结果】：", end='')
        print(res)

    def test2(self):
        print("【条件】parentId=0", end='')
        panel = area()
        res = panel.getArea(0)
        print("【结果】：", end='')
        print(res)

    def test2(self):
        print("【条件】parentId=1", end='')
        panel = area()
        res = panel.getArea(1)
        print("【结果】：", end='')
        print(res)


if __name__ == '__main__':
    unittest.main()
