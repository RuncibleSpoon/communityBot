from psaw import PushshiftAPI
from datetime import datetime, timedelta


days_to_subtract = 1

d = datetime.today() - timedelta(days=days_to_subtract)

api = PushshiftAPI()
subred = 'paloaltonetworks'
query_term = 'prisma'

# connect and query
gen = api.search_submissions(after=d, subreddit=subred, q=query_term,filter=['url','author', 'title', 'subreddit'], )
#results = list(gen)

for subm in gen:
     print(subm.title)
     print(subm.full_link)