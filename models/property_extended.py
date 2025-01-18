from odoo import models, fields, api

class PropertyExtended(models.Model):
    # _name = 'real.estate.property'  # Same as the original model
    _inherit = 'real.estate.property' 
     # Inherit the original model to extend field and method

    # Add a new field
    code = fields.Char(string='Code', tracking=True)

    # # Add a new method
    # def new_method(self):
    #     for record in self:
    #         print(f"New Method Called for Property: {record.name}")

    # Override an existing method
    @api.onchange('state','code')
    def _onchange_garden(self):
        if self.state == "sold":
            self.code = "Expire"  # Default garden area
        else:
            self.code = ""
