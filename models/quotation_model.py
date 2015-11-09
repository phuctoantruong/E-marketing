# -*- coding: utf-8 -*-
from openerp import models, fields

class Quotation(models.Model):
    _name = 'emarketingapp.quotation'
    _description = 'Quotation'
    tax = fields.Float('Tax', required=True)
    price = fields.Float('Price', required=True)   
    desc = fields.Char('Description', required=True)