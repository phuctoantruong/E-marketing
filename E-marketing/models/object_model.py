# -*- coding: utf-8 -*-
from openerp import models, fields

class Object(models.Model):
    _name = 'emarketingapp.object'
    _description = 'Object'
    click = fields.Integer('Click', required=True)
    success = fields.Integer('Click Success', required=True)   