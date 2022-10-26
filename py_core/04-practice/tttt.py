import pandas as pd
import os


def assert_msg(condition, msg):
    if not condition:
        raise Exception(msg)


def read_csv_file(filename):
    # 获取文件绝对路径
    filepath = os.path.join(os.path.dirname(__file__), filename)
    # 判断文件是否存在
    assert_msg(os.path.exists(filepath), "file noe found")
    # 读取csv文件并返回
    return pd.read_csv(filepath, index_col=0, parse_dates=True, infer_datetime_format=True)


BTCUSD = read_csv_file("BTCUSD_GEMINI.csv")
assert_msg(BTCUSD.__len__() > 0, "read failed")
print(BTCUSD.head())
