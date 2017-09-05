from paralleldots.config import get_api_key
import requests
import json

def get_usage():
	api_key  = get_api_key()
	if not api_key == None:
		url = "http://35.202.76.177/usage"
		r =  requests.post( url, params={ "api_key": api_key } )
		if r.status_code != 200:
			return { "Error": "Oops something went wrong ! You can raise an issue at https://github.com/ParallelDots/ParallelDots-Python-API/issues." }
		r = json.loads( r.text )
		return r
	else:
		return { "Error": "API Key not set." }