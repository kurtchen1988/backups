class DataRouter:
	"""docstring for ClassName"""
	def db_for_read(self, model, **hints):
		if model._meta.app_label == 'change':
			return 'contract'
		elif model._meta.app_label == 'testChange':
			return 'contractTest'
		else:
			return 'default'
		#return None

	def db_for_write(self, model, **hints):
		'''
		if model._meta.app_label == 'backman':
			return 'backman'
		else:
			return 'default'
		'''
		return None

	def allow_relation(self, obj1, obj2, **hints):
		return None

	def allow_migrate(self, db, app_label, model_name=None, **hints):
		if app_label == 'default':
			return db == 'default'
		else:
			return False
		#return False