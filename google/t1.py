

def solution(A):
    """
    """
    sorted_arr = sorted(A)
    count = 0
  
    for i in range(len(A) - 1):
            first_p = A[:i+1]
            second = A[i+1:]
            print(first_p)
            print(second)
            sorted_first = sorted(first_p)
            sorted_second = sorted(second)
            merge = sorted_first + sorted_second
            print(f"Merge: {merge}")
            
            if merge == sorted_arr:
                print("Found")
                count += 1
    return count
     



res = solution([1, 3, 2, 4])
print(f"Function result: {res}")