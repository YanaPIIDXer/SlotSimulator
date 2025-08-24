from abc import ABC, abstractmethod
import random
import math

class Machine(ABC):
  '''
  機種基底クラス
  '''

  def __init__(self):
    '''
    コンストラクタ
    '''
    self.__roles = []
    self.__choices = []
    self.__medals = 0
    self.__games = 0
    self.__total_in = 0
    self.__total_out = 0
    self.__is_end = False

  def register_role(self, name: str, value: int, rate: float):
    '''
    小役登録

    name(str): 小役名
    value(int): 払い出し枚数
    rate(float): 小役確率
    '''
    self.__roles.append({
      'name': name,
      'value': value,
      'rate': rate,
    })

  def ready(self):
    '''
    準備
    '''
    choices = []
    for role in self.__roles:
      num = int(65536 / role['rate'])
      choices.extend([role for i in range(num)])
    choices += [{'name': '', 'value': 0} for i in range(65536 - len(choices))]
    self.__choices = choices

  def reset(self):
    '''
    リセット
    '''
    self.__medals = 0
    self.__total_in = 0
    self.__total_out = 0
    self.__games = 0
    self.__is_end = False

  def reset_games(self, value: int = 0):
    '''
    現在ゲーム数のリセット

    value(int): セットするゲーム数
    '''
    self.__games = value

  def simulate_single(self, start_games: int):
    '''
    １回分のシミュレート施行

    start_games(int): 開始ゲーム数
    '''
    self.reset()
    self.reset_games(start_games)
    while not self.is_end:
      self.play()

  def end_simulate(self):
    '''
    シミュレート終了フラグを立てる
    '''
    self.__is_end = True

  def play(self):
    '''
    １回転回す
    '''
    i = random.randint(0, 65535)
    r = self.__choices[i]
    self.__medals += r['value'] - 3
    self.__games += 1
    self.__total_in += 3
    self.__total_out += r['value']
    self.after_play(r['name'])
  
  @abstractmethod
  def after_play(self, name: str):
    '''
    回した後の処理
    抽象メソッド
    
    name(str): 小役名
    '''
    pass

  def add_medal(self, value: int):
    '''
    メダルを強制追加

    value(int): 追加する値
    '''
    self.__medals += value

  @property
  def medals(self):
    '''
    差枚
    '''
    return self.__medals
  
  @property
  def games(self):
    '''
    現在の回転数
    '''
    return self.__games

  @property
  def payout(self):
    '''
    機械割
    '''
    if self.__total_in == 0: return 100.0
    return math.floor(self.__total_out / self.__total_in * 1000) / 10

  @property
  def is_end(self):
    '''
    シミュレートが終了しているか
    '''
    return self.__is_end
