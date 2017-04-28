class Person(object):
    """
    This class is used for creation of people.
    It is the super class for Staff and Fellow classes
    """
    def __init__(self, person_name):
        self.person_name = person_name

# Office inherits from Room class
class Staff(Person):
    pass

# Office inherits from Room class
class Fellow(Person):
    pass
