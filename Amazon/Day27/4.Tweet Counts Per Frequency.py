from typing import List
class TweetCounts:
    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets:
            self.tweets[tweetName] = []
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.tweets:
            return []
        if freq == "minute":
            interval = 60
        elif freq == "hour":
            interval = 3600
        elif freq == "day":
            interval = 86400
        else:
            return []
        res = []
        i = startTime
        while i <= endTime:
            j = min(i + interval, endTime + 1)
            res.append(sum(i <= t < j for t in self.tweets[tweetName]))
            i = j
        return res
