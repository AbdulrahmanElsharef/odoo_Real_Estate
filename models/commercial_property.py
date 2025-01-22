from odoo import models, fields, api

class CommercialProperty(models.Model):
    # New model name for commercial properties
    _name = 'real.estate.property.commercial'

    # Inherit all fields and methods from the base 'real.estate.property' model
    _inherit = 'real.estate.property'

    # Add new fields specific to commercial properties
    business_type = fields.Selection([
        ('office', 'Office'),
        ('retail', 'Retail'),
        ('warehouse', 'Warehouse'),
    ], string='Business Type', default='office', tracking=True)
    lease_term = fields.Integer(string='Lease Term (Months)', tracking=True)

    # Add a new method to calculate lease cost
    def calculate_lease_cost(self):
        for record in self:
            if record.lease_term and record.price:
                # Calculate lease cost by multiplying price and lease term
                lease_cost = record.price * record.lease_term
                print(f"Total Lease Cost for {record.name}: {lease_cost}")