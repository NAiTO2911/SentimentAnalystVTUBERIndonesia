#!/usr/bin/python
#validasi API Key dari Twitter melalui Tweepy
import tweepy
import csv #Import csv
consumerKey = 'FiaNpTfpS4VjSl3kdMlGAXOE6'
consumerSecret = 'cbrZ3Q1nBSS9jDXdypAqyxyUYMxiuCwR4I3sKFeJDlEhOyoLjB'
accessToken = '922327679344320512-rfAkdSYxvdvT3QoHagMeoNY09qSLmcC'
accessTokenSecret = 'kKdl5arR7xsJvBP0xYz1Jl0TMKwwUpxFrpO4k1BDmbXdh'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('datacrawlin2.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search_tweets,
                           q = "#Vtuber -filter:retweets",
                           lang = "id").items():
                           

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()