ParallelDots-Python-API
=======================

A wrapper for the [ParallelDots API](http://www.paralleldots.com).

	
Installation
------------
From PyPI:

	pip install paralleldots


From Source:

	https://github.com/ParallelDots/ParallelDots-Python-API.git
	python setup.py install

API Keys & Setup
----------------
Signup and get your free API key from [ParallelDots](http://www.paralleldots.com/pricing).
You will receive a mail containing the API key at the registered email id.

Configuration:

	>>> from paralleldots import set_api_key, get_api_key

	# Setting your API key
	>>> set_api_key("YOUR API KEY")

	# Viewing your API key
	>>> get_api_key()

Supported APIs:
---------------

- [Semantic Similarity](https://tinyurl.com/k23nqs9)
- [Sentiment Analysis](https://tinyurl.com/km99mzb)
- Taxonomy
- [Named Entity Extraction/Recognition ( NER )](https://tinyurl.com/k9yglwc)
- [Keywords](https://tinyurl.com/kujcu8o)
- [Intent](https://tinyurl.com/n568bqw)
- [Emotion](http://blog.paralleldots.com/technology/deep-learning/emotion-detection-using-machine-learning/)
- Abuse
- Multiple Language Sentiment
	- Portuguese ( pt )
	- Chinese ( cn )
	- Spanish ( sp )
- Sentiment Social
- Usage

Examples
--------

	>>> from paralleldots import similarity, ner, taxonomy, sentiment, keywords, intent, emotion, multilang, abuse, sentiment_social

	>>> similarity( "Sachin is the greatest batsman", "Tendulkar is the finest cricketer" )
	{"actual_score": 0.842932,"normalized_score": 4.931469}

	>>> sentiment( "Come on, lets play together" )
	{"probabilities": {"positive": 0.00002,"neutral": 0.999954,"negative": 0.000026}}

	>>> taxonomy( "Narendra Modi is the prime minister of India" )
	{"tag": "terrorism", "confidence_score": 0.531435}, {"tag": "world politics", "confidence_score": 0.391963}, {"tag": "politics", "confidence_score": 0.358955}, {"tag": "religion", "confidence_score": 0.308195}, {"tag": "defense", "confidence_score": 0.26187}, {"tag": "business", "confidence_score": 0.20885}, {"tag": "entrepreneurship", "confidence_score": 0.18349}, {"tag": "health", "confidence_score": 0.171121}, {"tag": "technology", "confidence_score": 0.168591}, {"tag": "law", "confidence_score": 0.156953}, {"tag": "education", "confidence_score": 0.146511}, {"tag": "science", "confidence_score": 0.101002}, {"tag": "crime", "confidence_score": 0.085016}, {"tag": "entertainment", "confidence_score": 0.080634}, {"tag": "environment", "confidence_score": 0.078024}, {"tag": "disaster", "confidence_score": 0.075295}, {"tag": "weather", "confidence_score": 0.06784}, {"tag": "accident", "confidence_score": 0.066831}, {"tag": "sports", "confidence_score": 0.058329}, {"tag": "advertising", "confidence_score": 0.054868}, {"tag": "history", "confidence_score": 0.043581}, {"tag": "mining", "confidence_score": 0.03833}, {"tag": "travel", "confidence_score": 0.025517}, {"tag": "geography", "confidence_score": 0.022372}, {"tag": "nature", "confidence_score": 0.013477}, {"tag": "lifestyle", "confidence_score": 0.006467}, {"tag": "automobile", "confidence_score": 0.001161}, {"tag": "personal care", "confidence_score": 0.000275}]}

	>>> ner( "Narendra Modi is the prime minister of India" )
	{"entities": [
		{
			"category": "name",
			"name": "Narendra Modi",
			"confidence_score": 0.951439
		},
		{
			"category": "place",
			"name": "India",
			"confidence_score": 0.9263
		}
	]}

	>>> keywords( "Prime Minister Narendra Modi tweeted a link to the speech Human Resource Development Minister Smriti Irani made in the Lok Sabha during the debate on the ongoing JNU row and the suicide of Dalit scholar Rohith Vemula at the Hyderabad Central University." )
	[{"relevance_score": 4, "keyword": "Prime Minister Narendra Modi"}, {"relevance_score": 1, "keyword": "link"}, {"relevance_score": 3, "keyword": "speech Human Resource"}, {"relevance_score": 1, "keyword": "Smriti"}, {"relevance_score": 1, "keyword": "Lok"}]

	>>> emotion("Did you hear the latest Porcupine Tree song ? It's rocking !")
	{"emotion": "other", "probabilities": {"angry": 0.010629, "other": 0.453988, "sad": 0.028748, "excited": 0.2596, "happy": 0.247035}
	>>> intent("Finance ministry calls banks to discuss new facility to drain cash")
	{"probabilities": {"news": 0.946028, "other": 0.015853, "query": 0.000412, "feedback/opinion": 0.014115, "spam": 0.023591}}

	>>> multilang("Me encanta jugar al baloncesto", "es")
	{"sentiment": "positive", "confidence_score": 1.0}

	>>> abuse("you f**king a$$hole")
	{"sentence_type": "Abusive", "confidence_score": 0.953125}

	>>> sentiment_social("I left my camera at home")
	{"probabilities": {"positive": 0.040374, "neutral": 0.491032, "negative": 0.468594}}

	>>> usage()
	{
	"emotion": 100,
	"sentiment": 100,
	"similarity": 100,
	"taxonomy": 100,
	"abuse": 100,
	"intent": 100,
	"keywords": 100,
	"ner": 100,
	"multilang": 100,
	"sentiment_social": 100
	}