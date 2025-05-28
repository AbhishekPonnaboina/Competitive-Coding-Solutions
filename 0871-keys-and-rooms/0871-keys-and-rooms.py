class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        vis = set()
        
        while stack:
            idx = stack.pop()
            vis.add(idx)
            for key in rooms[idx]:
                if key not in vis:
                    stack.append(key)
        if len(vis) != len(rooms):
            return False
        return True