class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        record = [0]*n
        record[0] = 1
        queue = rooms[0]
        while queue:
            tmp = []
            for key in queue:
                if record[key] == 0:
                    record[key] = 1
                    for k in rooms[key]:
                        tmp.append(k)
            queue = tmp
        if 0 in record: return False
        else: return True                   
