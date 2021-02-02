from hn import HN

hn = HN()

# print the first 2 pages of newest stories
for story in hn.get_stories(story_type='newest', limit=60):
    print(story.rank, story.title)

# Select messages

