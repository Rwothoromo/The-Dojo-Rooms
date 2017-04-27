from abc import ABCMeta

class Person(object):
    __metaclass__ = ABCMeta
    person_type = ''

    def __init__(self, person_name):
        self.person_name = person_name

class Staff(Person):
    person_type = 'STAFF'

class Fellow(Person):
    person_type = 'FELLOW'
