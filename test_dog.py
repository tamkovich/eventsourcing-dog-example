from aggregations import Dog


def test():

    # Give a dog a name, and some tricks.
    fido = Dog(name='Fido')
    fido.add_trick('fetch ball')
    fido.add_trick('roll over')
    fido.add_trick('play dead')

    # Check the state of the aggregate.
    assert fido.name == 'Fido'
    assert fido.tricks == [
        'fetch ball',
        'roll over',
        'play dead',
    ]

    # Check the aggregate events.
    events = fido.collect_events()
    assert len(events) == 4
    assert isinstance(events[0], Dog.Named)
    assert events[0].name == 'Fido'
    assert isinstance(events[1], Dog.TrickAdded)
    assert events[1].trick == 'fetch ball'
    assert isinstance(events[2], Dog.TrickAdded)
    assert events[2].trick == 'roll over'
    assert isinstance(events[3], Dog.TrickAdded)
    assert events[3].trick == 'play dead'

    # Reconstruct aggregate from events.
    copy = None
    for e in events:
        copy = e.mutate(copy)
    assert copy == fido

    # Create and test another aggregate.
    buddy = Dog(name='Buddy')
    assert fido != buddy
    events = buddy.collect_events()
    assert len(events) == 1
    assert isinstance(events[0], Dog.Named)
    assert events[0].name == 'Buddy'
    assert events[0].mutate(None) == buddy


if __name__ == '__main__':
    test()
