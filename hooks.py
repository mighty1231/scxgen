'''
User-section on this project.
Any hooks for convenience can be defined on this section

	with OnCondition([Deaths().PUnit((P8, 'Terran Marine')).AtLeast(8), Switch(4, Set)]):
		Trigger(...) # 1
		Trigger(...) # 2
	Trigger(...) # 3

	Then Trigger1 and Trigger2 would add those conditions.
'''

from .sections.trigsection import Trigger

class HookBase:
	def InstallHook(self):
		raise NotImplementedError

	def UninstallHook(self):
		raise NotImplementedError

	def __enter__(self):
		self.InstallHook()

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.UninstallHook()

# just add conditions on trigger
class OnCondition(HookBase):
	def __init__(self, conds):
		# It seems strangee, but Trigger object flattening conditions after hook functions
		self.hookfunc = lambda trig:trig.conditions.append(conds)

	def InstallHook(self):
		Trigger.InstallHook(self.hookfunc)

	def UninstallHook(self):
		Trigger.UninstallHook(self.hookfunc)


