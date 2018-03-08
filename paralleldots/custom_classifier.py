from paralleldots.config import get_api_key
import requests
import json

def get_custom_classifier( text, category ):
	api_key  = get_api_key()
	if not api_key == None:
		if type( text ) != str:
			return { "Error": "Input must be a string." }
		elif text in [ "", None ]:
			return { "Error": "Input string cannot be empty." }
		elif type( category ) != dict:
			return { "Error": "Category must be a dictionary." }
		url = "http://apis.paralleldots.com/v3/custom_classifier"
		r =  requests.post( url, params= { "api_key": api_key, "text": text, "category": json.dumps( category ) } )
		if r.status_code != 200:
			return { "Error": "Oops something went wrong ! You can raise an issue at https://github.com/ParallelDots/ParallelDots-Python-API/issues." }
		r = json.loads( r.text )
		return r
	else:
		return { "Error": "API key does not exist" }