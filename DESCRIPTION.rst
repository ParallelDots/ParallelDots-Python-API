ParallelDots-Python-API
=======================

A wrapper for the `ParallelDots API <http://www.paralleldots.com>`__.

.. image:: https://badge.fury.io/py/paralleldots.png
    :target: http://badge.fury.io/py/paralleldots
.. image:: https://travis-ci.org/ParallelDots/ParallelDots-Python-API.svg?branch=master
    :target: https://travis-ci.org/ParallelDots/ParallelDots-Python-API
    
Installation
------------
From PyPI:

.. code:: bash
	
	pip install paralleldots


From source:

.. code:: bash

	https://github.com/ParallelDots/ParallelDots-Python-API.git
	python setup.py install

API Keys + Setup
----------------
Signup and get your free API key from  `ParallelDots <http://www.paralleldots.com/pricing>`__.
You will receive a mail containing the API key at the registered email id.

Configuration:

.. code:: python

	>>> from paralleldots import config

	# Setting your API key
	>>> config.set_api_key("YOUR API KEY")

	# Viewing your API key
	>>> config.get_api_key()



Supported APIs:
---------------

- Semantic Proximity
- Sentiment Analysis
- Taxonomy
- Entity Extraction
- Keywords

Examples
--------

.. code:: python

	>>> from paralleldots import similarity, ner, taxonomy, sentiment, keywords

	>>> similarity( "Sachin is the greatest batsman", "Tendulkar is the finest cricketer" )
	{"actual": 0.79401779353226476, "similarity": 4.8781727384640341}

	>>> sentiment( "Come on, lets play together" )
	{"sentiment": 0.7375614089809589}

	>>> taxonomy( "Narendra Modi is the prime minister of India" )
	{"credits": "ParallelDots", "tags": [["finance", 1], ["business", 0], ["government", 0]]}

	>>> ner( "Narendra Modi is the prime minister of India" )
	{"entities": ["narendra modi", "india"]}

	>>> keywords( "Prime Minister Narendra Modi tweeted a link to the speech Human Resource Development Minister Smriti Irani made in the Lok Sabha during the debate on the ongoing JNU row and the suicide of Dalit scholar Rohith Vemula at the Hyderabad Central University." )
	{'keywords': [[u'Human Resource Development Minister Smriti Irani', 6], [u'Prime Minister Narendra Modi', 4], [u'Hyderabad Central University', 3], [u'ongoing JNU row', 3], [u'Dalit scholar', 2], [u'Lok Sabha', 2], [u'Rohith Vemula', 2]]}