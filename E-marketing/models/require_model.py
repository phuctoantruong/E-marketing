# -*- coding: utf-8 -*-
from openerp import models, fields
from select import select

class Require(models.Model):
    _name = 'emarketingapp.require'
    _description = 'Require'
    project_name = fields.Char('Project Name', required=True)
    desc = fields.Char('Description', required=True)   
    budget = fields.Integer('Budget', required=True)
    customer = fields.Many2one('emarketingapp.customers','Customer', ondelete='set null')