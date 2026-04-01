class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for word in strs:
            key = ''.join(sorted(word))

            if key not in store:
                store[key] = []
            
            store[key].append(word)
        
        result = list(store.values())
        return result

            

        
        