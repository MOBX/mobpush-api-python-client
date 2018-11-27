import unittest

from mob.device import device
from mob.push import push
from mob.stats import stats
from mob.tools import tools

appkey = "28cab3f162ef8"
rid = "5bf22f1266ffeffe19f93998"


# appSecret = "9148284e3337396201415fe78be0f05a"

class DeviceTest(unittest.TestCase):
    def test1(self):
        print("【条件】传入正确batchId统计", end='')
        panel = stats()
        batchId = "5bfcf48666ffeffe1a03a04c"
        res = panel.getStatsByBatchId(batchId)
        print("【结果】：", end='')
        print(res)

    def test2(self):
        print("【条件】传入正确workno统计", end='')
        panel = stats()
        workno = "230714933537218560"
        res = panel.getStatsByWorkno(workno)
        print("【结果】：", end='')
        print(res)


if __name__ == '__main__':
    unittest.main()
