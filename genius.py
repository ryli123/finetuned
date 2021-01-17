import lyricsgenius
from nltk import tokenize
import requests
from pprint import pprint
import unicodedata


API_TOKEN = ''

subscription_key = ""
endpoint = ""
sentiment_url = endpoint + "/text/analytics/v3.0/sentiment"

def chunk(text):

    # tokenize into sentences
    s = tokenize.word_tokenize(text)

    # limits
    item_limit = 5000
    doc_limit = 5000

    # holder variables
    phrases = []
    cur = ""

    # combine into phrases
    for sent in s:
        if len(cur) + len(sent) <= item_limit:
            cur = cur + " " + sent
        else:
            phrases.append([cur, len(cur)])
            print(phrases)
            print('-----------------------------')
            cur = sent
    if cur != "":
        phrases.append([cur, len(cur)])

        
    print('-----------------------------')
    print(phrases)

    # combine into documents
    documents = []
    cur = []
    curL = 0
    for phr in phrases:
        print(phr[1]) # debug
        if curL + phr[1] < doc_limit:
            curL += phr[1]
            cur.append(phr[0])
            # print(cur)
        else:
            documents.append(cur)
            cur = []
            curL = 0
    if len(cur) > 0:
        documents.append(cur)
      
    #print('-----------------------------')
    #print(cur)
    #print(curL)
    #print(documents)

    # print(documents) # debug

    # make documents into json
    final_result = []
    doc = []
    cnt = 1
    for d in documents:
        for p in d:
            doc.append({
                "id": cnt,
                "language": "en",
                "text": p
            })
            cnt += 1
        final_result.append({"documents": doc})
        doc = []
        cnt = 1

    return final_result

def find_lyrics(title, artist):
    genius = lyricsgenius.Genius(API_TOKEN)

    song = genius.search_song(title, artist)
    print(type(song.lyrics))
    print(song.lyrics)

    return song.lyrics

def calc_sentiment(lyrics):
    text = lyrics.replace("\n", ", ")
    text = chunk(text)

    pprint(text)

    sentiments_list = []
    for index in range(len(text)):
        documents = text[index]

        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        response = requests.post(sentiment_url, headers=headers, json=documents)
        sentiments = response.json()

        pprint(sentiments)
        sentiments_list.append(sentiments)
    print ('---------------------------------------------------------------------------------------------------------')

    pos = 0
    neg = 0
    neutral = 0
    count = 0

    for obj in sentiments_list:
        document = obj['documents'][0]
        pos += document['confidenceScores']['positive']
        neutral += document['confidenceScores']['neutral']        
        neg += document['confidenceScores']['negative']
        count += 1

    pos /= count
    neg /= count
    neutral /= count

    print((pos, neg, neutral))
    return (pos, neutral, neg)

if __name__ == "__main__":
    lyrics = find_lyrics("Times Like These", "EDEN")
    print('==============================================================================')
    calc_sentiment(lyrics)