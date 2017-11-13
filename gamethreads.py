#This script posts Game Threads an hour before gametime

import praw
import datetime
import csv
import time

now = datetime.datetime.now()
today = now.strftime("%a, %b %d, %Y")
title = ''
self = ''
currentHour = int(datetime.datetime.now().strftime("%H"))+2

#Open Wizards schedule and check to see if there is a game today. If so, post a pre-game thread
path = 'schedule.csv'
with open(path, newline='') as sched:
    reader = csv.DictReader(sched)
    for row in reader:
        if today == row['Date']:
            getStartTime = row['Start'].split()[0]
            startHour = int((list(getStartTime)[0]))+12
            while startHour-1 != currentHour:
                print("Still checking")
                time.sleep(3600)
            title = '[GAME THREAD] ' + 'Washington Wizards ' + row['Home'] + ' ' + row['Opponent'] + ' | ' + \
                    row['Start'] + " | NBC Sports"
            self = '    Game Thread v1.0\n\n' \
                    '[What do you want to see featured here going forward?](https://www.reddit.com/message/compose/?to=Wizards-Bot)'


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