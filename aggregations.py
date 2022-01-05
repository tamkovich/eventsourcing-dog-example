from eventsourcing.domain import Aggregate, event


class Dog(Aggregate):
    @event('Named')
    def __init__(self, name):
        self.name = name
        self.tricks = []

    @event('TrickAdded')
    def add_trick(self, trick):
        self.tricks.append(trick)
