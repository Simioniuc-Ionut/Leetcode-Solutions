

def subsets(nums: list[int]) -> list[list[int]]:
    set_sol = []
    back(0, nums, [], set_sol)
    return set_sol


def back(start, nums, sub_set, set_sol):
    set_sol.append(list(sub_set))
    for i in range(start, len(nums)):
        sub_set.append(nums[i])
        back(i + 1, nums, sub_set, set_sol)
        sub_set.pop()         
'''
Complexitatea totală:
-Numărul total de subseturi este 2^n.
-Pentru fiecare subset, operațiunea de copiere poate dura până la O(n).
Astfel, complexitatea totală va fi:
O( n * n^2 )
'''
print(subsets([1,2,3,4]))