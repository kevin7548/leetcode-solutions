class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        for l in range(1, len(searchWord)+1):
            prefix = searchWord[:l]   # 길이 l
            ls = []
            for p in products:
                if p[:l] == prefix:
                    ls.append(p)
                if len(ls) == 3:
                    break
            result.append(ls)
        return result

