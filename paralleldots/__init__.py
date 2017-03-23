__all__= [ 'taxonomy', 'config', 'ner', 'similarity', 'sentiment', 'keywords' ]

from paralleldots.taxonomy            import get_taxonomy            as taxonomy
from paralleldots.ner                 import get_ner                 as ner
from paralleldots.similarity          import get_similarity          as similarity
from paralleldots.sentiment           import get_sentiment           as sentiment
from paralleldots.keywords            import get_keywords            as keywords
from paralleldots.emotion             import get_emotion             as emotion
from paralleldots.intent              import get_intent              as intent
from paralleldots.multilang_sentiment import get_multilang_sentiment as multilang_sentiment
from paralleldots.config              import set_api_key