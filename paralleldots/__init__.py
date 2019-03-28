__all__= [ "config", "usage", "taxonomy", "ner", "similarity", "sentiment", "keywords", "emotion", "intent", "abuse", "sarcasm", "target_sentiment","custom_classifier", "phrase_extractor", "text_parser", "multilang_keywords", "language_detection", "nsfw", "popularity", "object_recognizer", "facial_emotion", "nsfw_url", "popularity_url", "object_recognizer_url", "facial_emotion_url", "batch_intent", "batch_abuse", "batch_ner", "batch_taxonomy", "batch_keywords", "batch_sentiment", "batch_emotion", "batch_sarcasm", "batch_language_detection", "batch_target_sentiment", "batch_phrase_extractor" ]

from paralleldots.paralleldots_apis import get_taxonomy              as taxonomy
from paralleldots.paralleldots_apis import get_ner                   as ner
from paralleldots.paralleldots_apis import get_similarity            as similarity
from paralleldots.paralleldots_apis import get_sentiment             as sentiment
from paralleldots.paralleldots_apis import get_keywords              as keywords
from paralleldots.paralleldots_apis import get_emotion               as emotion
from paralleldots.paralleldots_apis import get_intent                as intent
from paralleldots.paralleldots_apis import get_abuse                 as abuse
from paralleldots.paralleldots_apis import get_sarcasm               as sarcasm
from paralleldots.paralleldots_apis import get_target_sentiment      as target_sentiment
from paralleldots.paralleldots_apis import get_custom_classifier     as custom_classifier
from paralleldots.paralleldots_apis import get_phrase_extractor      as phrase_extractor
from paralleldots.paralleldots_apis import get_text_parser           as text_parser
from paralleldots.paralleldots_apis import get_multilang_keywords    as multilang_keywords
from paralleldots.paralleldots_apis import get_language_detection    as language_detection

from paralleldots.paralleldots_apis import get_nsfw                  as nsfw
from paralleldots.paralleldots_apis import get_popularity            as popularity
from paralleldots.paralleldots_apis import get_object_recognizer     as object_recognizer
from paralleldots.paralleldots_apis import get_facial_emotion        as facial_emotion

from paralleldots.paralleldots_apis import get_nsfw_url              as nsfw_url
from paralleldots.paralleldots_apis import get_popularity_url        as popularity_url
from paralleldots.paralleldots_apis import get_object_recognizer_url as object_recognizer_url
from paralleldots.paralleldots_apis import get_facial_emotion_url    as facial_emotion_url

from paralleldots.paralleldots_apis import get_usage                    as usage

from paralleldots.paralleldots_apis import get_batch_intent             as batch_intent
from paralleldots.paralleldots_apis import get_batch_abuse    		    as batch_abuse
from paralleldots.paralleldots_apis import get_batch_ner    		    as batch_ner
from paralleldots.paralleldots_apis import get_batch_taxonomy    	    as batch_taxonomy
from paralleldots.paralleldots_apis import get_batch_language_detection as batch_language_detection
from paralleldots.paralleldots_apis import get_batch_phrase_extractor   as batch_phrase_extractor
from paralleldots.paralleldots_apis import get_batch_keywords    		as batch_keywords
from paralleldots.paralleldots_apis import get_batch_sentiment    		as batch_sentiment
from paralleldots.paralleldots_apis import get_batch_emotion    		as batch_emotion
from paralleldots.paralleldots_apis import get_batch_sarcasm    		as batch_sarcasm
from paralleldots.paralleldots_apis import get_batch_target_sentiment   as batch_target_sentiment

from paralleldots.config            import set_api_key
from paralleldots.config            import get_api_key