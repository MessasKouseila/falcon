from abc import ABCMeta, abstractmethod


class ObserveObstacle(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, distance):
        pass
