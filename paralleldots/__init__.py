__all__= [ 'taxonomy', 'config', 'ner', 'similarity', 'sentiment', 'keywords', 'emotion', 'intent', 'multilang_sentiment', 'hit_count', 'specific_hit_count' ]

from paralleldots.taxonomy            import get_taxonomy            as taxonomy
from paralleldots.ner                 import get_ner                 as ner
from paralleldots.similarity          import get_similarity          as similarity
from paralleldots.sentiment           import get_sentiment           as sentiment
from paralleldots.keywords            import get_keywords            as keywords
from paralleldots.emotion             import get_emotion             as emotion
from paralleldots.intent              import get_intent              as intent
from paralleldots.multilang_sentiment import get_multilang_sentiment as multilang_sentiment
from paralleldots.hit_count           import get_hit_count           as hit_count
from paralleldots.specific_hit_count  import get_specific_hit_count  as specific_hit_count
from paralleldots.config              import set_api_key
from paralleldots.config              import get_api_key