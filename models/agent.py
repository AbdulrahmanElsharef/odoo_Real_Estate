from odoo import models, fields,api

class Agent(models.Model):
    _name = 'real.estate.agent'
    _description = 'Real Estate Agent'
    _rec_name="name" # *info*name for record like __Str_ 
    _order = 'name asc'

    name = fields.Char(string='Agent Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    property_ids = fields.One2many('real.estate.property', 'agent_id', string='Properties')
    ref = fields.Char(string='Ref', readonly=True , default=lambda self: self._generate_reference() )

    @api.model
    def _generate_reference(self):
        """Generate a unique reference using the sequence."""
        return self.env['ir.sequence'].next_by_code('agent_seq') or 'New'