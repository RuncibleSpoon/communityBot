from psaw import PushshiftAPI

api = PushshiftAPI()
subred = 'checkmarx'
query_term = 'lounge'

# connect and query
gen = api.search_submissions(subreddit=subred, q=query_term)
#results = list(gen)

for subm in gen:
     print(subm.title)
     print(subm.full_link)