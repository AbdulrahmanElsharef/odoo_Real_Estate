from odoo import models, fields, api

class PropertyWizard(models.TransientModel):
    # transit model not save in db 
    _name = 'property.wizard'
    _description = 'Property Wizard'

    # Fields
    property_id=fields.Many2one('real.estate.property',string='Property')
    # relations with property
    reason= fields.Char()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
    ], string='State', default='draft')

    # Method to update the state of selected properties
    def update_state_method(self):
        # update method for update button to change state if closed
        if self.state == 'closed':
            self.property_id.state=self.state
            self.property_id.create_history('closed',self.state,self.reason)
