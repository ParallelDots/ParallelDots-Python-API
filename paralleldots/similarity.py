from paralleldots.config import get_api_key
import requests
import json

def get_similarity( text ):
	api_key  = get_api_key()
	if not api_key == None:
		if type( text_1 ) != str or type( text_2 ) != str:
			return { "Error": "Input must be a string." }
		elif text_1 == "" or text_2 == "":
			return { "Error": "Input string cannot be empty." }
		url = "http://35.202.76.177/v2/similarity"
		r =  requests.post( url, params={ "api_key": api_key, "text_1": text_1, "text_2": text_2 } )
		if r.status_code != 200:
			return { "Error": "Oops something went wrong ! You can raise an issue at https://github.com/ParallelDots/ParallelDots-Python-API/issues." }
		r = json.loads( r.text )
		return r
	else:
		return { "Error": "API key does not exist" }