from psaw import PushshiftAPI

api = PushshiftAPI()
subred = checkmarx

gen = api.search_submissions(subreddit=subred, q='lounge')
results = list(gen)
print(results)