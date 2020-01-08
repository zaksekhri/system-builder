# Imports
import math, os, sys
from src.star import Star
from src.planet import Planet
from src.functions import Settings

""" 
Credits and Sources
"""

class sysBuilder:
	"""docstring for sysBuilder"""
	def __init__(self):
		super(sysBuilder, self).__init__()

	# Global 
	au  = 149597871
	pie = 3.14159265
	tab = "    "

	# Components of sysBuilder
	## Configures the star class as a function of sysBuilder so it can be called directly from sysBuilder
	def star(self):
		s = Star(self)
		return s

	## Configures the Planet class as a function of sysBuilder so it can be called directly from sysBuilder
	def planet(self):
		p = Planet(self)
		return p

	## Configures the Settings class as a function of sysBuilder so it can be called directly from sysBuilder
	def settings(self):
		s = Settings(self)
		return s

	# Input Requests
	## Requests string input from the user
	### stringMessage = the message to be printed out to the user
	def reqInput(self, stringMessage):
		return input(f"{stringMessage}")

	## Requests a number value with the given upper and lower boundaries applied to it
	### type = what type of number, if it doesnt match whats below the just returns an int object
	#### float 
	### stringMessage = to be passed onto reqInput
	### int<>Bound
	#### Upper = the highest value that's accepted
	#### Lower = the lowest value that's accepted
	def reqNumbInput(self, type, stringMessage, intUpperBound=9999, intLowerBound=-9999):
		stringErrorMessage = f"Out of bounds. Enter between {intLowerBound} and {intUpperBound}"

		if type == "float":
			choice = float(self.reqInput(stringMessage))
			intLowerBound = float(intLowerBound)
			intUpperBound = float(intUpperBound)
			if intLowerBound <= choice <= intUpperBound:
				return choice
			else:
				print(stringErrorMessage)
		else:
			choice = int(self.reqInput(stringMessage))
			if intLowerBound <= choice <= intUpperBound:
				return choice
			else:
				print(stringErrorMessage)

	# Menus
	# The initial menu shown to the user
	def main(self):
		entered = self.menuBuilder("Main", "Create New System", "Load System -- (not functional)", "About -- (not functional)")

		if entered == 1:
			self.newSys()
		elif entered == 2:
			pass
		elif entered == 3:
			pass
		elif entered == 0:
			print("Closing System Builder.")
			sys.exit()

	# The main menu where all other menus arise from
	def mainmenu(self):
		while True:
			entered = self.menuBuilder("System Builder", "View System Info -- (returns the dictionary so not really clean)", "Edit System -- (not functional)", "Add entry -- (not functional)", "Settings")

			if entered == 1:
				print(self.system)
			elif entered == 4:
				self.settingsmenu(self.system)
			elif entered == 0:
				self.main()
				break
				

	# Dynamically builds the menu displayed to the user and manages the entered value
	def menuBuilder(self, menuName ,*args):
		options = f"{menuName} Menu:"
		counter = 1
		for arg in args:
			options += f"\n{self.tab}{counter}: {arg}"
			counter += 1  # += is a shorthand of counter = counter + 1 or the other methods to do it
			if len(args) == counter-1:
				options += f"\n{self.tab}0: Exit \
								\n\nSelector: "

		choice = self.reqNumbInput("n", options, counter, 0)
		return choice 

	def newSys(self):
		print("First we need to make a star for the system")
		star = self.star().new()

		name = self.reqInput("To wrap up the basic settings, what's the name of the system? ")
		self.system = {
			"name" : name,
			"star" : star
		}

		self.mainmenu()

	def settingsmenu(self, system):
		while True:
			entered = self.menuBuilder(f"{system['name']} Settings","Save", "Export")

			if entered == 1:
				self.settings().save(self.system)
			elif entered == 2:
				print("Export")
			elif entered == 0:
				break # cant used sys.exit as that would end the entire script, thats why break

try:
	sysBuilder().main()
except Exception as e:
	raise e

# PyInstaller -- to build it into a .exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)