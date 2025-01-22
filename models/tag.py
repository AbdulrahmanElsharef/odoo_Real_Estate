from odoo import models, fields

class Tag(models.Model):
    """
    This class defines the `real.estate.tag` model in Odoo,
    representing tags used to categorize real estate properties.
    """

    _name = 'real.estate.tag'  # Name of the table in the database
    _description = 'Real Estate Tag'  # Display name of the table in Odoo
    _order = 'name asc'  # Default sorting for tag records (ascending by name)

    # Fields
    name = fields.Char(
        string='Tag Name',
        required=True,
        translate=True,
    )  # Required field for tag name, translatable for multilingual support
    color = fields.Integer(string='Color Index')  # Optional integer field for color coding tags in views

    # Many-to-Many Relationship with Properties
    property_ids = fields.Many2many('real.estate.property', string='Properties')  # Links tags to many related property records

    # Database Constraint
    _sql_constraints = [
        ('unique_tag_name', 'UNIQUE(name)', 'Tag name must be unique!'),
    ]  # Ensures that tag names are unique within the database