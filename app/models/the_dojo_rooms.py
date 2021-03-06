#-*- coding: utf-8-*-
"""
This module contains the classes used for creating a person in the Dojo.
"""
import random
import os.path
from app.models.persons import Fellow, Staff
from app.models.rooms import Office, LivingSpace
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from app.database.dojo_declarative_sqlalchemy import Base, engine
from app.database.dojo_declarative_sqlalchemy import DbFellows, DbStaff, DbOffices, DbLivingSpaces


class Dojo(object):
    """
    This class is used for running functions on the Dojo.
    """

    def __init__(self):
        self.all_rooms = {}
        self.allocated_rooms = []
        self.all_persons = {}
        self.allocated_persons = []

    def create_room(self, room_type, room_name):
        """Creates rooms in the Dojo."""

        initial_room_count = len(self.all_rooms)
        room_increment = 0

        if not isinstance(room_type, str):
            raise AttributeError("Room type must be a string")

        if not isinstance(room_name, list):
            raise AttributeError("Room name must be a list")

        if room_type.lower() != 'office' and room_type.lower() != 'livingspace':
            raise ValueError("Please set a room type as office or livingspace")

        if room_type.lower() == 'office':
            for room in room_name:
                room = room.lower().capitalize()
                if room in self.all_rooms.keys():
                    print("{} room already exists".format(room))
                else:
                    office = Office(room)

                    # append room objects to room dictionary
                    self.all_rooms[room] = office
                    print("An {} called {} has been successfully created!" \
                            .format(room_type.lower(), room))

                    #auto-allocate offices to persons pending allocation
                    allocated = self.auto_allocate_office()

        if room_type.lower() == 'livingspace':
            for room in room_name:
                room = room.lower().capitalize()
                if room in self.all_rooms.keys():
                    print("{} room already exists".format(room))
                else:
                    livingspace = LivingSpace(room)

                    # append room objects to room dictionary
                    self.all_rooms[room] = livingspace
                    print("A {} called {} has been successfully created!" \
                            .format(room_type.lower(), room))

                    #auto-allocate livingspaces to fellows pending allocation and in need thereof
                    allocated = self.auto_allocate_livingspace()

        new_room_count = len(self.all_rooms)
        room_increment = new_room_count - initial_room_count
        return (room_increment, allocated)

    def add_person(self, person_name, person_type, wants_accommodation=None):
        """Adds a person to the Dojo and assigns them a random room."""

        initial_person_count = len(self.all_persons)
        person_increment = 0

        if not isinstance(person_name, str):
            raise AttributeError("Person name must be a string")

        if not isinstance(person_type, str):
            raise AttributeError("Person type must be a string")

        if person_type.upper() == 'STAFF':
            person_name = ' '.join([name.capitalize() for name in person_name.lower().split()])
            if person_name in self.all_persons.keys():
                raise ValueError("{} already exists".format(person_name))

            if not wants_accommodation:
                staff = Staff(person_name)

                # append person object to all_persons dictionary
                self.all_persons[person_name] = staff
                print("{} {} has been successfully added.".format(staff.type, staff.name))
                self.allocate_office(staff)
            else:
                raise AttributeError("Staff cannot seek accomodation")

        if person_type.upper() == 'FELLOW':
            person_name = ' '.join([name.capitalize() for name in person_name.lower().split()])
            if person_name in self.all_persons.keys():
                raise ValueError("{} already exists".format(person_name))

            if not wants_accommodation:
                raise ValueError("Fellow must indicate 'Y' or 'N' for accomodation")

            if not isinstance(wants_accommodation, str):
                raise AttributeError("Fellow must indicate 'Y' or 'N' for accomodation")

            if wants_accommodation.upper() != 'Y' and wants_accommodation.upper() != 'N':
                raise ValueError("Fellow must indicate 'Y' or 'N' for accomodation")

            if wants_accommodation.upper() == 'N':
                person_name = ' '.join([name.capitalize() for name in person_name.lower().split()])
                fellow = Fellow(person_name, wants_accomodation=False)

                # append person object to all_persons dictionary
                self.all_persons[person_name] = fellow
                print("{} {} has been successfully added.".format(fellow.type, fellow.name))
                self.allocate_office(fellow)

            if wants_accommodation.upper() == 'Y':
                person_name = ' '.join([name.capitalize() for name in person_name.lower().split()])
                fellow = Fellow(person_name, wants_accomodation=True)

                # append person object to all_persons dictionary
                self.all_persons[person_name] = fellow
                print("{} {} has been successfully added.".format(fellow.type, fellow.name))
                self.allocate_office(fellow)
                self.allocate_livingspace(fellow)

        new_person_count = len(self.all_persons)
        person_increment = new_person_count - initial_person_count
        return person_increment

    def allocate_office(self, person):
        """Assign an office to a person."""

        first_name = person.name.split(' ')[0]
        offices_available = [room for room in self.all_rooms.values() \
                            if isinstance(room, Office) and room.check_room_availability()]

        if not offices_available:
            print("No Office space available")
        else:
            # select a random room object
            random_office = random.choice(offices_available)

            # assign a person a Dojo room
            random_office.add_occupant(person)

            # append person name to list of persons allocated rooms
            if person.name not in self.allocated_persons:
                self.allocated_persons.append(person.name)

            # append office name to dictionary of rooms
            self.all_rooms[random_office.name] = random_office

            # append person name to dictionary of persons in the Dojo
            self.all_persons[person.name] = person
            print("{} has been allocated the office {}.".format(first_name, random_office.name))
            return random_office

    def allocate_livingspace(self, person):
        """Assign a LivingSpace to a person."""

        first_name = person.name.split(' ')[0]
        livingspaces_available = [room for room in self.all_rooms.values() \
                                if isinstance(room, LivingSpace) and room.check_room_availability()]

        if not livingspaces_available:
            print("No Living space available")
        else:
            # select a random room object
            random_livingspace = random.choice(livingspaces_available)

            # assign a person a Dojo room
            random_livingspace.add_occupant(person)

            # append person name to list of persons allocated rooms
            if person.name not in self.allocated_persons:
                self.allocated_persons.append(person.name)

            # append room name to dictionary of rooms in the Dojo
            self.all_rooms[random_livingspace.name] = random_livingspace

            # append person name to dictionary of persons in the Dojo
            self.all_persons[person.name] = person
            print("{} has been allocated the livingspace {}." \
                    .format(first_name, random_livingspace.name))
            return random_livingspace

    def print_room(self, room_name):
        """Prints the names of all the people in a specified room, onto the screen."""

        if not isinstance(room_name, str):
            raise AttributeError("Room name must be a string.")

        room_name = room_name.lower().capitalize()
        if room_name not in self.all_rooms.keys():
            print("{} does not exist in rooms!".format(room_name))

        # retrieve list or person objects from all Dojo rooms
        room_occupants = self.all_rooms[room_name].occupants
        for individual in room_occupants:
            print('{}\n'.format(individual.name))
        return room_occupants

    def print_allocations(self, filename=None):
        """Prints a list of allocations onto the screen."""

        self.allocated_rooms = [room for room in self.all_rooms.values() if room.occupants]
        if not self.allocated_rooms:
            print("No Rooms allocated!")

        if filename and not isinstance(filename, str):
            raise AttributeError("Filename must be a string")

        write_to_file = False
        used_file = None
        if isinstance(filename, str):
            if len(filename) > 4 and filename.endswith('.txt'):
                write_to_file = True
                ouput_file = open(filename, 'w')

        # search the rooms with occupants, for room names and occupant names
        for room in self.allocated_rooms:
            print('{}\n{}'.format(room.name.upper(), '-'*30))
            if write_to_file:
                ouput_file.write('{}\n{}'.format(room.name.upper(), '-'*30))

            # search for occupant names in list of room occupant(person) objects
            for room_occupant in room.occupants:
                print("\nMEMBER {},".format(room_occupant.name))
                if write_to_file:
                    ouput_file.write("\nMEMBER {},".format(room_occupant.name))
            print('\n\n')
            if write_to_file:
                ouput_file.write('\n\n')
        if write_to_file:
            ouput_file.close()
            used_file = os.path.isfile(filename)

        return (self.allocated_rooms, used_file)

    def print_unallocated(self, filename=None):
        """Prints a list of unallocated people to the screen."""

        # retrieve list of person objects that are not assigned rooms in the Dojo
        unallocated_persons = [person for person in self.all_persons.keys() \
                                if person not in self.allocated_persons]
        if not unallocated_persons:
            print("No Person is unallocated!")

        if filename and not isinstance(filename, str):
            raise AttributeError("Filename must be a string")

        write_to_file = False
        used_file = None
        if isinstance(filename, str):
            if len(filename) > 4 and filename.endswith('.txt'):
                write_to_file = True
                ouput_file = open(filename, 'w')

        # retrieve names of persons without rooms
        for individual in unallocated_persons:
            print("\nMEMBER {},".format(individual))
            if write_to_file:
                ouput_file.write("\nMEMBER {},".format(individual))
        if write_to_file:
            ouput_file.close()
            used_file = os.path.isfile(filename)

        return (unallocated_persons, used_file)

    def auto_allocate_office(self):
        """Auto-allocate offices to non-allocated persons."""

        office_occupants = []
        offices = []

        for room_name in self.allocated_rooms:
            if isinstance(self.all_rooms[room_name], Office):
                offices.append(room_name)

        offices += [room for room in self.all_rooms.values() if isinstance(room, Office)]

        for office in offices:
            office_occupants += office.occupants

        initial_occupant_count = len(office_occupants)
        for person in self.all_persons.values():
            if person not in office_occupants:
                self.allocate_office(person)
                office_occupants.append(person)

        return len(office_occupants) - initial_occupant_count

    def auto_allocate_livingspace(self):
        """Auto-allocate livingspaces to non-allocated fellows."""

        livingspace_occupants = []
        livingspaces = []

        for room_name in self.allocated_rooms:
            if isinstance(self.all_rooms[room_name], LivingSpace):
                livingspaces.append(room_name)

        livingspaces += [room for room in self.all_rooms.values() if isinstance(room, LivingSpace)]

        for livingspace in livingspaces:
            livingspace_occupants += livingspace.occupants

        initial_occupant_count = len(livingspace_occupants)
        for person in self.all_persons.values():
            if person not in livingspace_occupants and person.type == "FELLOW" \
                and person.wants_accomodation:
                self.allocate_livingspace(person)
                livingspace_occupants.append(person)
        return len(livingspace_occupants) - initial_occupant_count

    def reallocate_person(self, person_name, room_name):
        """Relocate relocate a person from one room to another."""

        if not isinstance(person_name, str):
            raise AttributeError("Person name must be a string")

        if not isinstance(room_name, str):
            raise AttributeError("Room name must be a string")

        person_name = ' '.join([name.capitalize() for name in person_name.lower().split()])
        if person_name not in self.all_persons.keys():
            raise ValueError("{} does not exist!".format(person_name))

        room_name = room_name.lower().capitalize()

        if self.all_rooms[room_name]:
            room = self.all_rooms[room_name]
            person = self.all_persons[person_name]
            person_rooms = self.return_person_rooms(person)
            person_office = None
            person_livingspace = None
            old_room = None
            new_room = None

            if not room.check_room_availability:
                raise ValueError("{} room is full!".format(room_name))

            if room in person_rooms:
                raise ValueError("{} is already in {} room!".format(person_name, room_name))

            for room_object in person_rooms:
                if isinstance(room_object, Office):
                    person_office = room_object
                if isinstance(room_object, LivingSpace):
                    person_livingspace = room_object

            if isinstance(room, Office) and person_office:
                person_office.occupants.remove(person)
                room.occupants.append(person)
                print("{} has been re-located from office {} to office {}."\
                        .format(person.name, person_office.name, room_name))
                return (person_office.name, room_name)

            if isinstance(room, LivingSpace) and isinstance(person, Fellow) \
                            and person_livingspace:
                person_livingspace.occupants.remove(person)
                room.occupants.append(person)
                print("{} has been re-located from office {} to office {}."\
                        .format(person.name, person_livingspace.name, room_name))
                return (person_livingspace.name, room_name)

        return(old_room, new_room)

    def return_person_rooms(self, person):
        """Return a list of room objects in which person is an occupant."""
        person_rooms = []
        for room in self.all_rooms.values():
            for room_occupant in room.occupants:
                if room_occupant.name == person.name:
                    person_rooms.append(room)
        return person_rooms

    def load_people(self, filename):
        """Retrieves people from a text file and allocates them to rooms."""

        if not filename:
            raise AttributeError("Provide source file!")

        if filename and not isinstance(filename, str):
            raise AttributeError("Filename must be a string!")

        used_file = None
        person_increment = 0
        if isinstance(filename, str):
            input_file = open(filename, 'r')
            contents = input_file.read()
            contents_list = contents.split('\n')
            if input_file:
                used_file = filename

            for person in contents_list:
                person = person.split(' ')
                if len(person) > 2:
                    person_name = person[0].lower().capitalize() + ' ' \
                                        + person[1].lower().capitalize()
                    person_type = person[2].upper()

                    if len(person) == 3:
                        person_increment += self.add_person(person_name, person_type)

                    if len(person) == 4:
                        wants_accommodation = person[3].upper()
                        person_increment += self.add_person(person_name, person_type, \
                                                                    wants_accommodation)
            input_file.close()

        return (person_increment, used_file)

    def save_state(self, db_name='dojo_rooms.db'):
        """Persists all the data stored in the app to a SQLite database."""

        # engine = create_engine('sqlite:///%s' % db_name, echo=False) #disable logging with False

        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Create database objects
        for room in self.all_rooms.values():
            if isinstance(room, Office):
                db_office = DbOffices(room.name)
                office_query = session.query(DbOffices).filter_by(name=room.name).first()
                if not office_query:
                    session.add(db_office)

            if isinstance(room, LivingSpace):
                db_livingspace = DbLivingSpaces(room.name)
                livingspace_query = session.query(DbLivingSpaces).filter_by( \
                                                                        name=room.name).first()
                if not livingspace_query:
                    session.add(db_livingspace)

        for person in self.all_persons.values():
            person_rooms = self.return_person_rooms(person)

            for room_object in person_rooms:
                if isinstance(room_object, Office):
                    person_office = room_object.name
                if isinstance(room_object, LivingSpace):
                    person_livingspace = room_object.name

            if isinstance(person, Staff):
                # retrieve the office id for the matching office name in the database
                office_query = session.query(DbOffices).filter_by(name=person_office).first()
                office_id = office_query.id

                staff_query = session.query(DbStaff).filter_by(name=person.name).first()
                if not staff_query:
                    db_staff = DbStaff(person.name, office_id)
                    session.add(db_staff)

            if isinstance(person, Fellow):
                # retrieve the office and livingspace ids for the matching
                # office and livingspace names in the database
                office_query = session.query(DbOffices).filter_by(name=person_office).first()
                livingspace_query = session.query(DbLivingSpaces).filter_by( \
                                                            name=person_livingspace).first()

                office_id = office_query.id
                livingspace_id = livingspace_query.id

                wants_accomodation = 'N'
                if person.wants_accomodation:
                    wants_accomodation = 'Y'

                fellow_query = session.query(DbFellows).filter_by(name=person.name).first()
                if not fellow_query:
                    db_fellow = DbFellows(person.name, office_id, livingspace_id, \
                                                                        wants_accomodation)
                    session.add(db_fellow)

        # commit the data to the database
        session.commit()
        print("Data saved to database.")
        # You can view database content from http://sqliteviewer.flowsoft7.com/
        return db_name

    def load_state(self, db_name='dojo_rooms.db'):
        """Loads data from a database into the application."""

        # You can view database content from http://sqliteviewer.flowsoft7.com/

        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Create objects
        for room in session.query(DbOffices).order_by(DbOffices.id):
            office = Office(room.name)

            # append room objects to room dictionary
            self.all_rooms[room.name] = office

        for room in session.query(DbLivingSpaces).order_by(DbLivingSpaces.id):
            livingspace = LivingSpace(room.name)

            # append room objects to room dictionary
            self.all_rooms[room.name] = livingspace

        for person in session.query(DbStaff).order_by(DbStaff.id):
            staff = Staff(person.name)

            # append person object to all_persons dictionary
            self.all_persons[person.name] = staff

            # assign the staff an office
            office_query = session.query(DbOffices).filter_by(id=person.office).first()
            if office_query:
                office = self.all_rooms[office_query.name]
                office.add_occupant(staff)

        for person in session.query(DbFellows).order_by(DbFellows.id):
            if person.wants_accommodation == 'Y':
                wants_accomodation = True
            if person.wants_accommodation == 'N':
                wants_accomodation = False

            fellow = Fellow(person.name, wants_accomodation)

             # append person object to all_persons dictionary
            self.all_persons[person.name] = fellow

            # assign the fellow an office
            office_query = session.query(DbOffices).filter_by(id=person.office).first()
            if office_query:
                office = self.all_rooms[office_query.name]
                office.add_occupant(fellow)

            # assign the fellow a living space
            livingspace_query = session.query(DbLivingSpaces).filter_by( \
                                                            id=person.livingspace).first()
            if livingspace_query:
                livingspace = self.all_rooms[livingspace_query.name]
                livingspace.add_occupant(fellow)

        print("Data loaded from database.")
        return db_name
