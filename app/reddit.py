import json
import praw
from app.postsStruc import Submission

class Reddit():
    def __init__(self, authFile, rdonly):
        self.authInfo = self.getAuthDataFromFile(authFile)
        if rdonly:
            self.initRedditRDONLY()
        else:
            self.initReddit()

    def getAuthDataFromFile(self, filenName):
        with open(filenName, 'r') as readFile:
            return json.load(readFile)

    def initRedditRDONLY(self):
        self.praw = praw.Reddit(
                client_id = self.authInfo["client_id"],
                client_secret = self.authInfo["client_secret"],
                user_agent = self.authInfo["user_agent"]
        )
        print(self.praw)

    def initReddit(self):
        self.praw = praw.Reddit(
                client_id = self.authInfo["client_id"],
                client_secret = self.authInfo["client_secret"],
                user_agent = self.authInfo["user_agent"],
                username = self.authInfo["username"],
                password = self.authInfo["password"]
        )

    def getSubreddit(self,name):
        return self.praw.subreddit(name)

class Subreddit():
    def __init__(self, reddit, name):
        self.reddit = reddit
        self.name = name
        self.subreddit = reddit.getSubreddit(name)
        self.submissions = []

    def printHotSubmissions(self, NumPosts):
        print("Hottest post on " + self.name)
        for subID in self.subreddit.hot(limit=NumPosts):
            sub = Submission(self.reddit, subID)
            sub.printSubmission()
            self.submissions.append(sub)

