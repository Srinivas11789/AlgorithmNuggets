class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        # Hacky Quick Python Method
        
        # Use Collections Counter to get a dictionay of word count
        import collections
        record = collections.Counter(words)
        
        # Another dictionary to store the most frequent elements
        freqs = {}
        
        # Iterate through the dictionary for frequency and sort them by 
        for word, freq in record.items():
                if freq not in freqs:
                    freqs[freq] = []
                freqs[freq].append(word)
        
        result = []
        maxi = max(freqs.keys())
        for i in range(maxi, 0, -1):
            if i in freqs:
                result.extend(sorted(freqs[i]))
            if len(result) == k:
                return result
            elif len(result) > k:
                return result[:k]
