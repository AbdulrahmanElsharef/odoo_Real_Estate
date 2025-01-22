from odoo import models, fields, api

class PropertyExtended(models.Model):
    # Inherit the original model 'real.estate.property' to extend its functionalities
    _inherit = 'real.estate.property'

    # Add a new field named 'code' of type Char
    code = fields.Char(string='Code', tracking=True)

    # Override the existing '_onchange_garden' method
    @api.onchange('state', 'code')  # This function depends on 'state' and 'code' fields
    def _onchange_garden(self):
        for record in self:
            if record.state == "sold":
                # Set the 'code' to "Expire" if the property state is "sold"
                record.code = "Expire"
            else:
                # Set the 'code' to an empty string if the state is not "sold"
                record.code = ""