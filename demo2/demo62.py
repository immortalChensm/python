from Cat import Cat
from Mouse import Mouse
from Humans import Humans


person = Humans()
tom    = Cat("tom")
jerry  = Mouse("jerry")
'''
person.feedCat(tom,"fish")
person.feedMouse(jerry,"coin")
'''
person.feedAniaml(tom,'fish')
person.feedAniaml(jerry,'jam')
