# -*- coding: utf-8 -*-
from openerp import models, fields

class Task(models.Model):
    _name = 'emarketingapp.task'
    _description = 'Task'
    task_name = fields.Char('Task name', required=True)
    status = fields.Char('Status', required=True)