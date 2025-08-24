from simulator import Machine
import random

class Im6(Machine):
  '''
  天井付きアイム設定６
  '''
  
  def __init__(self):
    super().__init__()
    self.register_role('BIG', 252, 255),
    self.register_role('REG', 96, 255),
    self.register_role('ブドウ', 8, 5.8),
    self.register_role('リプレイ', 3, 7),
    self.register_role('チェリー', 2, 33),
    self.ready()

  def after_play(self, name: str):
    # 天井
    if self.games == 499:
      self.add_medal(10000)
      self.end_simulate()
    if name in ['BIG', 'REG']:
      self.end_simulate()

class HogeSample(Machine):
  '''
  適当なサンプル
  '''

  def __init__(self):
    super().__init__()
    self.register_role('ベル', 10, 7),
    self.register_role('押し順ベル', 0, 2),
    self.register_role('リプレイ', 3, 7),
    self.register_role('チェリー', 2, 80),
    self.ready()
    self.__at_games = -1

  def on_reset(self):
    self.__at_games = -1

  def after_play(self, name: str):
    if self.__at_games == -1:
      # 天井
      if self.games == 800:
        self.__begin_at()
      elif self.games == 200 and random.randint(0, 99) < 50:
        self.__begin_at()
      elif self.games == 400 and random.randint(0, 99) < 25:
        self.__begin_at()
    else:
      if name == '押し順ベル':
        self.add_medal(15)
      self.__at_games -= 1
      if self.__at_games == 0:
        self.end_simulate()

  def __begin_at(self):
    '''
    AT開始
    '''
    self.__at_games = 50


def main():
  machine = HogeSample()
  games = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
  for start in games:
    num = 1000
    total = 0
    total_payout = 0
    for i in range(num):
      machine.simulate_single(start)
      total += machine.medals
      total_payout += machine.payout
    print(f'start: {start}', f'result: {total / num}', f'payout: {total_payout / num}')
  
if __name__ == '__main__':
  main()
