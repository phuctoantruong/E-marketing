# -*- coding: utf-8 -*-
from openerp import models, fields

class Projects(models.Model):
    _name = 'emarketingapp.projects'
    _description = 'Projects Management'
    project_name = fields.Char('Project Name', required=True)
    short_desc = fields.Char('Description', required=True)
    status = fields.Char('Status', required=True)    