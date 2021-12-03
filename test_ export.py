from TestInterface import Interface
from Common import GBK2312, Now, TimeNow, Unicode, loginEZ, loginOther
import random
inter = Interface()
Random = TimeNow()

#1.导出勾选订单[参数正则提交]
def test_export():
    test_export = inter.export(
        value = str(["SO-RYA-2021-0119"]),
        headers = {'Authorization': loginEZ()}
    )
    print("="*100)
    print("#1.导出勾选订单[参数正则提交]",test_export,test_export.json())
    print("="*100)
# # test_export()
#     # assert str(test_export.status_code) == "200"