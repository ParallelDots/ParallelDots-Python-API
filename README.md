ParallelDots-Python-API
===============

A wrapper for the [ParallelDots API](http://www.paralleldots.com).


Installation
------------
From PyPI:
```bash
pip install paralleldots
```

From source:
```bash
https://github.com/ParallelDots/ParallelDots-Python-API.git
python setup.py install
```

API Keys + Setup
----------------
Signup and get your free API key from [ParallelDots](http://www.paralleldots.com/developers/signup).
You will receive a mail containing the API key at the registered email id.

Configuration:
```python
>>> from paralleldots import config

	#Setting your API key
>>> config.set_api_key("YOUR API KEY")

	#Viewing your API key
>>> config.get_api_key()
```



Supported APIs:
------------

- Semantic Proximity
- Sentiment Analysis
- Taxonomy
- Entity Extraction

Examples
--------
```python
>>> from paralleldots import similarity, ner, taxonomy, sentiment

>>> similarity('Sachin is the greatest batsman', 'Tendulkar is the finest cricketer')
{"actual": 0.79401779353226476, "similarity": 4.8781727384640341}

>>> sentiment('Come on, lets play together')
{"sentiment": 0.7375614089809589}

>>> taxonomy('Narendra Modi is the prime minister of India')
{"credits": "ParallelDots", "tags": [["finance", 1], ["business", 0], ["government", 0]]}

>>> ner("Narendra Modi is the prime minister of India")
{"entities": ["narendra modi", "india"]}
```
