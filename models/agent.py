from odoo import models, fields

class Agent(models.Model):
    _name = 'real.estate.agent'
    _description = 'Real Estate Agent'
    _rec_name="name" # *info*name for record like __Str_ 
    _order = 'name asc'

    name = fields.Char(string='Agent Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')