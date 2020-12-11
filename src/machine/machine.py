import random

# 小役
class Role(object):
    # コンストラクタ
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    # データをTupleで取得
    def get(self):
        return (self.__name, self.__value)

# スロット基底クラス
class Machine(object):
    # コンストラクタ
    def __init__(self, setting_value):
        self.__table = [None] * 65536
        self.__setting_value = setting_value
        configure_table()

    # デーブル構築
    def configure_table(self):
        raise NotImplementedError()

    # 役をテーブルに追加
    def add_to_table(self, role, rate):
        count = int(65536 / rate)
        begin = 0
        while self.__table[begin] != None:
            begin = begin + 1
            if begin > 65536: raise Error("OVerflow")
        for i = 0; i < count; i = i + 1:
            if begin + i > 65536: raise Error("Overflow")
            self.__table[begin + i] = role

    # シミュレート
    def simulate(self):
        index = random.randrange(65535)
        role = self.__table[index]
        if role == None: role = ("ハズレ", 0)
        return role

    # 設定値取得
    def setting_value():
        return self.__setting_value
