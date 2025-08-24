from simulator import Machine

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

def main():
  machine = Im6()
  games = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
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
