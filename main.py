import datetime
import scrape
import post_request
import test

user = 'ancestrai'
start = datetime.datetime(2016, 12, 1)  # year, month, day
end = datetime.datetime(2017, 1, 6)  # year, month, day
scrape.scrape(user, start, end)
post_request.get_metadata(user)
test.format(user)