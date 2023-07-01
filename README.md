# YouTube-API
We will be working with YouTube API in this project.

---

# How to get a YouTube API key

Following the instruction in this link here --> [Fitzgerald, Anna. How to Get a YouTube API Key [Tutorial + Examples], blog.hubspot.com](https://blog.hubspot.com/website/how-to-get-youtube-api-key)

**Summary: How to get YouTube API key**
- You need Google Cloud or Google account, log in
- Go to [Google Developers Console](https://console.cloud.google.com/apis/dashboard) >> click create a new project >> click on new project (or it'll redirect to the new project automatically after you create it) 
- Drop down menu, find "APIs & Services",click "Enabled APIs & services"
- Go to "Library" >> find & select "YouTube Data API v3" (or other API you want to work with), click "Enable"
- On the right top corner, click "Create Credentials" >> fill in the info, click "Next", then you get your API key, click Done

**Remember: this is personal, sensitive information. Therefor, keep you API key safe!**


- In this link you'll find document about YouTube Data API --> [YouTube Data API Overview](https://developers.google.com/youtube/v3/getting-started) - Document about YouTube Data API 

## How much does the YouTube API Cost?
YouTube Data API costs are based on quota usage, and all requests will incur at least a 1-point quota cost. For each project, you’re allowed 10,000 free quota units per day. 
[Ref.](https://rapidapi.com/blog/how-to-get-youtube-api-key/)

---

# How to hide API key & personal info e.g. email address, password
- We still want to work with this sensitive information (API key) to access data 
- And we want to publish our script to the public but don't want this info to be exposed.
- We will use ```.env```, 
    - we can write all the sensitive info into this file, 
    - after then we can call the environment variables in this file anytime when we want to use the info

## Getting started, 
1. install ```dotenv``` using 

```
pip install python-dotenv
```

2. create ```.env ``` file in your working folder
3. Store API key (e.g. "API_KEY = your-api-key-here") in the ```.env ``` file 
4. In the python code, 

```
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
``` 

Watch tutorial 
- [Soma, Jonathan. Hide API keys in Python scripts using python-dotenv, .env, and .gitignore, youtube.com](https://www.youtube.com/watch?v=YdgIWTYQ69A)
- [GitGuardian, Store & manage secrets like API keys in Python - Tech Tip Tuesdays, youtube.com](https://www.youtube.com/watch?v=DVVYHlGYIHY)

## Another way
Another way to store key without .env by simply store key in a file and read the content in the file --> see code in the reference below 
- [dylburger, Keeping your API keys secret, github.com/dylburger](https://github.com/dylburger/reading-api-key-from-file/blob/master/Keeping%20API%20Keys%20Secret.ipynb)

---

# How to get YouTube Channel ID 
- If you have your own channel >> you can see your Channel ID on the search bar when you're inside the [studio page](studio.youtube.com)
- But if you want to find ID of other Channels that you want to work on
    - Go to the channel page >> go to "About" 
    - select the arrow sign (share button) 
    - select "Copy Channel ID" - there you'll have the ID to write in your code


---


## Reference:
- The whole tutorial that I followed >> [StrataScratch, Working with APIs in Python [For Your Data Science Project]](https://www.youtube.com/watch?v=fklHBWow8vE)



     

