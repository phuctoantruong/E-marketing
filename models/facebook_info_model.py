from openerp import models, fields, api
import hashlib, json, urllib, requests, binascii, base64

class FacebookInfo(models.Model):
    _name = 'emarketingapp.facebookinfo'
    _description = 'Facebook Info Object'
    yourName = fields.Char('Your Name', required=True, default='Click on button "Get Name" after fill in another fields!')
    yourId = fields.Char('Your ID', required=True)
    appId = fields.Char('Your App ID', required=True)
    appSecret = fields.Char('Your App Sercet', required=True)
    yourAccessToken = fields.Char('User Access Token', required=True)
    appAccessToken = fields.Char('App Access Token', required=True)
    
    def getName(self):
        url = 'https://graph.facebook.com/%s/?fields=name&access_token=%s' % (self.yourId, self.yourAccessToken)
        data = urllib.urlopen(url).read()
        d = json.loads(data)
        self.write({ 'yourName' : d['name'].encode('utf-8') })
            
    def getLongAppAccessToken(self):
        link = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=" + self.appId +"&client_secret=" + self.appSecret + "&fb_exchange_token=" + self.appAccessToken
        s = requests.Session()
        token = s.get(link).content
        token = token.split("&")[0]                 # this strips out the expire info (now set set about 5184000 seconds, or 60 days)
        token = token.strip("access_token=")        # Strips out access token  
        self.write({ 'appAccessToken' : token.encode('base64','strict') })
#         binascii.a2b_hex(a)
        
    @api.one
    def refresh(self):
        self.getName()
        self.write({ 'appId' : self.appId.encode('base64','strict') })
        self.write({ 'appSecret' : self.appSecret.encode('base64','strict') })
        self.write({ 'yourAccessToken' : self.yourAccessToken.encode('base64','strict') })
        self.getLongAppAccessToken()
        
        