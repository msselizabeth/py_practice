def lengthOfLastSeen(s: str) -> int:
    # Словарь будет хранить {символ: последний_индекс}
    char_map = {}
    
    max_length = 0
    left = 0 # Левая граница окна

    for right in range(len(s)):
        current_char = s[right]
        
        # Если символ уже в словаре (т.е. в нашем окне)
        if current_char in char_map:
            # Мы должны сдвинуть левую границу.
            # Мы не можем просто взять "старый_индекс + 1",
            # потому что left мог уже уйти дальше (как в примере "abba").
            # Поэтому берем максимум из того, где left уже стоит,
            # и того, куда нам предлагает прыгнуть дубликат.
            
            last_seen_index = char_map[current_char]
            print(last_seen_index)
            left = max(left, last_seen_index + 1)
            
        # Обновляем (или добавляем) индекс последнего появления символа
        char_map[current_char] = right
        
        # Обновляем максимальную длину
        max_length = max(max_length, (right - left) + 1)
        
    return max_length

print(f"Метод со словарем 'abba': {lengthOfLastSeen('abba')}")
# print(f"Метод со словарем 'abcabcbb': {lengthOfLastSeen('abcabcbb')}")