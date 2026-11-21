class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Frequency counter created
        freq = {}

        # Step 2: Iterating over the input array
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 3: Sort by frequency of elements of dict values
        sorted_nums = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        # Step 4: Return first k elements
        return sorted_nums[:k]