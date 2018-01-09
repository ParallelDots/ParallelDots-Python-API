__all__= [ "taxonomy", "config", "ner", "similarity", "sentiment", "keywords", "emotion", "intent", "multilang", "sentiment_social", "get_usage", "custom_classifier" ]

from paralleldots.taxonomy            import get_taxonomy            as taxonomy
from paralleldots.ner                 import get_ner                 as ner
from paralleldots.similarity          import get_similarity          as similarity
from paralleldots.sentiment           import get_sentiment           as sentiment
from paralleldots.sentiment_social    import get_sentiment_social    as sentiment_social
from paralleldots.keywords            import get_keywords            as keywords
from paralleldots.emotion             import get_emotion             as emotion
from paralleldots.intent              import get_intent              as intent
from paralleldots.multilang           import get_multilang           as multilang
from paralleldots.abuse               import get_abuse               as abuse
from paralleldots.custom_classifier   import get_custom_classifier   as custom_classifier

from paralleldots.usage               import get_usage               as usage

from paralleldots.config              import set_api_key
from paralleldots.config              import get_api_key