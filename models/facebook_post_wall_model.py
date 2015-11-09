# -*- coding: utf-8 -*-
from openerp import models, fields, api
import facebook
import json

class FacebookPostWall(models.Model):
    _name = 'emarketingapp.facebookpostwall'
    _description = 'Facebook Post Wall Object'
    id = fields.Char(required=True)
    dateCreate = fields.Datetime
    content = fields.Char
    
    @api.one
    def post_to_wall(self):
        self.write({'content': ''})
    
    