import praw
import datetime
import csv

now = datetime.datetime.now()
today = now.strftime("%a, %b %d, %Y")
title = ''
self = ''

path = 'schedule.csv'
with open(path, newline='') as sched:
    reader = csv.DictReader(sched)
    for row in reader:
        if today == row['Date']:
            title = '[PRE-GAME THREAD] ' + 'Washington Wizards ' + row['Home'] + ' ' + row['Opponent'] + ' | ' + row['Start']
            self = '    Pre-Game Thread v1.0\n\n' \
                   '[What do you want to see featured here?](https://www.reddit.com/message/compose/?to=Wizards-Bot)'


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit(
        'wizards-bot',
        user_agent="Wizards GDT bot v1.0")
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def main():
    reddit = authenticate()
    run_bot(reddit)


def run_bot(reddit):
    print("Posting thread...")
    submission = reddit.subreddit('washingtonwizards').submit(title, selftext=self)
    submission.mod.sticky(state=True, bottom=True)
    submission.mod.distinguish()


if __name__ == '__main__':
    main()