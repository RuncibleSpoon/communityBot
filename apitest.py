from psaw import PushshiftAPI

api = PushshiftAPI()
subred = 'checkmarx'

gen = api.search_submissions(subreddit=subred, q='lounge')
#results = list(gen)

for subm in gen:
     print(subm.title)
     print(subm.full_link)