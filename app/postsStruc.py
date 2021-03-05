class Comment():
    def __init__(self, comment):
        self.comment = comment

    def printComment(self):
        print(self.comment)

class Submission():
    def __init__(self, reddit, postID):
        self.submissionID = postID
        self.submission = reddit.submission(id=postID)
        self.title = self.submission.title
        self.comments = []

    def getTopComments(self):
        self.comments = list(self.submission.comments)

    def printSubmission(self):
        getTopComments()
        print(self.title)
        print(self.comments)

