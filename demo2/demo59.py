from Blutbox import BlutBox
from Gun import Gun
from Person import Person

blutbox = BlutBox(**{"blutcount":5})

gun     = Gun(blutbox)

person  = Person(gun)
person.fire()
person.fire()
person.fire()
person.fire()
person.fire()
person.fire()

person.fillblut(2)
person.fire()
person.fire()
person.fire()