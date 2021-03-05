import json
import praw
from app.postsStruc import Submission

class Reddit():
    def __init__(self, authFile):
        self.authInfo = self.getAuthDataFromFile(authFile)
        self.reddit = self.initRedditRDONLY()

    def getAuthDataFromFile(self, filenName):
        with open(filenName, 'r') as readFile:
            return json.load(readFile)

    def initRedditRDONLY(self):
        self.reddit = praw.Reddit(
                client_id = self.authInfo["client_id"],
                client_secret = self.authInfo["client_secret"],
                user_agent = self.authInfo["user_agent"]
        )
        print(self.reddit)

    def initReddit(self):
        self.reddit = praw.Reddit(
                client_id = self.authInfo["client_id"],
                client_secret = self.authInfo["client_secret"],
                user_agent = self.authInfo["user_agent"],
                username = self.authInfo["username"],
                password = self.authInfo["password"]
        )

class Subreddit():
    def __init__(self, reddit, name):
        self.reddit = reddit
        self.name = name
        self.subreddit = reddit.subreddit(name)
        self.submissions = []

    def printHotSubmissions(self, NumPosts):
        print("Hottest post on " + self.name)
        for subID in self.subreddit.hot(limit=NumPosts):
            sub = Submission(self.reddit, subID)
            sub.printSubmission()
            self.submission.appand(sub)

