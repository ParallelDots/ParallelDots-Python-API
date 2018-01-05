from paralleldots import similarity, ner, taxonomy, sentiment, keywords, intent, emotion, multilang, abuse, sentiment_social


def test():
    print similarity("Sachin is the greatest batsman", "Tendulkar is the finest cricketer")


if __name__ == "__main__":
    test()
