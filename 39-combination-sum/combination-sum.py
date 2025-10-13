class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r = []
        candidates.sort()
        combos = [[num] for num in candidates if num <= target]
        for _ in range(target):  
            new_combos = []
            for comb in combos:
                s = sum(comb)
                if s == target:
                    sorted_comb = sorted(comb)
                    if sorted_comb not in r:
                        r.append(sorted_comb)
                elif s < target:
                    for num in candidates:
                        if s + num <= target:
                            new_combos.append(comb + [num])
            combos = new_combos
        return r