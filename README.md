# Backstory

I've recently completed a purchase of some digital goods on reddit.com. It turned out to be a scam, the seller stopped replying but still continued with his selling activities. Needless to say - I was quite angry and decided to pay him back. I rushed and made the script that is in front of you. Not that pretty but works.

Each time the scammer posts a new thread or a new comment, this script will reply with a custom message. It will warn others to steer clear and avoid purchasing anything from him. To avoid duplicate comments, each comment reply is stored in a json file.

# Installation

Install the required prerequisites with:


```shell
pip install -r requirements.txt
```

Create an app at https://www.reddit.com/prefs/apps and store the client ID and client secret. You'll be needing these shortly. Edit the annoy.py file and type in your username and password, client ID and client secret. Don't forget to enter the scammer's username. The script will create a json file that serves as a database, so type in the full path to the directory that will have this file. Give it a quick spin and see if a comment is posted.

When you're sure it's working, create a cronjob. In my case it looks like this:
```shell
*/10 * * * * python /home/peter/annoy.py
```

Reddit has a limit - one post each 10 minutes. This cronjob is run every 10 minutes to respect this limitation. Every 10 minutes the script will check for the latest posts and comments. If there a new post or comment exists, it will post a reply. You could increase the limit from 1 to a bigger number. The script will wait for 10 minutes before posting.
