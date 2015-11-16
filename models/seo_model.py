# -*- coding: utf-8 -*

from openerp import models, fields,api
from googleads import adwords
from openerp.http import request

class SEO(models.Model):
    _name = 'emarketingapp.seo'
    _description = 'SEO Object'
    keyword = fields.Char('Keyword', required=True)
    location= fields.Char('location',required=False)
    keywords = fields.One2many('emarketingapp.listkeyword','keywords','List Keyword')

    @api.one
    def button_get_keyword2(self):
        cr, uid, pool = request.cr, request.uid, request.registry
        listkeyword = pool['emarketingapp.listkeyword']
        keywords = self.keyword
        print keywords
        adwords_client = adwords.AdWordsClient.LoadFromStorage()
        adwords_client.SetClientCustomerId('2253118112')
        PAGE_SIZE = 100
        targeting_idea_service = adwords_client.GetService(
                'TargetingIdeaService', version='v201509')
        offset =0
        selector = {
                'searchParameters':[
                    {
                        'xsi_type':'RelatedToQuerySearchParameter',
                        'queries': [keywords]
                    },
                    {
                        'xsi_type': 'LanguageSearchParameter',
                        'languages': [{'id': '1040'}]
                    }
                ],
                'ideaType': 'KEYWORD',
                'requestType': 'IDEAS',
                'requestedAttributeTypes': ['KEYWORD_TEXT',
                                            'SEARCH_VOLUME',
                                            'COMPETITION',
                                            'CATEGORY_PRODUCTS_AND_SERVICES'
                                            ],
                    'paging': {
                        'startIndex': str(offset),
                        'numberResults': str(PAGE_SIZE)
                        }
                    }
        count = 0
        max=9
        number = 1
        more_pages = True
        while more_pages:
                page = targeting_idea_service.get(selector)
                # Display results.
                if 'entries' in page:
                  for result in page['entries']:
                    if count < max:
                        count=count+number
                        attributes = {}
                        for attribute in result['data']:
                          attribute_value = attribute['value']
                          if 'value' in attribute_value:
                            attributes[attribute['key']] = attribute_value['value']
                          else:
                            attributes[attribute['key']] = []
                        print (attributes['KEYWORD_TEXT'])
                        listkeyword.create(cr, uid, {'id':self.id,'keyword': attributes['KEYWORD_TEXT'],'volume':attributes['SEARCH_VOLUME'],'competition':attributes['COMPETITION']})
                        #cr.execute('insert into emarketingapp.listkeyword (keyword,volume) values($s,$s)',(attributes['KEYWORD_TEXT'],attributes['SEARCH_VOLUME']))
                    else:
                        break
                  print
                else:
                  print 'No related keywords were found.'
                offset += PAGE_SIZE
                selector['paging']['startIndex'] = str(offset)
                more_pages = offset < int(page['totalNumEntries'])