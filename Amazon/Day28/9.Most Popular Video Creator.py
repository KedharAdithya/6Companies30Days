class Solution:
    def mostPopularCreator(self, cts: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        creator_popularity = {}
        max_popularity = 0
        
        for i in range(len(cts)):
            creator = cts[i]
            video_id = ids[i]
            views_count = views[i]
            
            if creator not in creator_popularity:
                creator_popularity[creator] = [views_count, video_id, views_count]
            else:
                creator_popularity[creator][0] += views_count
                if views_count > creator_popularity[creator][2]:
                    creator_popularity[creator][1] = video_id
                    creator_popularity[creator][2] = views_count
                elif views_count == creator_popularity[creator][2]:
                    creator_popularity[creator][1] = min(creator_popularity[creator][1], video_id)
            
            max_popularity = max(max_popularity, creator_popularity[creator][0])
        
        most_popular_creators = []
        for creator in creator_popularity:
            if creator_popularity[creator][0] == max_popularity:
                most_popular_creators.append([creator, creator_popularity[creator][1]])
        
        return most_popular_creators