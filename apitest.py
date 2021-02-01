from psaw import PushshiftAPI
from datetime import datetime, timedelta


days_to_subtract = 1

d = datetime.today() - timedelta(days=days_to_subtract)

api = PushshiftAPI()
subred = 'paloaltonetworks'
query_term = 'prisma'

# connect and query
gen = api.search_submissions(subreddit=subred, q=query_term,filter=['full_link','author', 'title', 'subreddit'], after=d)
#results = list(gen)

for subm in gen:
     print(subm.title)
     print(subm.full_link)