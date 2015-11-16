# -*- coding: utf-8 -*-
from openerp import models, fields
from openerp import exceptions

import logging
_logger=logging.getLogger(__name__)

class ListKeywordSEO(models.Model):
    _name = 'emarketingapp.listkeyword'
    _description = 'ConversionRate Email'
    keywords = fields.Many2one('emarketingapp.seo', string='Tasks')
    keyword = fields.Char('Keyword',required=True)
    volume = fields.Char('Volume',required=False)
    cpc = fields.Char('CPC',required=False)
    competition = fields.Char('Competition',required=False)
