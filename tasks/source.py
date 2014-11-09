from abc import ABCMeta, abstractmethod


class TaskSource:
  __metaclass__ = ABCMeta

  @abstractmethod
  def tasks(self):
    pass
