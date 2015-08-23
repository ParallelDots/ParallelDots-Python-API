import urllib3, urllib
import json
from paralleldots.config import get_api_key
http = urllib3.PoolManager()
def get_sentiment(s1):
	apikey  = get_api_key()
	if not apikey == None:
		return "SENTIMENT API is currently underconstruction. You will be notified via email once it is up."
	else:
		return "API key does not exist"




