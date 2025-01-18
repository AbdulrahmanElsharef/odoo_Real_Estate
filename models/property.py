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
    _order = 'price asc'
    #_rec_names_search= [""]
    # _log_access=False    *info* for disable  (create,write uid and date) 
    
    
    # Basic Fields
    name = fields.Char(string='Property Name', required=True, tracking=True,default="New Property")
    # *info* -string show in ui - required field python restrict  - tracking for track change in ui
    description = fields.Text(string='Description', tracking=True)
    note = fields.Text(string='Notes' , tracking=True)
    active = fields.Boolean(string='Active', default=True)
    # *info* default mean default text or choice or boolean display in ui
    price = fields.Float(string='Price', required=True, tracking=True)
    living_area = fields.Integer(string='Living Area (sqm)' , digits=(0,3) , tracking=True)
    bedrooms = fields.Integer(string='Bedrooms', default=2 , tracking=True)
    bathrooms = fields.Integer(string='Bathrooms', default=1 , tracking=True)
    garage = fields.Boolean(string='Garage', default=False , tracking=True)
    garden = fields.Boolean(string='Garden', default=False , tracking=True)
    garden_area = fields.Float(string='Garden Area (sqm)' , digits=(0,3) , tracking=True) # digits for float means number of digits after points
    total_area = fields.Float(string='Total Area (sqm)', compute='_compute_total_area', store=True )
    #*info*  store true allow to store field in db after compute 
    # and compute means you use compute method in with other fileds 
    availability_date = fields.Date(string='Availability Date' )
    offer_date = fields.Date(string='Offer Date' )
    postcode = fields.Char(string='Postcode', tracking=True)
    date_created = fields.Date(string='Created On', default=fields.Date.today, readonly=True)
    # *info* readonly means this field cant update it 
    image = fields.Binary(string='Property Image', attachment=True , tracking=True)
    # *info* attachment=True means this field allow to upload file

    # Selection Fields
    state = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled'),
        ('closed', 'Closed'),
    ], string='Status', default='draft', tracking=True)
    property_type = fields.Selection([
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('villa', 'Villa'),
    ], string='Property Type', default='apartment' , tracking=True)


    # Relational Fields
    agent_id = fields.Many2one('real.estate.agent', string='Agent', required=True  , tracking=True)
    # many2one mean that alot poroperty for one agent name of models related 
    # string for ui and required for user tracking for track change
    offer_ids = fields.One2many('real.estate.offer', 'property_id', string='Offers')
    # One2many mean that alot offers for one porperty  name of models related and 'property_id' that field related in other model 
    # and string for ui and required for user tracking for track change
    tag_ids = fields.Many2many('real.estate.tag', string='Tags'  , tracking=True)
    # Many2many mean that alot poroperty for alot tags  , name of models related 
    # string for ui and required for user tracking for track change

    # Computed Fields
    best_offer = fields.Float(string='Best Offer', compute='_compute_best_offer', store=True )
    # Computed Fields definr by compute=  and name of method and store=True for svae this comuted field in db
    is_offer_accepted = fields.Boolean(string='Offer Accepted', compute='_compute_is_offer_accepted', store=True)

    # Related Fields
    agent_email = fields.Char(string='Agent Email', related='agent_id.email')
    # Related Fields defin by related= and name of field in other model to related with readonly=True for user unable to change
    agent_phone = fields.Char(string='Agent Phone', related='agent_id.phone')

    # # Sequence Field
    ref = fields.Char(string='Ref', readonly=True , default=lambda self: self._generate_reference() )
    # default=lambda self: self._generate_reference()

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

    # Computed Methods
    @api.depends('offer_ids.price') #args is models fields only
    # depends means depend on field in db and non display in ui and reltions fields
    # and you can save it in db any compute fields only on depend method
    def _compute_best_offer(self):
        for record in self:
            record.best_offer = max(record.offer_ids.mapped('price')) if record.offer_ids else 0.0
    # for self record if record of offers mape means select all by price and get max price to save it

    @api.depends('offer_ids.state')
    def _compute_is_offer_accepted(self):
        for record in self:
            record.is_offer_accepted = any(offer.state == 'sold' for offer in record.offer_ids)
            

            
    # for self record if record of ofers state == sold  mape means select any by state and sold state

    @api.depends('garden_area', 'living_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area
    # get rcord and add garedn area to living area to total area

    # Onchange Methods
    @api.onchange('garden') # args is view fields only
    # Onchange Methods means on any change in other field in ui display in tree and form view
    # not store in db
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 50  # Default garden area
        else:
            self.garden_area = 0


    
    @api.model
    def _generate_reference(self):
        """Generate a unique reference using the sequence."""
        return self.env['ir.sequence'].next_by_code('real.estate.property') or 'New'
    # env for explor odoo sequnce and next_by_code related by code in xml file or return new


    def closed_property_automatically(self):
        ids=self.search([])
        # get all porporty by serach
        for rec in ids :
            if rec.offer_date and  rec.offer_date < fields.date.today():
                # get today func from odoo fields 
                self.note = 'offer date is expire'


        
        
        
    # Workflow Methods
    def action_draft(self):
        self.state = 'draft'
        
    def action_available(self):
        self.state = 'available'
        
    def action_sold(self):
        self.state = 'sold'

    def action_canceled(self):
        self.state = 'canceled'
        
    def action_closed(self):
        self.state = 'closed'


    # Override Create Method  
    @api.model_create_multi 
    def create(self, vals):
        print("in create method")
        return super(Property, self).create(vals)


    def write_method(self, vals):
        print("print in write  method")
        return super(Property, self).write(vals)