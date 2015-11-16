# -*- coding: utf-8 -*-
from openerp import models, fields, api
import facebook
import json, hashlib, hmac

class FacebookPostWall(models.Model):
    _name = 'emarketingapp.facebookpostwall'
    _description = 'Facebook Post Wall Object'
    id = fields.Char
    content = fields.Char(required=True)
    
    def getId(self):
        access_token = 'CAACEdEose0cBAPGxcBvUD7ivSNQk9OTZCxziBn2O68sI4aLEcgQb2KMZB4pD6z063YhqIYZA1Oh16V1oTZBSxcH9mZCIHWdQs8P0NhWIV2QTQZAKwRrXypIg9JZCak2nfA9uFRTjHumLJKimGAogG3FUzYxY8UprXuAS4wcljYGq6gnVhDG13CT9wGawUA6dHUuIA7f4ZCyk1wZDZD'
        user = '576126995829584'
        
        graph = facebook.GraphAPI(access_token)
        profile = graph.get_object(user)
        posts = graph.get_connections(profile['id'], 'feed')
        self.write({ 'id' : posts['data'][0]['id'] })
        
    def genAppSecretProof(self, app_secret, access_token):
        h = hmac.new (
            app_secret.encode('utf-8'),
            msg=access_token.encode('utf-8'),
            digestmod=hashlib.sha256
        )
        return h.hexdigest()
    
    @api.one
    def post(self):
        app_secret = "4252ecaa9b6b11ed5d72ddb8fc2528db"
        access_token = "CAAMhuz7vdEgBAEAk6mob1sA9Pio8nwYyTMTY9wdzVrL4XizbTdrjaw2Ky4O98ZCZAZCgxoqC3xYtCGdLywR5B9ARuZBBCP3TvGcoceqigUTfZBYrHKKEChC0KUAL7vtOa3ZBD5bniIEdRWZC36l1PIgRZCyF8ZBHfs1u27esJ4H4nCIXtJMogZAkLZCCZChphBZBsODIhPNQ1L8e0SQZDZD"
        api = facebook.GraphAPI(access_token)
        msg = self.content
        postargs = {"appsecret_proof": self.genAppSecretProof(app_secret, access_token)}
        status = api.put_wall_post(msg, postargs)
        
    