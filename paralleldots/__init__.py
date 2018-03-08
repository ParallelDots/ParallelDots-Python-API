__all__= [ "config", "get_usage", "taxonomy", "ner", "similarity", "sentiment", "keywords", "emotion", "intent", "abuse", "custom_classifier", "phrase_extractor", "text_parser", "multilang_keywords", "nsfw", "popularity" ]

from paralleldots.taxonomy            import get_taxonomy            as taxonomy
from paralleldots.ner                 import get_ner                 as ner
from paralleldots.similarity          import get_similarity          as similarity
from paralleldots.sentiment           import get_sentiment           as sentiment
from paralleldots.keywords            import get_keywords            as keywords
from paralleldots.emotion             import get_emotion             as emotion
from paralleldots.intent              import get_intent              as intent
from paralleldots.abuse               import get_abuse               as abuse
from paralleldots.custom_classifier   import get_custom_classifier   as custom_classifier
from paralleldots.phrase_extractor    import get_phrase_extractor    as phrase_extractor
from paralleldots.text_parser         import get_text_parser         as text_parser
from paralleldots.multilang_keywords  import get_multilang_keywords  as multilang_keywords
from paralleldots.nsfw                import get_nsfw                as nsfw
from paralleldots.popularity          import get_popularity          as popularity

from paralleldots.usage               import get_usage               as usage

from paralleldots.config              import set_api_key
from paralleldots.config              import get_api_key