import random
import math

class Velocity:



	def __init__(self):
		angle = random.randint(1,360)
		self.magnitude = random.randint(0,60)
		self.height = random.randint(3,30)
		self.toCoord(angle, self.magnitude)


	def toCoord(self,theta,mag):
		dilutemag = mag*1.5
		self.xcoord = dilutemag * math.cos(math.radians(theta))
		self.ycoord = dilutemag * math.sin(math.radians(theta))
		self.arrowSides(theta,dilutemag)
		self.wherelabel(theta)
		# print "X: "+str(xcoord)+" | Y: " + str(ycoord)
	def arrowSides(self,theta,mag):
		#reduction factor for sides
		rf = .9

		#sides
		self.leftx = rf*mag*math.cos(math.radians(theta+10))
		self.lefty = rf*mag*math.sin(math.radians(theta+10))

		self.rightx = rf*mag*math.cos(math.radians(theta-10))
		self.righty = rf*mag*math.sin(math.radians(theta-10))

	def wherelabel(self, theta):
		if(theta>180):
		#choose end of stick
			self.booleanchoice = 0

		else:
		#choose point of stick
			self.booleanchoice = self.ycoord