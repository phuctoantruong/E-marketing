# -*- coding: utf-8 -*-
from openerp import models, fields

class ListKeywordSEO(models.Model):
    _name = 'emarketingapp.listkeyword'
    _description = 'ConversionRate Email'
    keyword = fields.Char('Keyword', required=True)