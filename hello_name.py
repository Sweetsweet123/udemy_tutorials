from random import choice


class Person():
    def __init__(self, name):
        self.greeting = '<div>Hello {}</div>'
        self.name = name

    def __str__(self):
        return self.make_greeting()

    def make_greeting(self):
        return self.greeting.format(self.name)


def main():
    people = [
        Person('Jane'),
        Person('Tom')
    ]
    person = choice(people)
    print(person)


if __name__ == '__main__':
    main()