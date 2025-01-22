from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date, datetime

class PropertyHistory(models.Model):
    # This model is for tracking changes in property state by user and property ID
    _name = 'real.estate.property.history'  # Name of the table in the database
    _description = 'Real Estate Property History'  # Display name for the model

    user_id = fields.Many2one('res.users', string='User')
        # This field is a Many2one relation to the 'res.users' model,
        # which stores user information. It allows linking a property history record
        # to the user who made the state change.

    property_id = fields.Many2one('real.estate.property', string='Property')
        # This field is a Many2one relation to the 'real.estate.property' model,
        # which stores property information. It allows linking a property history record
        # to the specific property that underwent a state change.

    old_state = fields.Char()
        # This field stores the old state of the property before the change.

    new_state = fields.Char()
        # This field stores the new state of the property after the change.

    reason = fields.Char()
        # This field allows users to provide a reason for changing the property state.