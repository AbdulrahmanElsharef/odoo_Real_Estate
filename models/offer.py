from odoo import models, fields, api

class Offer(models.Model):
    """
    This class defines the `real.estate.offer` model in Odoo,
    representing offers made on real estate properties.
    """
    _name = 'real.estate.offer'  # Name of the table in the database
    _description = 'Real Estate Offer'  # Display name of the table in Odoo
    _rec_name = "name"  # Field used to display the record name (like __str__)
    _order = 'price asc'  # Default sorting for offer records (ascending by price)

    # Basic Offer Information
    name = fields.Char(string='Offer Name', required=True)  # Required field for offer name
    phone = fields.Char(string='Phone')  # Optional field for phone number

    # Offer Details
    price = fields.Float(string='Price', required=True)  # Required field for offer price

    # Relationship with Property
    property_id = fields.Many2one('real.estate.property', string='Property')  
    # Many-to-One relationship with the `real.estate.property` model

    # Derived Fields from Related Property
    agent_id = fields.Many2one('real.estate.agent', string='Agent', related='property_id.agent_id', store=True)  
    # Agent linked to the property (related field)
    state = fields.Selection(related='property_id.state', string='State', store=True)  
    # State of the property (related field)

    # Reference Field
    ref = fields.Char(
        string='Ref',
        readonly=True,
        default=lambda self: self._generate_reference(),
    )  # Read-only field for offer reference, generated automatically

    @api.model
    def _generate_reference(self):
        """
        This method generates a unique reference code for each offer record.
        """
        # Get the next reference number from the sequence named 'offer_seq'
        reference = self.env['ir.sequence'].next_by_code('offer_seq')

        # If no sequence number is available, return 'New'
        return reference or 'New'