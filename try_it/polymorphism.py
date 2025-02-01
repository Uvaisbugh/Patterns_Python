from abc import ABC, abstractmethod

class Car(ABC):
	@abstractmethod
	def sound(self):
		pass


class Honda(Car):
	def sound(self):
		return "phooo!"


class Benz(Car):
	def sound(self):
		return "phaaa!"


class Vw(Car):
	def sound(self):
		return "phee!"


# def horn(car):
# 	print(car.sound())

Accord = Honda()
S_class = Benz()
gti = Vw()

print(Accord.sound())
print(S_class.sound())
print(gti.sound())
# horn(Accord)
# horn(S_class)
# horn(Vw)
#
