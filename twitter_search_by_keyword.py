# references :joy:
# https://pypi.python.org/pypi/TwitterSearch/
# https://twittersearch.readthedocs.io/en/latest/advanced_usage_tso.html
# https://github.com/ckoepp/TwitterSearch/blob/master/docs/advanced_usage_ts.rst
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
# http://www.davidrschuler.com/python_twitter_streaming/
# https://stackoverflow.com/questions/2440147/how-to-check-the-existence-of-a-row-in-sqlite-with-python


from TwitterSearch import *
import time 
import sqlite3

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['foo', 'bar'],  or_operator=True)
    tso.set_language('en') # download English tweets only
    tso.set_include_entities(True) 

    # REPLACE WITH TOKEN VALUES
    ts = TwitterSearch(
        consumer_key = 'blablabla',
        consumer_secret = 'blablabla',
        access_token = 'blablabla',
        access_token_secret = 'blablabla'
     )
    
    sqlite_file = 'twitter_data.sqlite'

    ######## USE THIS PART FOR FIRST TIME ONLY TO CREATE TABLE ######################
    """
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    
    c.executescript('drop table if exists twitter_search_teszt_march20;')
    c.execute('''CREATE TABLE twitter_search_teszt_march20\
        (rowid INTEGER PRIMARY KEY, tweet_id integer, tweet_date text, tweet_text text,\
        retweets integer, tweet_lang text, user_screen text, user_followers integer,\
        user_location text, user_description text, user_favourites integer)''')

    conn.commit()
    """
    ##################################################################################
    
    def my_callback_closure(current_ts_instance): # accepts ONE argument: an instance of TwitterSearch
        queries, tweets_seen = current_ts_instance.get_statistics()
        if queries > 0 and (queries % 5) == 0: # trigger delay every 5th query
            print("sleeping")
            time.sleep(60) # sleep for 60 seconds

    # actual downloading
    count = 0
    for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()
        tw_id = tweet['id']
        

        # checking for already existing tweet
        c.execute("SELECT tweet_id FROM twitter_search_teszt_march20 WHERE tweet_id = ?", (tw_id,))
        data = c.fetchone()
        
        if data is None:
            print("dowloading tweet: ", tw_id)
            count += 1
            tw_text = tweet['text']
            tw_created_at = tweet['created_at']
            tw_retwets = tweet['retweet_count']
            tw_lang = tweet['lang']
            tw_user = tweet['user']['screen_name']
            tw_user_followers = tweet['user']['followers_count']
            tw_user_location = tweet['user']['location']
            tw_user_description = tweet['user']['description']
            tw_user_favourites  = tweet['user']['favourites_count']
            c.execute("INSERT INTO twitter_search_teszt_march20 (tweet_id, tweet_date, tweet_text,\
            retweets, tweet_lang, user_screen, user_followers, user_location, user_description, user_favourites) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (tw_id, tw_created_at, tw_text, tw_retwets, \
                tw_lang, tw_user, tw_user_followers, tw_user_location, tw_user_description, tw_user_favourites))
            conn.commit()
            conn.close()
        else:
            print("TWEET EXISTS")
            
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
