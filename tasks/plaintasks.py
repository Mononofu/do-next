 # -*- coding: utf-8 -*-
import os


def tasks():
  home = os.environ['HOME']
  todo_dir = os.path.join(home, 'Dropbox/wichtig/todo/')
  todos = [os.path.join(todo_dir, p) for p in os.listdir(todo_dir)]
  todos = [t for t in todos if os.path.isfile(t)]

  return [t for path in todos for t in parse_file(path)]


def parse_file(path):
  with open(path) as f:
    content = f.read().replace('＿', '')
    if 'Archive:' in content:
      content = content.split('Archive:')[0]

    tasks = []
    category = None
    lines = ''
    for line in content.split('\n'):
      if not line:
        continue
      if '☐' not in line and line[-1] == ':':
        if category:
          tasks += parse_category(category, lines)
        category = line[:-1]
        lines = ''
      else:
        lines += line + '\n'
    tasks += parse_category(category, lines)
    return tasks


def parse_category(category, lines):
  tasks = [t.strip() for t in lines.split('☐')]
  tasks = ['%s: %s' % (category, t) for t in tasks if t and '@done' not in t]
  return tasks


if __name__ == "__main__":
  for t in tasks():
    print t
