#!/usr/bin/python3
"""Count it!"""
from operator import itemgetter
import requests


def count_words(subreddit, word_list, hot_list=[], init=0, after="null"):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    agt = {"User-Agent": "linux:1:v2.1 (by /u/heimer_r)"}
    payload = {"limit": "100", "after": after}
    hot = requests.get(url, headers=agt, params=payload, allow_redirects=False)
    if hot.status_code == 200:
        posts = hot.json().get("data").get("children")
        hot_list += [post.get("data").get("title") for post in posts]
        after = hot.json().get("data").get("after")
        if after is not None:
            count_words(subreddit, word_list, hot_list, 1, after)
        if init == 0:
            hot_str = " ".join(hot_list)
            hot_words = hot_str.split(" ")
            word_list_low = sorted(word_list)
            reddit = []
            for word in word_list_low:
                num = len(
                    list(
                        filter(
                            lambda hot_w: hot_w.lower() == word.lower(), hot_words)))
                if num != 0:
                    reddit.append([word, num])
            if len(reddit) != 0:
                i = 0
                while i < len(reddit) - 1:
                    if reddit[i + 1][0] is not None and reddit[i][0] == reddit[i + 1][0]:
                        reddit[i][1] += reddit[i + 1][1]
                        reddit.pop(i + 1)
                        reddit.append([None, None])
                        i -= 1
                    i += 1
                r = list(filter(lambda x: x != [None, None], reddit))
                reddit_sorted = sorted(r, key=lambda x: (x[1]), reverse=True)
                for i in reddit_sorted:
                    print(*i, sep=": ")
