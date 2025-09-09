class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, "
              f"работаю {self.occupation}. Высшее образование: {self.higher_education}")


class Classmate(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассник Абдымиталип, "
              f"я родился {self.birth_date}, работаю {self.occupation}")


class Friend(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я друг Абдымиталип, "
              f"я родился {self.birth_date}, работаю {self.occupation}")

classmate1 = Classmate(name="Элмырза", birth_date="24.01.2009", occupation="Программист", higher_education=True)
classmate2 = Classmate(name="Айтолкун", birth_date="38.01.2010", occupation="Студент", higher_education=False)

friend1 = Friend(name="Алмаз", birth_date="5.12.2008", occupation="Программист", higher_education=True)
friend2 = Friend(name="Жанара", birth_date="20.08.2008", occupation="Дизайнер", higher_education=True)

# Вызов метода introduce у каждого
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()