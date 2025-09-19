class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu = "есть высшее образование" if self.higher_education else "нет высшего образования"
        print(f"Привет! Меня зовут {self.name}. Я родился {self.birth_date}. "
              f"Моя профессия — {self.occupation}. У меня {edu}.")

p1 = Person("Абдымиталип", "31.01.2010", "программист", True)
p2 = Person("Мой друг", "24.01.2009", "дизайнер", False)
p3 = Person("Наруто Удзумаки", "10.10.1999", "хокаге", False)

print(p1.name, p1.birth_date, p1.occupation, p1.higher_education)
print(p2.name, p2.birth_date, p2.occupation, p2.higher_education)
print(p3.name, p3.birth_date, p3.occupation, p3.higher_education)

# Вызываем метод introduce
p1.introduce()
p2.introduce()
p3.introduce()