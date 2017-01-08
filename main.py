import datetime
import scrape
import post_request
import test

user = input('handle of user: ').lower()
year = int(input('year in which user started tweeting: '))
month = int(input('month in which user started tweeting(1-12): '))
start = datetime.datetime(year, month, 1)  # year, month, day
now = datetime.datetime.now()
end = datetime.datetime(now.year, now.month, now.day)  # year, month, day
"""scrape.scrape(user, start, end)"""
post_request.get_metadata(user)
maximum = int(input('how many tweets do you want to display(0 for all tweets, negative value indicates how many tweets you want to leave out): '))
mode = input('mode of sorting(\'retweets\', \'favs\' or \'sum\'(for sum of RTs and favs): ')
test.format(user, maximum=maximum, mode=mode)