import multiprocessing.dummy

from tasks import wanikani, duolingo, plaintasks

sources = [wanikani, duolingo, plaintasks]
p = multiprocessing.dummy.Pool(len(sources))

tasks = [t for ts in p.map(lambda s: s.tasks(), sources) for t in ts]

if tasks:
  print tasks[0]
else:
  print 'You are all done!'
