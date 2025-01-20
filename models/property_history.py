from odoo import models, fields, api
# *info* models from odoo  to define model of to db , fields to use odoo fields , api to use odoo api 
from odoo.exceptions import ValidationError
from datetime import date, datetime

class PropertyHistory(models.Model):
    # this model for traking changes in porperty state by user and porperty id
    # meta data for model
    _name = 'real.estate.property.history' # *info* name of table in db 
    _description = 'real.estate.property.history'
    
    
    user_id= fields.Many2one('res.users',string='User')
    property_id=fields.Many2one('real.estate.property',string='Property')
    old_state= fields.Char()
    new_state=fields.Char()
    reason=fields.Char()
