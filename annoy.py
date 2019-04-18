import praw
from tinydb import TinyDB, Query
import time

CLIENT_ID=''
CLIENT_SECRET=''
USERNAME=''
PASSWORD=''

SCAMMER_USERNAME=''

reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     password=PASSWORD, user_agent='USERAGENT',
                     username=USERNAME)


db = TinyDB('database.json') #enter full path where json file will be stored

user = reddit.redditor(SCAMMER_USERNAME)

comments=Query()

for comment in user.comments.new(limit=1):
	#have we already commented on this post?
	if(db.search(comments.title==comment.body)):
		continue

	time.sleep(600) #who doesn't like a nap?
	db.insert({'title':comment.body})
	comment.reply("Just a heads up - this user is a scammer. Several people have already been scammed, do not fall for this scam!")

for post in user.submissions.new(limit=1):
	#have we already commented on this post?
	if(db.search(comments.posts==post.title)):
		continue
	
	time.sleep(600) #lets sleep a bit more
	db.insert({'posts':post.title})
	post.reply("Please do not buy from this seller. He is a known scammer, do not waste your money!")
