import multiprocessing.dummy

from tasks import wanikani, duolingo

sources = [wanikani, duolingo]
p = multiprocessing.dummy.Pool(5)

tasks = [t for ts in p.map(lambda s: s.tasks(), sources) for t in ts]

if tasks:
  print tasks[0]
else:
  print 'You are all done!'
