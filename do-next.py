import multiprocessing.dummy
import os
import random

from tasks import wanikani, duolingo, plaintasks

home = os.environ['HOME']
todo_dir = os.path.join(home, 'Dropbox/wichtig/todo/')

# Configure your task sources here:
mandatory = [
  wanikani.WaniKani('1f00efbe4183e455b29e5ad99f45b057'),
  duolingo.Duolingo('JulianSchr'),
]
optional = [
  plaintasks.PlainTasks(todo_dir, '@remind')
]


# Do not edit below.

p = multiprocessing.dummy.Pool(max(len(mandatory), len(optional)))


def next():
  tasks = [t for ts in p.map(lambda s: s.tasks(), mandatory) for t in ts]
  if tasks:
    return tasks[0]

  tasks = [t for ts in p.map(lambda s: s.tasks(), optional) for t in ts]
  if not tasks:
    return 'You are all done!'

  return tasks[random.randint(0, len(tasks))]


if __name__ == "__main__":
  print next()
