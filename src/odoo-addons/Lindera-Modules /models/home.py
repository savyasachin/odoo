from odoo import models, fields, api

class LinderHome(models.Model):
	"""
	Add more fields and functions to the home
	"""
	_inherit = 'res.partner'

	senior_number = fields.Integer('senior_number')
	show_senior_number = fields.Boolean('show_senior_number')

	@api.model
	def create(self, values):
		"""
		Creates a new contact instance. Wraps existing method.
		:param values: initial values of the event
		:return: returns an event
		"""

		contact = super(LinderHome, self).create(values)

		if 'category_id' in values.keys():
			isEinrichtung = False
			for id in values['category_id'][0][2]:
				cat = contact.env['res.partner.category'].browse(id)
				if cat.name == 'Einrichtung':
					isEinrichtung = True
			contact.show_senior_number = isEinrichtung
			if not isEinrichtung:
				contact.senior_number = 0

		return contact

	@api.multi
	def write(self, values):
		"""
		Is called whenever a field is changed (even during initialization!).
		:param values: changed fields
		:return: bool writeSuccess
		"""
		if 'category_id' in values.keys():
			isEinrichtung = False
			for id in values['category_id'][0][2]:
				cat = self.env['res.partner.category'].browse(id)
				if cat.name == 'Einrichtung':
					isEinrichtung = True
			self.show_senior_number = isEinrichtung
			if not isEinrichtung:
				self.senior_number = 0

		super(LinderHome, self).write(values)
