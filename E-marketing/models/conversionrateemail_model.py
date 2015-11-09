# -*- coding: utf-8 -*-
from openerp import models, fields

class ConversionRateEmail(models.Model):
    _name = 'emarketingapp.conversionrateemail'
    _description = 'ConversionRate Email'
    click = fields.Integer('Click', required=True)
    success = fields.Integer('Click Success', required=True)   