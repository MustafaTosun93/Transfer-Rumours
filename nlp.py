# -*- coding: utf-8 -*-
import tweepy
import csv
import urlparse

def getTweets(keyword):

    consumer_key = "D03K2PmhO19AqGZgMZyGJ6Ygq"
    consumer_secret = "bVLBNv7QyIr1PeUiuTxngL1Zwhm0wtqP8F5cKnwDrVhDBKc5oj"
    access_token = "145998559-7ue7ZzT8GOqpzUF2oBDzAG7i2VUaLXn7Jp3G1QPd"
    access_token_secret = "nwbFjULd4FpZz46Tm1wfusJUqru5vmiCvoHKScDgsjQov"
    callback_url = "https://github.com/MustafaTosun93/Transfer-Rumours"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)


    cleaned_Data1 = csv.writer(open("Cleaned_Data.csv", "wb"))
    pure_data1 = csv.writer(open("Pure_Data.csv", "wb"))
    search = tweepy.Cursor(api.search, q=keyword)

    for tweet in search.items():
        pure_data1.writerow([tweet.text.encode("utf8")])
        cleanedData = cleanData(tweet.text)
        cleaned_Data1.writerow([cleanedData.encode("utf8")])


        print cleanedData

def cleanData(string):

    new_string = ''
    for i in string.split():
        s, n, p, pa, q, f = urlparse.urlparse(i)
        if s and n:
           pass
        elif i[:1] == '@':
           pass
        elif i[:2] == 'RT' :
            pass
        elif i[:1] == '#':
            new_string = new_string.strip() + ' ' + i[1:]

        elif i[:1] == "'" :
            new_string = new_string.strip() + ' ' + i[1:]
        elif i[:1] == "\"" :
            new_string = new_string.strip() + ' ' + i[1:]


        else:
           new_string = new_string.strip() + ' ' + i
    return new_string



def process(text) :



        ptext = text.encode("utf8")
        return ptext






if __name__ == '__main__':
	getTweets('Transfer haberleri')