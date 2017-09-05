from paralleldots.config import get_api_key
import requests
import json

def get_multilang( text, lang_code ):
	api_key  = get_api_key()
	if not api_key == None:
		if type( text ) != str:
			return { "Error": "Input must be a string." }
		elif text in [ "", None ]:
			return { "Error": "Input string cannot be empty." }
		url = "http://apis.paralleldots.com/v2/multilang"
		r =  requests.post( url, params={ "api_key": api_key, "text": text, "lang_code": lang_code } )
		if r.status_code != 200:
			return { "Error": "Oops something went wrong ! You can raise an issue at https://github.com/ParallelDots/ParallelDots-Python-API/issues." }
		r = json.loads( r.text )
		return r
	else:
		return { "Error": "API key does not exist" }