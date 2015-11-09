# -*- coding: utf-8 -*-
from openerp import models, fields

class ConversionRateSEO(models.Model):
    _name = 'emarketingapp.conversionrateseo'
    _description = 'ConversionRate SEO'
    click = fields.Integer('Click', required=True)
    success = fields.Integer('Click Success', required=True)   