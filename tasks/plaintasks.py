 # -*- coding: utf-8 -*-
import os

import source


class PlainTasks(source.TaskSource):
  def __init__(self, todo_dir, tagname):
    self.todo_dir = todo_dir
    self.tagname = tagname

  def __iter__(self):
    return self.tasks().__iter__()

  def tasks(self):
    todos = [os.path.join(self.todo_dir, p) for p in os.listdir(self.todo_dir)]
    todos = [t for t in todos if os.path.isfile(t)]

    return [t for path in todos for t in self.parse_file(path)]

  def parse_file(self, path):
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
            tasks += self.parse_category(category, lines)
          category = line[:-1]
          lines = ''
        else:
          lines += line + '\n'
      tasks += self.parse_category(category, lines)
      return tasks

  def parse_category(self, category, lines):
    tasks = [t.strip() for t in lines.split('☐')]
    tasks = ['%s: %s' % (category, t) for t in tasks if t and '@done' not in t]
    return [t.replace(self.tagname, '').strip() for t in tasks if self.tagname in t]


if __name__ == "__main__":
  home = os.environ['HOME']
  for t in PlainTasks(os.path.join(home, 'Dropbox/wichtig/todo/'), '@remind'):
    print t
