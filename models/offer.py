from odoo import models, fields, api

class Offer(models.Model):
    _name = 'real.estate.offer'
    _description = 'Real Estate Offer'
    _rec_name="name" # *info*name for record like __Str_ 
    _order = 'price asc'

    name = fields.Char(string='Offer Name', required=True)
    phone = fields.Char(string='Phone')
    price = fields.Float(string='Price', required=True)
    property_id = fields.Many2one('real.estate.property', string='Property' )
    agent_id = fields.Many2one('real.estate.agent', string='Agent', related='property_id.agent_id', store=True)
    state = fields.Selection(related='property_id.state', string='State', store=True)
    ref = fields.Char(string='Ref', readonly=True , default=lambda self: self._generate_reference() )

    @api.model
    def _generate_reference(self):
        """Generate a unique reference using the sequence."""
        return self.env['ir.sequence'].next_by_code('offer_seq') or 'New'