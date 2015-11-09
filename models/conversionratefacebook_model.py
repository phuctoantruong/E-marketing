# -*- coding: utf-8 -*-
from openerp import models, fields

class ConversionRateFacebook(models.Model):
    _name = 'emarketingapp.conversionratefacebook'
    _description = 'ConversionRate Facebook'
    click = fields.Integer('Click', required=True)
    success = fields.Integer('Click Success', required=True)   