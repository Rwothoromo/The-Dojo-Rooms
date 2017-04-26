class Person(object):
    def __init__(self, person_name):
        self.person_name = person_name

class Staff(Person):
    def __init__(self, person_name):
        pass

class Fellow(Person):
    def __init__(self, person_name):
        pass
