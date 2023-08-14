class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Leveraging quick_select (kth smallest/largest in unordered list)

        def find_largest_k(nums, k):

            # select any pivot
            pivot = nums[0]

            greater = []
            smaller = []
            equal = []

            for i in range(len(nums)):
                if nums[i] > pivot:
                    greater.append(nums[i])
                elif nums[i] < pivot:
                    smaller.append(nums[i])
                else:
                    equal.append(nums[i])
                
            if k <= len(greater):
                return find_largest_k(greater, k)

            if len(greater) + len(equal) < k:
                return find_largest_k(smaller, k - len(greater) - len(equal))

            return pivot

        def find_smaller_k(nums, k):

            # select any pivot
            pivot = nums[0]

            greater = []
            smaller = []
            equal = []

            for i in range(len(nums)):
                if nums[i] > pivot:
                    greater.append(nums[i])
                elif nums[i] < pivot:
                    smaller.append(nums[i])
                else:
                    equal.append(nums[i])
                
            if k <= len(smaller):
                return find_smaller_k(smaller, k)

            if len(smaller) + len(equal) < k:
                return find_smaller_k(greater, k - len(smaller) - len(equal))

            return pivot

        print(find_smaller_k(nums, k))
        return find_largest_k(nums, k)
