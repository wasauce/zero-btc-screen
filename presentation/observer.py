class Observer:
    def __init__(self, observable):
        observable.register(self)

    def update(self, data):
        pass


class Observable:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def update_observers(self, data, currency):
        for observer in self._observers:
            observer.update(data, currency)

    def close(self):
        for observer in self._observers:
            observer.close()
