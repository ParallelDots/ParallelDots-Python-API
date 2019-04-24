from paralleldots.config import get_api_key
import requests
import json

def get_sentiment( text, lang_code= "en" ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/sentiment", data= { "api_key": api_key, "text": text, "lang_code": lang_code } ).text
	response = json.loads( response )
	return response

def get_ner( text ,lang_code="en"):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/ner", data= { "api_key": api_key, "text": text, "lang_code": lang_code} ).text
	response = json.loads( response )
	return response

def get_keywords( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/keywords", data= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_sarcasm( text ,  lang_code= "en" ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/sarcasm", data= { "api_key": api_key, "text": text, "lang_code": lang_code} ).text
	response = json.loads( response )
	return response

def get_target_sentiment( text ,entity):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/target/sentiment", data= { "api_key": api_key, "text": text, "entity": entity} ).text
	response = json.loads( response )
	return response

def get_intent( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/intent", data= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_emotion( text, lang_code= "en" ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/emotion", data= { "api_key": api_key, "text": text, "lang_code": lang_code } ).text
	response = json.loads( response )
	return response

def get_abuse( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/abuse", data= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_taxonomy( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/taxonomy", data= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_similarity( text_1, text_2 ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/similarity", data= { "api_key": api_key, "text_1": text_1, "text_2": text_2 } ).text
	response = json.loads( response )
	return response

def get_custom_classifier( text, category ):
	api_key  = get_api_key()
	if type( category ) == dict:
		category = json.dumps( category )
	response = requests.post( "https://apis.paralleldots.com/v4/custom_classifier", data= { "api_key": api_key, "text": text, "category": category } ).text
	response = json.loads( response )
	return response

def get_phrase_extractor( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/phrase_extractor", data= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_language_detection( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/language_detection", data= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_text_parser( text ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/text_parser", data= { "api_key": api_key, "text": text } ).text
	response = json.loads( response )
	return response

def get_multilang_keywords( text, lang_code= "en" ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/multilang_keywords", data= { "api_key": api_key, "text": text, "lang_code": lang_code } ).text
	response = json.loads( response )
	return response

def get_popularity( path ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/popularity", data= { "api_key": api_key }, files= { "file": open( path, "rb" ).read() } ).text
	response = json.loads( response )
	return response

def get_nsfw( path ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/nsfw", data= { "api_key": api_key }, files= { "file": open( path, "rb" ).read() } ).text
	response = json.loads( response )
	return response

def get_facial_emotion( path ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/facial_emotion", data= { "api_key": api_key }, files= { "file": open( path, "rb" ).read() } ).text
	response = json.loads( response )
	return response

def get_object_recognizer( path ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/object_recognizer", data= { "api_key": api_key }, files= { "file": open( path, "rb" ).read() } ).text
	response = json.loads( response )
	return response

def get_popularity_url( url ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/popularity", data= { "api_key": api_key, "url": url } ).text
	response = json.loads( response )
	return response

def get_nsfw_url( url ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/nsfw", data= { "api_key": api_key, "url": url } ).text
	response = json.loads( response )
	return response

def get_facial_emotion_url( url ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/facial_emotion", data= { "api_key": api_key, "url": url } ).text
	response = json.loads( response )
	return response

def get_object_recognizer_url( url ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/object_recognizer", data= { "api_key": api_key, "url": url } ).text
	response = json.loads( response )
	return response

def get_usage():
	api_key  = get_api_key()
	if api_key == None or api_key == "":
		return { "Error": "API Key cannot be None or an empty String." }
	response = requests.post( "https://apis.paralleldots.com/usage", data= { "api_key": api_key } ).text
	response = json.loads( response )
	return response

def get_batch_intent( data ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/intent_batch", data= { "text": json.dumps( data ), "api_key": api_key } ).text
	response = json.loads( response )
	return response	

def get_batch_abuse( data ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/abuse_batch", data= { "text": json.dumps( data ), "api_key": api_key } ).text
	response = json.loads( response )
	return response


def get_batch_ner( data ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/ner_batch", data= { "text": json.dumps( data ), "api_key": api_key } ).text
	response = json.loads( response )
	return response


def get_batch_taxonomy( data ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/taxonomy_batch", data= { "text": json.dumps( data ), "api_key": api_key } ).text
	response = json.loads( response )
	return response	


def get_batch_language_detection( data ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/language_detection_batch", data= { "text": json.dumps( data ), "api_key": api_key } ).text
	response = json.loads( response )
	return response		


def get_batch_phrase_extractor( data ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/phrase_extractor_batch", data= { "text": json.dumps( data ), "api_key": api_key } ).text
	response = json.loads( response )
	return response


def get_batch_keywords( data ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/keywords_batch", data= { "text": json.dumps( data ), "api_key": api_key } ).text
	response = json.loads( response )
	return response

def get_batch_sentiment( data ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/sentiment_batch", data= { "text": json.dumps( data ), "api_key": api_key } ).text
	response = json.loads( response )
	return response


def get_batch_emotion( data ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/emotion_batch", data= { "text": json.dumps( data ), "api_key": api_key } ).text
	response = json.loads( response )
	return response

def get_batch_sarcasm( data ):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/sarcasm_batch", data= { "text": json.dumps( data ), "api_key": api_key } ).text
	response = json.loads( response )
	return response


def get_batch_target_sentiment( data ,entity):
	api_key  = get_api_key()
	response = requests.post( "https://apis.paralleldots.com/v4/target/sentiment_batch", data= { "text": json.dumps( data ), "api_key": api_key ,"entity":entity} ).text
	response = json.loads( response )
	return response