import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        a = heapq.nsmallest(1,nums)
        return a[0]