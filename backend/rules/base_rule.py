#-*- coding: utf-8 -*-

from abc import ABCMeta

class BaseRule:
  __metaclass__ = ABCMeta

  @abstractmethod
  def check():
    pass
