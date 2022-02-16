#import animal
from animal import Mammal, Dog, Cat

myMammal = Mammal("General Species")
myMammal.showSpecies()
myMammal.makeNoise()

myDog = Dog()
myDog.showSpecies()
myDog.makeNoise()

myCat = Cat()
myCat.showSpecies()
myCat.makeNoise()