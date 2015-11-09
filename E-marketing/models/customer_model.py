# -*- coding: utf-8 -*-
from openerp import models, fields

class Customers(models.Model):
    _name = 'emarketingapp.customers'
    _description = 'Customers Management'
    fullname = fields.Char('Customer Name', required=True)
    address = fields.Char('Address', required=True)
    numberPhone = fields.Char('Number Phone', required=True)
    
    