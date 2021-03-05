import json
import praw
from app.reddit import Reddit, Subreddit

def setup():
    auth = getAuthDataFromFile("authInfo.txt");
    reddit = praw.Reddit(
            client_id = auth["client_id"],
            client_secret = auth["client_secret"],
            user_agent = auth["user_agent"]
            )
    print(reddit.read_only)
    return reddit

def testprinthotposts(reddit, subreddit):
    print("Hottest post on " + subreddit)
    for submission in reddit.subreddit(subreddit).hot(limit=10):
        print(submission)

def getHotPosts(reddit, subreddit, NumPosts, labels):
    submissions = []
    for submission in reddit.subreddit(subreddit).hot(limit=NumPosts):
        submissions.append(submission)
    return submissions

if __name__ == "__main__":
    reddit = Reddit("app/authInfo.txt")
    subreddit = Subreddit(reddit.reddit, "wallstreetbets")
    print(subreddit)
    subreddit.printHotSubmissions(10);
    print(subreddit)
