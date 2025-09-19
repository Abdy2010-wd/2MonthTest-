class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    # property для occupation
    @property
    def occupation(self):
        return self.__occupation

    @occupation.setter
    def occupation(self, value):
        self.__occupation = value

    # property для higher_education
    @property
    def higher_education(self):
        return self.__higher_education

    @higher_education.setter
    def higher_education(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("higher_education должно быть True или False")
        self.__higher_education = value

    def introduce(self):
        edu_text = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. {edu_text}")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        edu_text = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Я учился с Абдымиталип в группе {self.group}. {edu_text}")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        edu_text = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Мое хобби {self.hobby}. {edu_text}")


# Примеры
classmate1 = Classmate(name="Элмырза", birth_date="24.01.2009", occupation="Программист", higher_education=True, group="11D")
classmate2 = Classmate(name="Айтолкун", birth_date="18.01.2010", occupation="Студент", higher_education=False, group="11D")

friend1 = Friend(name="Алмаз", birth_date="5.12.2008", occupation="Программист", higher_education=True, hobby="футбол")
friend2 = Friend(name="Жанара", birth_date="20.08.2008", occupation="Дизайнер", higher_education=True, hobby="рисование")

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()