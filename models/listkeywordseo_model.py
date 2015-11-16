# -*- coding: utf-8 -*-
from openerp import models, fields

class ListKeywordSEO(models.Model):
    _name = 'emarketingapp.listkeyword'
    _description = 'ConversionRate Email'
    keywords = fields.Many2one('emarketingapp.seo','keywords', ondelete='cascade', select=1)
    keyword = fields.Char('Keyword',required=True)
    volume = fields.Char('Volume',required=False)
    cpc = fields.Char('CPC',required=False)
    competition = fields.Char('Competition',required=False)
