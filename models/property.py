from odoo import models, fields, api
# *info* models from odoo  to define model of to db , fields to use odoo fields , api to use odoo api 
from odoo.exceptions import ValidationError
from datetime import date, datetime

class Property(models.Model):
    # meta data for model
    _name = 'real.estate.property' # *info* name of table in db 
    _description = 'Property' # *info* name of table for record 
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Enable Chatter and Activities
    _rec_name="name" # *info*name for record like __Str_ 
    _order = 'availability_date asc'
    #_rec_names_search= [""]
    # _log_access=False    *info* for disable  (create,write uid and date) 
    
    
    # Basic Fields
    name = fields.Char(string='Property Name', required=True, tracking=True,default="New Property")
    # *info* -string show in ui - required field python restrict  - tracking for track change in ui
    description = fields.Text(string='Description')
    note = fields.Text(string='Notes')
    active = fields.Boolean(string='Active', default=True)
    # *info* default mean default text or choice or boolean display in ui
    price = fields.Float(string='Price', required=True, tracking=True)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    bathrooms = fields.Integer(string='Bathrooms', default=1)
    garage = fields.Boolean(string='Garage', default=False)
    garden = fields.Boolean(string='Garden', default=False)
    garden_area = fields.Float(string='Garden Area (sqm)' , digits=(0,3)) # digits for float means number of digits after points
    total_area = fields.Float(string='Total Area (sqm)', compute='_compute_total_area', store=True)
    #*info*  store true allow to store field in db after compute 
    # and compute means you use compute method in with other fileds 
    availability_date = fields.Date(string='Availability Date', default=fields.Date.today)
    postcode = fields.Char(string='Postcode')
    date_created = fields.Datetime(string='Created On', default=fields.Datetime.now, readonly=True)
    # *info* readonly means this field cant update it 
    image = fields.Binary(string='Property Image', attachment=True)
    # *info* attachment=True means this field allow to upload file

    # Selection Fields
    state = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
    ], string='Status', default='draft', tracking=True)
    property_type = fields.Selection([
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
    ], string='Property Type', default='house')


    # Relational Fields
    agent_id = fields.Many2one('real.estate.agent', string='Agent', required=True)
    offer_ids = fields.One2many('real.estate.offer', 'property_id', string='Offers')
    tag_ids = fields.Many2many('real.estate.tag', string='Tags')

    # # Computed Fields
    # best_offer = fields.Float(string='Best Offer', compute='_compute_best_offer', store=True)
    # is_offer_accepted = fields.Boolean(string='Offer Accepted', compute='_compute_is_offer_accepted', store=True)

    # # Related Fields
    # agent_email = fields.Char(string='Agent Email', related='agent_id.email', readonly=True)
    # agent_phone = fields.Char(string='Agent Phone', related='agent_id.phone', readonly=True)

    # # Sequence Field
    # reference = fields.Char(string='Reference', readonly=True, default=lambda self: self._generate_reference())

    # *info*Constraints  that high level restrict field from pg_db
    _sql_constraints = [
        ('unique_name', 'unique (name)', 'This name must be unique.'),
        ('check_price', 'CHECK(price > 0)', 'The price must be  positive.'),
    ]
    
    # *info* Python Constraints second high level restrict field from Python logic
    @api.constrains('availability_date')
    def _check_availability_date(self):
        for record in self:
            if record.availability_date < date.today():
                raise ValidationError(('Any Property availability_date must be in future '))

    # # Computed Methods
    # @api.depends('offer_ids.price')
    # def _compute_best_offer(self):
    #     for record in self:
    #         record.best_offer = max(record.offer_ids.mapped('price')) if record.offer_ids else 0.0

    # @api.depends('offer_ids.status')
    # def _compute_is_offer_accepted(self):
    #     for record in self:
    #         record.is_offer_accepted = any(offer.status == 'accepted' for offer in record.offer_ids)

    # @api.depends('garden_area', 'living_area')
    # def _compute_total_area(self):
    #     for record in self:
    #         record.total_area = record.garden_area + record.living_area

    # # Onchange Methods
    # @api.onchange('garden')
    # def _onchange_garden(self):
    #     if self.garden:
    #         self.garden_area = 100  # Default garden area
    #     else:
    #         self.garden_area = 0

    # # Sequence Generation
    # @api.model
    # def _generate_reference(self):
    #     return self.env['ir.sequence'].next_by_code('real.estate.property') or 'New'

    # # Workflow Methods
    # def action_mark_sold(self):
    #     self.state = 'sold'

    # def action_mark_canceled(self):
    #     self.state = 'canceled'

    # # Python Constraints
    # @api.constrains('garden_area')
    # def _check_garden_area(self):
    #     for record in self:
    #         if record.garden_area < 0:
    #             raise ValidationError(_('Garden area cannot be negative.'))

    # Override Create Method  
    @api.model_create_multi 
    def create(self, vals):
        print("in create method")
        return super(Property, self).create(vals)


    def write_method(self, vals):
        print("print in write  method")
        return super(Property, self).write(vals)