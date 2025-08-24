import random

def make_role(name: str, value: int, denom: int, numer: int):
  return {'name': name, 'value': value, 'denom': denom, 'numer': numer}
im_6_roles = [
  make_role('BIG', 252, 255, 1),
  make_role('REG', 96, 255, 1),
  make_role('ブドウ', 8, 58, 10),
  make_role('リプレイ', 3, 7298, 1000),
  make_role('チェリー', 2, 3562, 1000),
]

def pick(roles: list[dict], game: int):  
  results = []
  for role in roles:
    if random.randint(1, role['denom']) <= role['numer']:
      results.append(role)
  
  if results:
    return results[0]['value']
  else:
    return 0

def simulate(start_game: int):
  medals = 0
  current_game = start_game
  for i in range(8000):
    result = pick(im_6_roles, current_game)
    medals += result - 3
    current_game += 1
  return medals

def main():
  result = simulate(0)
  print(f'result: {result}')

if __name__ == '__main__':
  main()
