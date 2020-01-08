# Imports
import math

# Class
class Star:
	def __init__(self, sysBuilder):
		super(Star, self).__init__()
		self.sysBuilder = sysBuilder

	# Global

	## These are the absolute values of our own sun, all used to check the absolute values of the created star
	absolute = {
		"mass" : { # in kg
			"short" : "1.98855 * 10^30",
			"true" : 1988546924138717739712069812881, 
			"exact": 1988546924138717739712069812881.3396785059276218789
		}
	}

	## Registers the zone class as a function of Star so it can be called thru the star class directly
	def zone(self):
		z = zone(self)
		return z

	## Creates a new star and returns a dictionary of the star
	def new(self):
		print(f"There are a two things that will be needed to create this new star.\
			\nIts name and mass, with the mass being relative to our sun's mass of {self.absolute['mass']['short']} kg.")

		name = self.sysBuilder.reqInput("Star Name: ")
		mass = self.sysBuilder.reqNumbInput("float", "Relative to the sun, what's it's mass? ")
		lum = self.lum(mass)
		diam = self.diam(mass)
		surftemp = self.surftemp(mass)
		lifetime = self.lifetime(mass)
		innerbound = self.zone().planetInBound(mass)
		outerbound = self.zone().planetOutBound(mass)
		frostline = self.zone().frostline(lum)
		habmid = self.zone().habmid(lum)
		habinner = self.zone().habinner(habmid)
		habouter = self.zone().habouter(habmid)

		star = { # Creates the dictionary and assigns all the variables to their correct location, this dictionary is backend however
			"name": name,
			"stats": {
				"mass": mass,
				"lum": lum,
				"diam": diam,
				"surftemp": surftemp,
				"lifetime": lifetime,
				"zones": {
						"innerbound": innerbound,
						"outerbound": outerbound,
						"frostline": frostline,
						"habmid": habmid,
						"habinner": habinner,
						"habouter": habouter
				}
			}
		}

		return star # Returns the dictionary

	# Stats for the star

	## Returns the luminosity of the star relative to our own
	## m = mass of the star relative to the sun
	### No absolute values
	def lum(self, m):
		lum = m**3
		return lum

	## Returns the diameter of the star relative to our own
	## m = mass of the star relative to the sun
	### No absolute values
	def diam(self, m):
		diam = m**0.74
		return diam

	## Returns the surface temp of the star relative to our own
	## m = mass of the star relative to the sun
	### No absolute values
	def surftemp(self, m):
		st = m**0.505
		return st

	## Returns the lifetime of the star relative to our own
	## m = mass of the star relative to the sun
	### No absolute values
	def lifetime(self, m):
		lt = m**-2.5
		return lt

class zone:
	def __init__(self, Star):
		super(zone, self).__init__()
		self.Star = Star

	# Planet bounds
	## Returns the inner boundaries for planets so they dont get ripped apart in tidal forces
	## mass = the mass of the star relative to the sun
	### No absolute values
	def planetInBound(self, mass):
		pi = 0.1*mass
		return pi

	## Returns the outer boundary for planets to safely exist in the solar system
	## mass = the mass of the star relative to the sun
	### No absolute values
	def planetOutBound(self, mass):
		po = 40*mass
		return po

	# Returns the frost line of the system
	## lum = the luminosity of the star relative to the sun
	### No absolute values
	def frostline(self, lum):
		fl = 4.85*math.sqrt(lum)
		return fl

	# Planet Habitability Ranges
	## Returns the midpoint for habitability 
	## lum = the luminosity of the star relative to the sun
	### No absolute values
	def habmid(self, lum):
		ha = math.sqrt(lum)
		return ha

	## Returns the inner range for habitability 
	## m = the midpoint of the hab ring
	def habinner(self, m):
		hi = m * 0.95
		return hi

	## Returns the inner range for habitability 
	## m = the midpoint of the hab ring
	def habouter(self, m):
		ho = m * 1.37
		return ho