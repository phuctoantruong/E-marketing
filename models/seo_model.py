# -*- coding: utf-8 -*-
from openerp import models, fields

class SEO(models.Model):
    _name = 'emarketingapp.seo'
    _description = 'SEO Object'
    clicks = fields.Integer('Clicks', required=False)
    success = fields.Integer('Click Success', required=False)