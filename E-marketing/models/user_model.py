# -*- coding: utf-8 -*-
from openerp import models, fields

class User(models.Model):
    _name = 'emarketingapp.user'
    _description = 'User'
    fullname = fields.Char('Full name', required=True)
    address = fields.Char('Address', required=True)
    number_phone = fields.Char('Number Phone', required=True)