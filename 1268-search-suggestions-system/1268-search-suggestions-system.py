import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""
        for char in searchWord:
            prefix += char  # prefix 일일이 인덱싱 X
            suggestions = []
            left = bisect.bisect_left(products, prefix) # bisect 활용 인덱싱
            for i in range(left, min(left + 3, len(products))):
                if products[i].startswith(prefix):  # startswith 함수
                    suggestions.append(products[i])
                else:
                    break
            result.append(suggestions)
        return result

