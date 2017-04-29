class Person(object):
    """
    This class is used for creation of people.
    It is the super class for Staff and Fellow classes
    """
    def __init__(self, name):
        self.name = name

# Staff inherits from Person class
class Staff(Person):
    def __init__(self, name):
        self.type = "STAFF"
        super(Staff, self).__init__(name)

# Fellow inherits from Person class
class Fellow(Person):
    def __init__(self, name):
        self.type = "FELLOW"
        super(Fellow, self).__init__(name)
