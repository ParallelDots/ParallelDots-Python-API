from paralleldots.config import get_api_key
import requests
import json

def get_sentiment( text, lang_code= "en" ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/sentiment", params= { "api_key": api_key, "text": text, "lang_code": lang_code } ).text
	response = json.loads( response )
	return response

def get_ner( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/ner", params= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_keywords( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/keywords", params= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_intent( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/intent", params= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_emotion( text, lang_code= "en" ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/emotion", params= { "api_key": api_key, "text": text, "lang_code": lang_code } ).text
	response = json.loads( response )
	return response

def get_abuse( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/abuse", params= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_taxonomy( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/taxonomy", params= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_similarity( text_1, text_2 ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/similarity", params= { "api_key": api_key, "text_1": text_1, "text_2": text_2 } ).text
	response = json.loads( response )
	return response

def get_custom_classifier( text, category ):
	api_key  = get_api_key()
	if type( category ) == dict:
		category = json.dumps( category )
	response = requests.post( "https://apis.paralleldots.com/v3/custom_classifier", params= { "api_key": api_key, "text": text, "category": category } ).text
	response = json.loads( response )
	return response

def get_phrase_extractor( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/phrase_extractor", params= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_language_detection( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/language_detection", params= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_text_parser( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/text_parser", params= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_multilang_keywords( text, lang_code= "en" ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/multilang_keywords", params= { "api_key": api_key, "text": text, "lang_code": lang_code } ).text
	response = json.loads( response )
	return response

def get_popularity( path ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/popularity", params= { "api_key": api_key }, files= { "file": open( path, "rb" ).read() } ).text
	response = json.loads( response )
	return response

def get_nsfw( path ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/nsfw", params= { "api_key": api_key }, files= { "file": open( path, "rb" ).read() } ).text
	response = json.loads( response )
	return response

def get_facial_emotion( path ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/facial_emotion", params= { "api_key": api_key }, files= { "file": open( path, "rb" ).read() } ).text
	response = json.loads( response )
	return response

def get_object_recognizer( path ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/object_recognizer", params= { "api_key": api_key }, files= { "file": open( path, "rb" ).read() } ).text
	response = json.loads( response )
	return response

def get_popularity_url( url ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/popularity", params= { "api_key": api_key, "url": url } ).text
	response = json.loads( response )
	return response

def get_nsfw_url( url ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/nsfw", params= { "api_key": api_key, "url": url } ).text
	response = json.loads( response )
	return response

def get_facial_emotion_url( url ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/facial_emotion", params= { "api_key": api_key, "url": url } ).text
	response = json.loads( response )
	return response

def get_object_recognizer_url( url ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v3/object_recognizer", params= { "api_key": api_key, "url": url } ).text
	response = json.loads( response )
	return response

def get_usage():
	api_key  = get_api_key()
	if api_key == None or api_key == "":
		return { "Error": "API Key cannot be None or an empty String." }
	response = requests.post( "https://apis.paralleldots.com/usage", params= { "api_key": api_key } ).text
	response = json.loads( response )
	return response