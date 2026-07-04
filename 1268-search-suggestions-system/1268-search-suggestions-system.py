import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        prefix = ""
        result = []
        for char in searchWord:
            prefix += char
            suggestions = []
            idx = bisect.bisect_left(products, prefix)
            for i in range(idx, min(idx+3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
            result.append(suggestions)
        return result

