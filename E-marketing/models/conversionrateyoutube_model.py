# -*- coding: utf-8 -*-
from openerp import models, fields

class ConversionRateYoutube(models.Model):
    _name = 'emarketingapp.conversionrateyoutube'
    _description = 'ConversionRate Youtube'
    click = fields.Integer('Click', required=True)
    success = fields.Integer('Click Success', required=True)   