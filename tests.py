from paralleldots import set_api_key, get_api_key
from paralleldots import similarity, ner, taxonomy, sentiment, keywords, intent, emotion, abuse


def test():
    similarity( "Sachin is the greatest batsman", "Tendulkar is the finest cricketer" )
    sentiment( "Come on, lets play together" )
    taxonomy( "Narendra Modi is the prime minister of India" )
    ner( "Narendra Modi is the prime minister of India" )
    keywords( "Prime Minister Narendra Modi tweeted a link to the speech Human Resource Development Minister Smriti Irani made in the Lok Sabha during the debate on the ongoing JNU row and the suicide of Dalit scholar Rohith Vemula at the Hyderabad Central University." )
    emotion("Did you hear the latest Porcupine Tree song ? It's rocking !")
    intent("Finance ministry calls banks to discuss new facility to drain cash")
    abuse("you f**king a$$hole")

if __name__ == "__main__":
    test()
