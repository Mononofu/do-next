import requests

url = 'https://www.duolingo.com/users/JulianSchr'


def tasks():
  r = requests.get(url).json()

  if r['streak_extended_today']:
    return []
  else:
    return ['Extend Duoling Streak']


if __name__ == "__main__":
  print tasks()
