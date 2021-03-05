import json
import praw
from app.reddit import Reddit, Subreddit

if __name__ == "__main__":
    reddit = Reddit("app/authInfo.txt", True)
    subreddit = Subreddit(reddit, "wallstreetbets")
    print(subreddit)
    subreddit.printHotSubmissions(10);
    print(subreddit)
