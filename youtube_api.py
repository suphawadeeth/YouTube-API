# import libraries 
import requests
import pandas as pd
import time 
from dotenv import load_dotenv
import os
load_dotenv() # get environment variables in the .env file to use when called 

# Setup environmant
API_KEY = os.getenv("API_KEY") # I stored key in the .env as API_KEY=xxxxxx
CHANNEL_ID = "UC176GAQozKKjhz62H8u9vQQ"


def get_video_stats(video_id):
    """
    This function take a video_id as an argument & return video stats
    e.g. view, like, favorite, and comment counts
    """

    url_video_stats = "https://www.googleapis.com/youtube/v3/videos?id=" + video_id + "&part=statistics&key=" + API_KEY
    response_video_stats = requests.get(url_video_stats).json()
        
    view_count = response_video_stats['items'][0]['statistics']['viewCount']
    like_count = response_video_stats['items'][0]['statistics']['likeCount']
    favorite_count = response_video_stats['items'][0]['statistics']['favoriteCount']
    comment_count = response_video_stats['items'][0]['statistics']['commentCount']
    
    return view_count, like_count, favorite_count, comment_count


def get_videos(df):
    """
    This function will make 2 API calls 
        1. Return json object, then the video id, title, publish_date will be collected
        2. 2nd API call, will return the video stats (from function above) return
            - view, like, favorite, 6 comment counts
    """

    ### Set url
    # pageToken = ""
    url = "https://www.googleapis.com/youtube/v3/search?key=" + API_KEY + "&channelId=" + CHANNEL_ID + "&part=snippet,id&order=date&maxResults=100"

    # Make API call & store the json into the "response" object
    response = requests.get(url).json() # return as a json object
    time.sleep(5)

    for video in response['items']:
        # Specify that we want to pick only the youtube video (not ads)
        if video['id']['kind'] == "youtube#video":  
            video_id = video['id']['videoId']
            video_title = video['snippet']['title']
            publish_date = video['snippet']['publishTime']
            publish_date = publish_date.split("T")[0]

            # calling the get_video_stats() function to get all stats & append into the df
            view_count, like_count, favorite_count, comment_count = get_video_stats(video_id)

            df = df.append({'video_id': video_id, 
                            'video_title': video_title,
                            'publish_date': publish_date,
                            'view_count': view_count,
                            'like_count': like_count,
                            'comment_count': comment_count}, ignore_index=True)             
    return df 



# Create an empty dataframe
df = pd.DataFrame(columns = ['video_id', 'video_title', 'publish_date', 
                             'view_count', 'like_count', 'favorite_count', 'comment_count'])

# Call the function
df = get_videos(df)
