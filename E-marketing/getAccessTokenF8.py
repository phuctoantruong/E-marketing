import requests

access_token = 'CAAMhuz7vdEgBABXkAN3X0ENuqiv7AET5OxLbzPsPV4iZBnoLg57K3uDtMoffB3IoZCH8X6mDqBeW58R4biv32PyziVQfmL1gbQCbIkBPtGT1pMBHZBsfmAfjZA4VfbTsC9MTxk0UCOOvK7vZC3cBA0aGIxq30DX6BfwiIYvk4hiMnPUZAdA201CbtiYAjyZCv5F3Au507ndZBAZDZD'      # Obtained from https://developers.facebook.com/tools/accesstoken/
app_id = "881513028613192"                       # Obtained from https://developers.facebook.com/        
client_secret = "4252ecaa9b6b11ed5d72ddb8fc2528db"         # Obtained from https://developers.facebook.com/

link = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=" + app_id +"&client_secret=" + client_secret + "&fb_exchange_token=" + access_token
s = requests.Session()
token = s.get(link).content
token = token.split("&")[0]                 # this strips out the expire info (now set set about 5184000 seconds, or 60 days)
token = token.strip("access_token=")        # Strips out access token
print token