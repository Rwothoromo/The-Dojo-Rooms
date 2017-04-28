class Person(object):
    def __init__(self, person_name):
        self.person_name = person_name

class Staff(Person):
    def __init__(self, person_name):
        self.person_name = person_name
        super(Staff, self).__init__(person_name)

class Fellow(Person):
    def __init__(self, person_name):
        self.person_name = person_name
        super(Fellow, self).__init__(person_name)
