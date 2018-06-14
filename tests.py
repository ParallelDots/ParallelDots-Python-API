from paralleldots import set_api_key, get_api_key
from paralleldots import similarity, ner, taxonomy, sentiment, keywords, intent, emotion, abuse, batch_intent, batch_emotion, batch_abuse, batch_ner, batch_sentiment, batch_keywords, batch_taxonomy, batch_phrase_extractor, batch_language_detection


def test():
    set_api_key("write your api key here")
    similarity( "Sachin is the greatest batsman", "Tendulkar is the finest cricketer" )
    sentiment( "Come on, lets play together" )
    taxonomy( "Narendra Modi is the prime minister of India" )
    ner( "Narendra Modi is the prime minister of India" )
    keywords( "Prime Minister Narendra Modi tweeted a link to the speech Human Resource Development Minister Smriti Irani made in the Lok Sabha during the debate on the ongoing JNU row and the suicide of Dalit scholar Rohith Vemula at the Hyderabad Central University." )
    emotion("Did you hear the latest Porcupine Tree song ? It's rocking !")
    intent("Finance ministry calls banks to discuss new facility to drain cash")
    abuse("you f**king a$$hole")
    batch_intent([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ])
    batch_abuse([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ])
    batch_ner([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ])
    batch_emotion([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ])
    batch_sentiment([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ])
    batch_keywords([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ])
    batch_phrase_extractor([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ])
    batch_language_detection([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ])
    batch_taxonomy([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ])





if __name__ == "__main__":
    test()
