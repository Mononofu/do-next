import multiprocessing.dummy
import os

from tasks import wanikani, duolingo, plaintasks

home = os.environ['HOME']
todo_dir = os.path.join(home, 'Dropbox/wichtig/todo/')

sources = [wanikani.WaniKani('1f00efbe4183e455b29e5ad99f45b057'),
           duolingo.Duolingo('JulianSchr'),
           plaintasks.PlainTasks(todo_dir, '@remind')]

p = multiprocessing.dummy.Pool(len(sources))

tasks = [t for ts in p.map(lambda s: s.tasks(), sources) for t in ts]

if tasks:
  print tasks[0]
else:
  print 'You are all done!'
