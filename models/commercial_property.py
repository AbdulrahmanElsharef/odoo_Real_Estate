from odoo import models, fields, api

class CommercialProperty(models.Model):
    _name = 'real.estate.property.commercial'  # New model name
    _inherit = 'real.estate.property'  # Inherit all fields and methods from Property model

    # Add new fields
    business_type = fields.Selection([
        ('office', 'Office'),
        ('retail', 'Retail'),
        ('warehouse', 'Warehouse'),
    ], string='Business Type', default='office', tracking=True)

    lease_term = fields.Integer(string='Lease Term (Months)', tracking=True)

    # Add a new method
    def calculate_lease_cost(self):
        for record in self:
            if record.lease_term and record.price:
                lease_cost = record.price * record.lease_term
                print(f"Total Lease Cost for {record.name}: {lease_cost}")
            else:
                print(f"Lease Cost cannot be calculated for {record.name}")

    # Override an existing method
    def action_sold(self):
        res=super(CommercialProperty, self).action_sold()
        self.lease_term=0
        return res