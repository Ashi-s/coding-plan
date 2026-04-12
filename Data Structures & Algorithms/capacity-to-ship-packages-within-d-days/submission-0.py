class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        output = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            days_count = 1
            weight_count = 0

            for w in weights:
                if weight_count + w > mid:
                    days_count += 1
                    weight_count = 0
                weight_count += w
            
            if days_count <= days:
                right = mid - 1
            else:
                left = mid + 1
        
        return left