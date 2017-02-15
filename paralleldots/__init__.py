__all__= [ 'taxonomy', 'config', 'ner', 'similarity', 'sentiment', 'keywords' ]

from paralleldots.taxonomy import get_taxonomy as taxonomy
from paralleldots.ner import get_ner as ner
from paralleldots.similarity import get_similarity as similarity
from paralleldots.sentiment import get_sentiment as sentiment
from paralleldots.keywords import get_keywords as keywords
from paralleldots import config