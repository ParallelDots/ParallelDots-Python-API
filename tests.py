from paralleldots import set_api_key, get_api_key
from paralleldots import similarity, ner, sentiment, keywords, intent, emotion, abuse, batch_intent, batch_emotion, batch_abuse, batch_ner, batch_sentiment, batch_keywords,batch_phrase_extractor, set_api_key, taxonomy,phrase_extractor,sarcasm,batch_sarcasm,custom_classifier,multilang_keywords,batch_taxonomy,facial_emotion_url,object_recognizer_url,object_recognizer,facial_emotion,target_sentiment,batch_target_sentiment


def test():
    set_api_key("Put your Api key here")
    category  = { "finance": [ "markets", "economy", "shares" ], "world politics": [ "diplomacy", "UN", "war" ], "india": [ "congress", "india", "bjp" ] }
    print(similarity( "Sachin is the greatest batsman", "Tendulkar is the finest cricketer" ))
    print(sentiment( "Come on, lets play together" ))
    print(ner( "Narendra Modi is the prime minister of India" ))
    print(taxonomy("Michael Jordan of the Chicago Bulls is getting a 10-hour Netflix documentary in 2019"))
    print(keywords( "Prime Minister Narendra Modi tweeted a link to the speech Human Resource Development Minister Smriti Irani made in the Lok Sabha during the debate on the ongoing JNU row and the suicide of Dalit scholar Rohith Vemula at the Hyderabad Central University." ))
    print(phrase_extractor( "Prime Minister Narendra Modi tweeted a link to the speech Human Resource Development Minister Smriti Irani made in the Lok Sabha during the debate on the ongoing JNU row and the suicide of Dalit scholar Rohith Vemula at the Hyderabad Central University." ))
    print(emotion("Did you hear the latest Porcupine Tree song ? It's rocking !"))
    print(intent("Finance ministry calls banks to discuss new facility to drain cash"))
    print(abuse("you f**king a$$hole"))
    print(custom_classifier("Narendra Modi is the prime minister of India",category))
    print(batch_intent([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ]))
    print(batch_abuse([ "drugs are fun", "dont do drugs, stay in school"]))
    print(batch_sentiment([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ]))
    print(batch_phrase_extractor([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ]))
    print(batch_taxonomy(["Michael Jordan of the Chicago Bulls is getting a 10-hour Netflix documentary in 2019","Michael Jordan of the Chicago Bulls is getting a 10-hour Netflix documentary in 2019"]))
    print(batch_ner(["Michael Jordan of the Chicago Bulls is getting a 10-hour Netflix documentary in 2019","Michael Jordan of the Chicago Bulls is getting a 10-hour Netflix documentary in 2019"]))
    print(batch_emotion([ "drugs are fun", "don\'t do drugs, stay in school", "lol you a fag son", "I have a throat infection" ]))
    print(facial_emotion_url("https://i.imgur.com/klb812s.jpg"))
    print(object_recognizer_url("https://i.imgur.com/klb812s.jpg"))
    print(object_recognizer("test.jpg"))
    print(facial_emotion("test.jpg"))
    print(sarcasm("The movie that i watched last night is so funny that i get rolled out with laughter"))
    print(batch_sarcasm(["The movie that i watched last night is so funny that i get rolled out with laughter","I want to spend my life alone"]))

    





if __name__ == "__main__":
    test()
