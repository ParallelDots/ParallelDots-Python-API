ParallelDots-Python-API
=======================

A wrapper for the [ParallelDots APIs](http://www.paralleldots.com).

Build Status: [![CircleCI](https://circleci.com/gh/ParallelDots/ParallelDots-Python-API.svg?style=svg)](https://circleci.com/gh/ParallelDots/ParallelDots-Python-API)

Installation
------------
From PyPI:

	pip install paralleldots


From Source:

	https://github.com/ParallelDots/ParallelDots-Python-API.git
	python setup.py install

API Keys & Setup
----------------
Sign up to create your free account from [ParallelDots](https://www.paralleldots.com/sign-up).
[Log in](https://user.apis.paralleldots.com/login) to your account to get your API key.

Configuration:

	>>>>> import paralleldots

	# Setting your API key
	>>>>> paralleldots.set_api_key( "YOUR API KEY" )

	# Viewing your API key
	>>>>> paralleldots.get_api_key()

Languages Supported:
-------------------

- Portuguese ( pt )
- Simplified Chinese ( Not available in multilingual keyword generator API ) ( zh )
- Spanish ( es )
- German ( de )
- French ( fr )
- Dutch ( nl )
- Italian ( it )
- Japanese ( ja )
- Thai ( th )
- Danish ( da )
- Finnish ( fi )
- Greek ( el )
- Russian ( ru )
- Arabic ( ar )

Supported APIs:
---------------

- Abuse
- Custom Classifier
- Emotion
- Sarcasm
- Facial Emotion
- Intent
- Keywords
- Multilanguage Keywords ( Supports Multiple Languages )
- Named Entity Extraction/Recognition ( NER )
- Not Safe For Work ( NSFW Image Classifier )
- Phrase Extractor
- Popularity ( Image Classifier )
- Object Recognizer
- Sentiment Analysis
- Target Sentiment Analysis
- Semantic Similarity
- Taxonomy
- Text Parser
- Usage

Examples
--------

	>>> import paralleldots

	>>> api_key   = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	>>> text      = "Chipotle in the north of Chicago is a nice outlet. I went to this place for their famous burritos but fell in love with their healthy avocado salads. Our server Jessica was very helpful. Will pop in again soon!"
	>>> path      = "/path/to/image.jpg"
	>>> lang_code = "fr"
	>>> aspect    = "food"
	>>> lang_text = "C'est un environnement très hostile, si vous choisissez de débattre ici, vous serez vicieusement attaqué par l'opposition."
	>>> category  = [ "travel","food","shopping", "market" ]
	>>> url       = "http://i.imgur.com/klb812s.jpg"
	>>> data      =  [ "I like walking in the park", "Don't repeat the same thing over and over!", "This new Liverpool team is not bad", "I have a throat infection" ]


	>>> paralleldots.set_api_key( api_key )
	>>> print( "API Key: %s" % paralleldots.get_api_key() )

	>>> print( "\nAbuse" )
	>>> paralleldots.abuse( text )
	

	>>> print( "\nBatch Abuse" )
	>>> paralleldots.batch_abuse( data )
	

	>>> print( "\nCustom Classifier" )
	>>> paralleldots.custom_classifier( text, category )

	>>> print( "\nEmotion" )
	>>> paralleldots.emotion( text )

	>>> print( "\nBatch Emotion" )
	>>> paralleldots.batch_emotion( data )
	

	>>> print( "\nEmotion - Lang: Fr". )
	>>> paralleldots.emotion( lang_text, lang_code )
	

	>>> print( "\nSarcasm - Lang: Fr" )
	>>> paralleldots.sarcasm( lang_text,lang_code )


	>>> print( "\nSarcasm" )
	>>> paralleldots.sarcasm( text)
	

	>>> print( "\nBatch Sarcasm" )
	>>> paralleldots.batch_sarcasm( data )
	

	>>> print( "\nFacial Emotion" )
	>>> paralleldots.facial_emotion( path )

	>>> print( "\nFacial Emotion: URL Method" )
	>>> paralleldots.facial_emotion_url( url )

	>>> print( "\nIntent" )
	>>> paralleldots.intent( text )

	>>> print( "\nBatch Intent" )
	>>> paralleldots.batch_intent( data )

	>>> print( "\nKeywords" )
	>>> paralleldots.keywords( text )

	>>> print( "\nBatch Keywords" )
	>>> paralleldots.batch_keywords( data )
	
	>>> print( "\nLanguage Detection" )
	>>> paralleldots.language_detection( lang_text )
	

	>>> print( "\nBatch Language Detection" )
	>>> paralleldots.batch_language_detection( data )
	

	>>> print( "\nMultilang Keywords - Lang: fr". )
	>>> paralleldots.multilang_keywords( lang_text, lang_code )
	
	>>> print( "\nNER" )
	>>> paralleldots.ner( text )

	>>> print( "\nNER - Lang: es" )
	>>> paralleldots.ner( "Lionel Andrés Messi vuelve a ser el gran protagonista en las portadas de la prensa deportiva internacional al día siguiente de un partido de Champions.","es" )


	>>> print( "\nBatch NER" )
	>>> paralleldots.batch_ner( data ) 
	


	>>> print( "\nObject Recognizer" )
	>>> paralleldots.object_recognizer( path )
	

	>>> print( "\nObject Recognizer: URL Method" )
	>>> paralleldots.object_recognizer_url( url )
	

	>>> print( "\nPhrase Extractor" )
	>>> paralleldots.phrase_extractor( text ) 
	

	>>> print( "\nBatch Phrase Extractor" )
	>>> paralleldots.batch_phrase_extractor( data )


	>>> print( "\nSentiment" )
	>>> paralleldots.sentiment( text )
	
	>>> print( "\nTarget Sentiment" )
	>>> paralleldots.target_sentiment( text, aspect )

	>>> print( "\nBatch Sentiment" )
	>>> paralleldots.batch_sentiment( data )
	

	>>> print( "\nSentiment - Lang: Fr". )
	>>> paralleldots.sentiment( lang_text, lang_code ) 
	

	>>> print( "\nSimilarity" )
	>>> paralleldots.similarity( "I love fish and ice cream!", "fish and ice cream are the best!" )
	

	>>> print( "\nTaxonomy" )
	>>> paralleldots.taxonomy( text ) 
	

	>>> print( "\nBatch Taxonomy" )
	>>> paralleldots.batch_taxonomy( data )

	
	>>> paralleldots.usage()
