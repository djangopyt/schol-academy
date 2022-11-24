
from odoo import models, fields, api


class partner(models.Model):

     _name = 'res.partner'
     _inherit = "res.partner"

     instructor = fields.Boolean('instructor', Default=False)
     session_ids = fields.Many2many('schol1.session', string='attended sessions',readonly=True)