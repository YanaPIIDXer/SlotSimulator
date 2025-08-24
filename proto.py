import random

def make_role(name: str, value: int, denom: float):
  return {'name': name, 'value': value, 'denom': denom}

im_1_roles = [
  make_role('BIG', 252, 273),
  make_role('REG', 96, 439),
  make_role('ブドウ', 8, 6.02),
  make_role('リプレイ', 3, 7),
  make_role('チェリー', 2, 33),
]

im_6_roles = [
  make_role('BIG', 252, 255),
  make_role('REG', 96, 255),
  make_role('ブドウ', 8, 5.8),
  make_role('リプレイ', 3, 7),
  make_role('チェリー', 2, 33),
]

def pick(choices: list[int], game: int):
  i = random.randint(0, 65535)
  return choices[i]

def make_choices(roles: list[dict]):
  choices = []
  for role in roles:
    num = int(65536 / role['denom'])
    choices.extend([role['value'] for i in range(num)])
  choices += [0 for i in range(65536 - len(choices))]
  return choices

def simulate(roles: list[dict], start_game: int):
  medals = 0
  current_game = start_game
  choices = make_choices(roles)
  for i in range(8000):
    result = pick(choices, current_game)
    medals += result - 3
    current_game += 1
  return medals

def main():
  result = simulate(im_6_roles, 0)
  print(f'result: {result}')

if __name__ == '__main__':
  main()
