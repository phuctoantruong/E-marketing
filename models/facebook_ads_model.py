# -*- coding: utf-8 -*-
from openerp import models, fields, api

from facebookads.api import FacebookAdsApi
from facebookads import objects# Define app information
from facebookads.objects import Campaign

import json

import random
from random import randint
import string

class FacebookAds(models.Model):
    _name = 'emarketingapp.facebookads'
    _description = 'Facebook Ads Object'
    name = fields.Char(required=True, default='Click on generate name!')
    result = fields.Integer('Result', required=True)   
    # Number of people your ad was shown to
    reach = fields.Integer('Reach', required=True)
    # Cost per Click
    cost = fields.Integer('CPC Average', required=True)
    # The total amount you've spent during the dates you've selected in your Ads Manager.
    amount_spent = fields.Integer('Amount Spent', required=True)
    budget = fields.Integer('Budget', required=True)
    
#     def insert_recinto(self,cr,uid, name_campaign, result, reach, cost, amount_spent, budget, context=None):
#         cr.execute("INSERT INTO gs_recintos (name_campaign, result, reach, cost, amount_spent, budget) VALUES ('%s','%s','%s','%s','%s','%s')" %(name_campaign, result, reach, cost, amount_spent, budget))
#         return True
#     def do_foo(self, cr, uid, ids, context = None): 
#         wizard = self.browse(cr, uid, ids[0], context = context) 
#         my_field_value = wizard.name_campaign
#         return True
    #==============================================
    @api.one
    def generate_record(self):
        my_app_id = '881513028613192'
        my_app_secret = '4252ecaa9b6b11ed5d72ddb8fc2528db'
        my_access_token = 'CAAMhuz7vdEgBAPSuWuBSoCjsV0P45Y3KrqU7y5blqHVyM3XshUN9Dr3ZBNJWZCGJljogD6ZC2XSbqXT4D7I6PVH7isy4EBDqb1U3lB005yIM65ov4fCYUKz3J42kxMfwZBpVZABqBM5vOjZApE6ZC9PvOkRnc7mwZBMFZBnVXBiy37LgJJP2RQrZACpTac2s9INasZD'
        FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
        
        campaign = Campaign('6029907036952')
        campaign.remote_read(fields=[
            Campaign.Field.name,
            Campaign.Field.effective_status,
            Campaign.Field.objective,
        ])
        params = {
            'date_preset': 'last_30_days',
        }
        insights = campaign.get_insights(params=params)
        
        self.write({'name': campaign['name']})
        self.write({'result': insights[0]['actions'][0]['value']})
        self.write({'reach': insights[0]['reach']})
        self.write({'cost': insights[0]['cost_per_total_action']})
        self.write({'amount_spent': insights[0]['spend']})