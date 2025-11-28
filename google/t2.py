
def solution(A):
    """
    """
    total = sum(A)
    sums = []
    
    for el in A:
        new_sum = total - el * 2
        # best_min = min(best_min, abs(new_sum))
        sums.append(abs(new_sum))
            
    return min(sums)
        



res = solution([1, 3, 2, 5])
print(f"Function result: {res}")
res1 = solution([-4, 0, -3, -3])
print(f"Function result: {res1}")
# res = solution([1, 3, 2, 5])
# print(f"Function result: {res}")
# res = solution([1, 3, 2, 5])
# print(f"Function result: {res}")