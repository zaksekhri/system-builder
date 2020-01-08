# Imports
import math

# Class
class Planet:
	def __init__(self, sysBuilder):
		super(Planet, self).__init__()
		self.sysBuilder = sysBuilder

	# Global

	## These are the absolute values of earth all used to check the absolute values of the created planet
	absolute = {
		"mass" : { # in kg
			"short" : "5.97237 * 10^24",
			"true" : 5974000000000000000000000
		}, 
		"radius": 6371.0, # in km
		"density": 5.52 # grams per cm cubed / g/cm^3
	}

	## Moon
	## Registers the moon class as a function of Planet so functions from moon can be called directly from the Planet class
	def moon(self):
		m = moon(self)
		return m

	# Creates a new planet, with the nested moon maker being there as well
	def new(self):
		print(f"There are four things that will be needed to create this new planet.\
			\nIts name, distance (in AU) from its star, mass and radius, with the mass and radius being relative to earth.")

		name = self.sysBuilder.reqNumbInput("float", "Planet Name: ")
		distance = self.sysBuilder.reqNumbInput("float", "Distance (in AU): ")
		mass = self.sysBuilder.reqNumbInput("float", "Relative to the earth, what's it's mass?")
		radius = self.sysBuilder.reqNumbInput("float", "Relative to the earth, what's it's radius?")
		density = self.density(mass, radius)
		sg = self.surfgrav(mass, radius)

		planet = { # used for the backend, all values relative to earth
			"name": name,
			"distance": distance,
			"mass": mass,
			"radius": radius,
			"density": density,
			"surfacegrav": sg,
			"moons": {
				"count": 0
			}
		}

		# moons arent working rn, will have to run a seperate test for them
		#while not input == ["no", "n", "No", "nO"]:
			#moondict = planet['moons']
			#input = self.sysBuilder.reqInput("n", "Would you like to make a planet?")
			#moon = self.Planet().moon().new(planet)
			#moondict[f'moon-{moondict['count']}'] = moon
			#moondict['count'] += 1

		return planet # Returns the dictionary

	## Returns the density of the object relative to earth
	### m = the mass of the object
	### r = the radius of the object
	#### No absolute values
	def density(self, m, r):
		den = m / r**3
		return den

	## Returns the surface gravity of the object relative to earth
	### m = the mass of the object
	### r = the radius of the object
	#### No absolute values
	def surfgrav(self, m, r):
		sv = m / r**2
		return sv

# Class moon
## Deals with all moon related things
class moon:
	def __init__(self, Planet):
		super(moon, self).__init__()
		self.Planet = Planet

	def new(self, planet):
		moon = self.moon

		moon = {
			"position": planet['moons']['count'],
			"name": name
		}

	# Calculates the inner limit the moon can be before it gets destroyed by the primaries satellites tidal forces
	# Also known as the roche limit
	## primr = radius of primary relative to earth
	## primd = density of the primary relative to earth
	## satd  = density of the satellite relative to earth
	def boundinner(self, primr, primd, satd):
		bi = 2.44 * primr * (primd / satd)**(1/3)
		return bi

	# Calculates the outer limit the moon can be before it starts to leave the planets gravitational well
	# also known as the hill sphere
	## primDis = distance the primary is from where it orbits around
	## primM = mass of the primary
	## satM = mass of the satellite 
	def boundouter(self, primDis, primM, satM):
		bo = primDis * (satM / primM)**(1/3) * 235
		return bo