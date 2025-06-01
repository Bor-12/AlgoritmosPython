from collections import defaultdict
from typing import List
def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)

    for palabra in strs:
        clave = tuple(sorted(palabra))
        anagrams[clave].append(palabra)

    return list(anagrams.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))