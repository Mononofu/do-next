from abc import ABCMeta, abstractmethod


class TaskSource:
  __metaclass__ = ABCMeta

  @abstractmethod
  def tasks(self):
    """A list of all tasks that need to be done."""
    pass
