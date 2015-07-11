import urllib2, urllib
import json
from paralleldots.config import get_api_key

def get_taxonomy(s1):
	apikey  = get_api_key()
	if not apikey == None:
		params = { 'sentence1' : s1, 'apikey' : apikey}
		en_params = urllib.urlencode(params)
		url = 'http://54.255.201.193:7777/taxonomy?'+en_params
		a =  urllib2.urlopen(url)
		return json.load(a)
	else:
		return "API key does not exist"


