class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res, count = [0] * len(spells), 0
        for spell_intensity in spells:
            for potion_intensity in potions:
                if spell_intensity * potion_intensity >= success:
                    res[count] += 1
            count += 1
        return res
