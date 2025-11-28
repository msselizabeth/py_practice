"""
You are given an array A representing heights of students. All the students are asked to stand in rows. The students arrive by one, sequentially (as their heights appear in A). For the i-th student, if there is a row in which all the students are taller than A[i], the student will stand in one of such rows. If there is no such row, the student will create a new row. Your task is to find the minimum number of rows created.


Write a function that, given a non-empty array A containing N integers, denoting the heights of the students, returns the minimum number of rows created.


For example, given A = [5, 4, 3, 6, 1], the function should return 2.


Students will arrive in sequential order from A[0] to A[N−1]. So, the first student will have height = 5, the second student will have height = 4, and so on.

For the first student, there is no row, so the student will create a new row.

Row1 = [5]

For the second student, all the students in Row1 have height greater than 4. So, the student will stand in Row1.


Row1 = [5, 4]

Similarly, for the third student, all the students in Row1 have height greater than 3. So, the student will stand in Row1.


Row1 = [5, 4, 3]

For the fourth student, there is no row in which all the students have height greater than 6. So, the student will create a new row.


Row1 = [5, 4, 3]

Row2 = [6]

For the fifth student, all the students in Row1 and Row2 have height greater than 1. So, the student can stand in either of the two rows.


Row1 = [5, 4, 3, 1]

Row2 = [6]

Since two rows are created, the function should return 2.

------------------------------------------------------
Assume that:
N is an integer within the range [1..1,000]
each element of array A is an integer within the range [1..10,000]
"""
def solution(A):
    """
    The function takes an array of integers representing height, 
    and returns the number of rows taken to create sequenced rows from the array.
    """
    # list of mins
    min_h = []
  
    for h in A:
        print(f"H: {h}")
        in_row = False  
        for i in range(len(min_h)):
            if h < min_h[i]:
                in_row = True
                min_h[i] = h
                break
        
        if not in_row:
            min_h.append(h)
    print(min_h)  
    return len(min_h)      
    

# def solution(A):
    # """Your solution goes here."""
    # min_rows = []
    # for h in A:
    #     found_a_row = False

    #     for i in range(len(min_rows)):
    #         if h < min_rows[i]:
    #             min_rows[i] = h
    #             found_a_row = True
    #             break

    #     if not found_a_row:
    #         min_rows.append(h)
    # return len(min_rows)


# Пример 1:
print(f"A=[5, 4, 3, 6, 1]: {solution([5, 4, 3, 6, 1])}")  # Ожидаем 2

# Пример 2 (где твой первый код ошибался):
print(f"A=[10, 5, 7]: {solution([10, 5, 7])}")  # Ожидаем 2 


