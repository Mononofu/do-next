import requests

import source


class Duolingo(source.TaskSource):
  def __init__(self, user):
    self.url = 'https://www.duolingo.com/users/%s' % user

  def tasks(self):
    r = requests.get(self.url).json()

    if r['streak_extended_today']:
      return []
    else:
      return ['Extend Duoling Streak']


if __name__ == "__main__":
  print Duolingo('JulianSchr').tasks()
