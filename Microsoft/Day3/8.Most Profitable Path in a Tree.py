class Solution:
    def dfs1(self,edges,bob):
        dict1 = collections.defaultdict(set)

        for i,j in edges:
            dict1[i].add(j)
            dict1[j].add(i)

        parent_graph = collections.defaultdict(int)

        stack = [0]

        while stack:
            next_level = []

            for x in stack:
                for neighbor in dict1[x]:
                    if neighbor != parent_graph[x]:
                        parent_graph[neighbor] = x
                        next_level.append(neighbor)

            stack = next_level

        path = [bob]

        while path[-1] != 0:
            path.append(parent_graph[path[-1]])

        bob_path = {x:i for i,x in enumerate(path)}

        return bob_path

    def mostProfitablePath(self, edges, bob, amount):
        dict3 = collections.defaultdict(set)

        for i,j in edges:
            dict3[i].add(j)
            dict3[j].add(i)

        dict2 = self.dfs1(edges,bob)

        @lru_cache(None)
        def dfs(i,parent,current):
            bob_time = dict2.get(current,float("inf"))

            cur_amount = amount[current]

            if i == bob_time:
                cur_amount = cur_amount//2
            elif i > bob_time:
                cur_amount = 0

            result = [i for i in dict3[current] if i != parent]

            if not result:
                return cur_amount

            max_val = float("-inf")

            for j in result:
                max_val = max(max_val,cur_amount+dfs(i+1,current,j))

            return max_val

        return dfs(0,None,0)