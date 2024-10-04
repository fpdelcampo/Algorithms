class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s = skill[0] + skill[-1]
        chemistry = 0
        for i in range(len(skill) // 2):
            chemistry += skill[i] * skill[len(skill) - i - 1]
            if skill[i] + skill[len(skill) - i - 1] != skill[0] + skill[-1]:
                return -1
        return chemistry