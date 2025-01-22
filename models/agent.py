from odoo import models, fields, api

class Agent(models.Model):
    """
    This class defines the `real.estate.agent` model in Odoo,
    representing real estate agents.
    """
    _name = 'real.estate.agent'  # Name of the table in the database
    _description = 'Real Estate Agent'  # Display name of the table in Odoo
    _rec_name = "name"  # Field used to display the record name (like __str__)
    _order = 'name asc'  # Default sorting for agent records (ascending by name)

    # Basic Agent Information
    name = fields.Char(string='Agent Name', required=True)  # Required field for agent's name
    email = fields.Char(string='Email')  # Optional field for agent's email address
    phone = fields.Char(string='Phone')  # Optional field for agent's phone number

    # Relationship with Properties
    property_ids = fields.One2many('real.estate.property', 'agent_id', string='Properties')  
    # One-to-Many relationship with the `real.estate.property` model

    # Reference Field
    ref = fields.Char(
        string='Ref',
        readonly=True,
        default=lambda self: self._generate_reference(),
    )  # Read-only field for agent reference, generated automatically

    @api.model
    def _generate_reference(self):
        """
        This method generates a unique reference code for each agent record.
        """
        # Get the next reference number from the sequence named 'agent_seq'
        reference = self.env['ir.sequence'].next_by_code('agent_seq')
        # If no sequence number is available, return 'New'
        return reference or 'New'