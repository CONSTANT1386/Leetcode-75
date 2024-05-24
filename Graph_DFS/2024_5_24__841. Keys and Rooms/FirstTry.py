class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        record = [0]*n
        record[0] = 1
        def dfs(keys:List[int], r:List[int]):
            if keys:
                for key in keys:
                    if r[key] == 0:
                        r[key] = 1
                        dfs(rooms[key],r)
        dfs(rooms[0],record)
        if 0 in record: return False
        else: return True                   
