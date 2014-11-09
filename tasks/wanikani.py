import requests

import source


class WaniKani(source.TaskSource):
  def __init__(self, api_key):
    self.api = 'https://www.wanikani.com/api/user/%s/%%s' % api_key

  def tasks(self):
    tasks = []
    r = requests.get(self.api % 'study-queue').json()['requested_information']

    if r['reviews_available'] > 0:
      tasks.append('%d WaniKani reviews' % r['reviews_available'])

    if r['lessons_available'] > 0:
      tasks.append('%d WaniKani lessons' % r['lessons_available'])

    return tasks


if __name__ == "__main__":
  print WaniKani('1f00efbe4183e455b29e5ad99f45b057').tasks()
