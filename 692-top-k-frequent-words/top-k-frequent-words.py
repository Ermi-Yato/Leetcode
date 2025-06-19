class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)
        result = []
        def sort_key(item):
            word, freq = item
            return (-freq, word)
        
        items = word_count.items()
        sorted_items = sorted(items, key=sort_key)
        for item in sorted_items[:k]:
            result.append(item[0])
        return result

