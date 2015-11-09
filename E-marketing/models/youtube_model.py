# -*- coding: utf-8 -*-
from openerp import models, fields

class Youtube(models.Model):
    _name = 'emarketingapp.youtube'
    _description = 'Youtube Object'
    clicks = fields.Integer('Clicks', required=False)
    success = fields.Integer('Click Success', required=False)