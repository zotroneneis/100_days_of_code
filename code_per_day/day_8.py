"""
File: day_8.py
Author: Anna-Lena Popkes
Email: popkes@gmx.net
Github: https://github.com/zotroneneis
Description: all code for day 8 of my new coding habit
Link to blog post with explanations: http://www.alpopkes.com/posts/2018/07/coding-challenge-day-8/
"""
import datetime
from abc import ABC, abstractmethod

class CastleKilmereMember:
    """ Creates a member of the Castle Kilmere School of Magic """
    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words: str) -> str:
        return f"{self.name} says {words}"

    @property
    def age(self) -> int:
        now = datetime.datetime.now().year
        return now - self.birthyear

    @classmethod
    def school_headmistress(cls) -> 'CastleKilmereMember':
        return cls('Miranda Mirren', 1963, 'female')

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}')")


class Professor(CastleKilmereMember):
    """ Creates a Castle Kilmere professor """
    def __init__(self, name: str, birthyear: int, sex: str, subject: str, department: str = None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.department = department

    @classmethod
    def blade(cls) -> 'Professor':
        return cls('Blade Bardock', 1988, 'male', 'Potions', 'Science')

    @classmethod
    def briddle(cls) -> 'Professor':
        return cls('Birdie Briddle', 1931, 'female', 'Foreign Magical Systems', 'Law')


    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}', "
                f"subject='{self.subject}', department='{self.department}')")


class Ghost(CastleKilmereMember):
    """ Creates a Castle Kilmere ghost """
    def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}', "
                f"year_of_death={self.year_of_death})")

    @classmethod
    def mocking_knight(cls):
        return cls('The Mocking Knight', 1401, 'male', 1492)


class Pupil(CastleKilmereMember):
    """ Create a Castle Kilmere Pupil """
    def __init__(self, name: str, birthyear: int, sex: str, start_year: int, pet: tuple = None):
        super().__init__(name, birthyear, sex)
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
                  'Critical Thinking': False,
                  'Self-Defense Against Fresh Fruit': False,
                  'Broomstick Flying': False,
                  'Magical Theory': False,
                  'Foreign Magical Systems': False,
                  'Charms': False,
                  'Defence Against Dark Magic': False,
                  'History of Magic': False,
                  'Potions': False,
                  'Transfiguration': False}

        self._friends = []

    @classmethod
    def luke(cls) -> 'Pupil':
        return cls('Luke Bery', 2008, 'male', 2018, ('Cotton', 'owl'))

    @classmethod
    def lissy(cls) -> 'Pupil':
        return cls('Lissy Spinster', 2008, 'female', 2018, ('Ramses', 'cat'))

    @classmethod
    def adrien(cls) -> 'Pupil':
        return cls('Adrien Fulford', 2008, 'male', 2018, ('Unnamed', 'owl') )

    @property
    def current_year(self) -> int:
        now = datetime.datetime.now().year
        return now - self.start_year

    @property
    def elms(self):
        return self._elms

    @property
    def friends(self):
        return f"{self.name}'s current friends are: {[person.name for person in self._friends]}"

    @elms.setter
    def elms(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass and iterable with two items: subject and grade")

        passed = self.passed(grade)

        if passed:
            self._elms[subject] = True
        else:
            print('The exam was not passed so no ELM was awarded!')

    @elms.deleter
    def elms(self):
        print("Caution, you are deleting this students' ELM's! "
              "You should only do that if she/he dropped out of school without passing any exam!")
        del self._elms


    @staticmethod
    def passed(grade):
        """
        Given a grade, determine if an exam was passed.
        """
        grades = {
                'E': True,
                'Excellent': True,
                'G': True,
                'Good': True,
                'A': True,
                'Acceptable': True,
                'P': False,
                'Poor': False,
                'H': False,
                'Horrible': False,
                }

        return grades.get(grade, False)

    def befriend(self, person):
        """Adds another person to your list of friends"""
        self._friends.append(person)
        print(f"{person.name} is now your friend!")

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"birthyear={self.birthyear}, sex='{self.sex}', "
                f"start_year={self.start_year})")

class Spell(ABC):
    def __init__(self, name: str, incantation: str, effect: str):
        self.name = name
        self.incantation = incantation
        self.effect = effect

    @abstractmethod
    def cast(self):
        pass

    @property
    @abstractmethod
    def defining_feature(self):
        pass


class Charm(Spell):
    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = "Simple", min_year: int = 1):
        super().__init__(name, incantation, effect)
        self.difficulty = difficulty
        self.min_year = min_year

    @property
    def defining_feature(self) -> str:
        return ("Alteration of the object's inherent qualities, that is, its behaviour and capabilities")

    def cast(self):
        print(f"{self.incantation}!")

    @classmethod
    def stuporus_ratiato(cls):
        return cls('The Stuporus Ratiato spell', 'Stuporus Ratiato', 'Makes objects fly')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.incantation}, {self.difficulty}, {self.effect})"

if __name__ == "__main__":
    bromley = CastleKilmereMember(name='Bromley Huckabee', birthyear=1959, sex='male')
    lissy = Pupil(name='Lissy Spinster', birthyear=2008, sex='female', start_year=2018)
    luke = Pupil.luke()
    adrien = Pupil.adrien()

    lissy.befriend(bromley)
    lissy.befriend(luke)
    lissy.befriend(adrien)
    print(lissy.friends)
    print()

    stuporus = Charm.stuporus_ratiato()
    stuporus.cast()






