import abc


class Sensor(abc.ABC):

    @abc.abstractmethod
    def generate(self):
        pass
