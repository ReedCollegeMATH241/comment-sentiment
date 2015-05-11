import json
from hackernews_scraper import CommentScraper

#this script is hacky and was only meant for my own use

#one problem with it is that the amount of comments returned is non-deterministic
#this could be fixed by implementing a method take(), a la Haskell
#e.g. take(1000, result_of_scrape) to get the first 1000 comments since the ID supplied to the getComments call

#it could probably also be made neater by dumping all the JSON to one file
#but on a technical level, I didn't encounter any problems by having a file for each comment

def threedigits(x):
    '''Convenience function for readability of main method.
    Returns a number formatted to 3 digits.'''
    return '%(num)03d' % {"num":x}

def main():
    call = CommentScraper.getComments(since=9521155)
    
    res = [x for x in call]
    
    for i,r in enumerate(res):
        with open("comment" + threedigits(i) + ".json", mode="w") as f:
            json.dump(r, f)

