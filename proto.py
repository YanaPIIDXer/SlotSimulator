import random

def make_role(name: str, value: int, denom: float, reset: bool):
  return {'name': name, 'value': value, 'denom': denom, 'reset': reset}

im_1_roles = [
  make_role('BIG', 252, 273, True),
  make_role('REG', 96, 439, True),
  make_role('ブドウ', 8, 6.02, False),
  make_role('リプレイ', 3, 7, False),
  make_role('チェリー', 2, 33, False),
]

im_6_roles = [
  make_role('BIG', 252, 255, True),
  make_role('REG', 96, 255, True),
  make_role('ブドウ', 8, 5.8, False),
  make_role('リプレイ', 3, 7, False),
  make_role('チェリー', 2, 33, False),
]

def pick(choices: list[int], game: int):
  if game == 500:
    return {'value': 1000, 'reset': True}
  
  i = random.randint(0, 65535)
  return choices[i]

def make_choices(roles: list[dict]):
  choices = []
  for role in roles:
    num = int(65536 / role['denom'])
    choices.extend([role for i in range(num)])
  choices += [{'value': 0, 'reset': False} for i in range(65536 - len(choices))]
  return choices

def single_simulate(roles: list[dict], start_game: int):
  medals = 0
  current_game = start_game
  choices = make_choices(roles)
  for i in range(8000):
    result = pick(choices, current_game)
    medals += result['value'] - 3
    current_game += 1
    if result['reset']:
      return medals
  return medals

def main():
  result = single_simulate(im_6_roles, 0)
  print(f'result: {result}')

if __name__ == '__main__':
  main()
