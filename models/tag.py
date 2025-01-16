from odoo import models, fields

class Tag(models.Model):
    _name = 'real.estate.tag'
    _description = 'Real Estate Tag'
    _order = 'name asc'  # Sort tags alphabetically by name

    # Fields
    name = fields.Char(string='Tag Name', required=True, translate=True)
    color = fields.Integer(string='Color Index')  # Used for coloring tags in views

    # Constraints
    _sql_constraints = [
        ('unique_tag_name', 'UNIQUE(name)', 'Tag name must be unique!'),
    ]