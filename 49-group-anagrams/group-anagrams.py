class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
           map = {}

           for s in strs:

               key = ''.join(sorted(s))

               if key not in map:
                  map[key] = []
            
               map[key].append(s)
    
           return list(map.values())

         