import praw
import time
reddit = praw.Reddit(
    client_id="yours",
    client_secret="yours",
    user_agent="yours",
)

ms = 0
cr = 0
start = time.time()
subreddit = reddit.subreddit("soccer")
for submission in subreddit.top(limit=10000):
    for comment in submission.comments.list():
        if hasattr (comment, "body"):
            comment_lower = comment.body.lower()
            if ("messi" in comment_lower and "goat" in comment_lower):
                 ms += 1
                 print("messi")
                 print(ms)
            if ("ronaldo" in comment_lower and "goat" in comment_lower):
                cr += 1
                print("ronaldo")
                print(cr)
end = time.time()
print("time it took" )
print(end - start)
print("ronaldo")
print(cr)
print("messi")
print(ms)

