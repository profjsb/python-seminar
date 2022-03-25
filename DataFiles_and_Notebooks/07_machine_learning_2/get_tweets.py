import pandas as pd
import tweepy
import csv

import json
cred = json.load(open(".cred.json","r"))

consumer_key = cred["consumer_key"]
consumer_secret = cred["consumer_secret"]
access_token = cred["access_token"]
access_secret = cred["access_secret"]

def retrieve_tweets(input_file, output_file):
    
    """
    Takes an input filename/path of tweetIDs and outputs the full tweet data to a csv
    """
    
    # Authorization with Twitter
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_count=3, retry_delay=5, retry_errors=set([401, 404, 500, 503]))

    # Read input file

    df0 = pd.read_csv(input_file)
    df = df0.sample(len(df0))
    
    # Create output file

    csvFile = open(output_file, 'w')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["text",
                        "created_at",
                        "geo",
                        "lang",
                        "place",
                        "coordinates",
                        "user.favourites_count",
                        "user.statuses_count",
                        "user.description",
                        "user.location",
                        "user.id",
                        "user.created_at",
                        "user.verified",
                        "user.following",
                        "user.url",
                        "user.listed_count",
                        "user.followers_count",
                        "user.default_profile_image",
                        "user.utc_offset",
                        "user.friends_count",
                        "user.default_profile",
                        "user.name",
                        "user.lang",
                        "user.screen_name",
                        "user.geo_enabled",
                        "user.profile_background_color",
                        "user.profile_image_url",
                        "user.time_zone",
                        "id",
                        "favorite_count",
                        "retweeted",
                        "source",
                        "favorited",
                        "retweet_count"])
    
    # Append tweets to output file

    for tweetid in df.iloc[:,0]:

        csvFile = open(output_file, 'a')

        csvWriter = csv.writer(csvFile)

        try:
            status = api.get_status(tweetid)
            csvWriter.writerow([status.text,
                                status.created_at,
                                status.geo,
                                status.lang,
                                status.place,
                                status.coordinates,
                                status.user.favourites_count,
                                status.user.statuses_count,
                                status.user.description,
                                status.user.location,
                                status.user.id,
                                status.user.created_at,
                                status.user.verified,
                                status.user.following,
                                status.user.url,
                                status.user.listed_count,
                                status.user.followers_count,
                                status.user.default_profile_image,
                                status.user.utc_offset,
                                status.user.friends_count,
                                status.user.default_profile,
                                status.user.name,
                                status.user.lang,
                                status.user.screen_name,
                                status.user.geo_enabled,
                                status.user.profile_background_color,
                                status.user.profile_image_url,
                                status.user.time_zone,
                                status.id,
                                status.favorite_count,
                                status.retweeted,
                                status.source,
                                status.favorited,
                                status.retweet_count])
        except Exception as e:
            print(e)
            pass