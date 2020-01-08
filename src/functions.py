# Imports
import math, os

class Settings():
	"""docstring for settings"""
	def __init__(self, sysBuilder):
		super(Settings, self).__init__()
		self.sysBuilder = sysBuilder
		
	def save(self, system):
		with open(f'/saved/{system["name"]}.json', 'w') as outfile:
			json.dump(system, outfile)

	def load(self):
		pass