from collections import defaultdict
def groupAnagrams(strs: list[str]) ->list[list[str]]:
        dict = defaultdict(list)


        for i in strs:
            S = [x for x in i]
            S.sort()
            S = tuple(S)
            dict[S].append(i)
        return list(dict.values())

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(groupAnagrams(["x"]))