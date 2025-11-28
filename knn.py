# Как с этим работать:
# Базовая задача (euclidean_distance):

# Просто потренируйтесь считать расстояние между любыми двумя точками из dataset_features.

# Например: euclidean_distance(dataset_features[0], dataset_features[4]) (расстояние между первым красным и первым белым вином).

# Сложная задача (find_nearest):
# Напишите функцию find_nearest(query_point, dataset_features).
# Эта функция должна пройтись по каждой точке в dataset_features и посчитать расстояние от нее до query_point.
# Функция должна вернуть индекс самой близкой точки.

# Логическое завершение (Цель k-NN):
# Допустим, ваша функция find_nearest вернула индекс 5.
# Вы смотрите, какая метка у этого индекса: dataset_labels[5].
# Она равна 1.
# Вывод: "Наш k-NN (с k=1) предсказывает, что query_point — это 'Белое' вино!

# --- 1. "Тренировочный" набор данных (в виде списка словарей) ---
# Каждый словарь — это одно "наблюдение" (одно вино)
# Каждая точка(features) - это [кислотность, сахар] -> значения уже нормализированны дли использования алгоритмом 
# label - Это метки (0 -> Красное , 1 -> белое)

import math 
from collections import Counter

wine_dataset = [
    # Класс 0 ('Красное')
    {'features': [0.7, 0.3], 'label': 0},
    {'features': [0.8, 0.2], 'label': 0},
    {'features': [0.6, 0.4], 'label': 0},
    {'features': [0.9, 0.1], 'label': 0},
    
    # Класс 1 ('Белое')
    {'features': [0.2, 0.8], 'label': 1},
    {'features': [0.3, 0.7], 'label': 1},
    {'features': [0.1, 0.9], 'label': 1},
    {'features': [0.2, 0.6], 'label': 1}
]

#  calc disctance between point
# v1 - point 1
# v2 - point 2
def euclidean_distance(v1, v2):
    square_sum = sum((p1 - p2) ** 2 for p1, p2 in zip(v1, v2))
    return  math.sqrt(square_sum)

# # Just to check formula 
# point_a = [1, 5, 2] 
# point_b = [3, 1, 6]
# euclidean_distance(point_a, point_b)

# fin closest neighbours
def find_nearest(query_point, dataset, k=1):
    distance_pairs = [(item, euclidean_distance(query_point, item["features"])) for item in dataset]
    # print(distance_pairs) # [
    #  ({'features': [0.7, 0.3], 'label': 0}, 0.49244289008980524),
    # ({'features': [0.8, 0.2], 'label': 0}, 0.6264982043070835), 
    # ({'features': [0.6, 0.4], 'label': 0}, 0.36400549446402586), 
    # ({'features': [0.9, 0.1], 'label': 0}, 0.7632168761236874), 
    # ({'features': [0.2, 0.8], 'label': 1}, 0.30413812651491096), 
    # ({'features': [0.3, 0.7], 'label': 1}, 0.20615528128088306), 
    # ({'features': [0.1, 0.9], 'label': 1}, 0.4272001872658766), 
    # ({'features': [0.2, 0.6], 'label': 1}, 0.33541019662496846)
    # ] 
    
    sorted_distance_pairs = sorted(distance_pairs, key=lambda item: item[1])
    print(sorted_distance_pairs) #[
        # ({'features': [0.3, 0.7], 'label': 1}, 0.20615528128088306), ({'features': [0.2, 0.8], 'label': 1}, 0.30413812651491096), ({'features': [0.2, 0.6], 'label': 1}, 0.33541019662496846), ({'features': [0.6, 0.4], 'label': 0}, 0.36400549446402586), ({'features': [0.1, 0.9], 'label': 1}, 0.4272001872658766), ({'features': [0.7, 0.3], 'label': 0}, 0.49244289008980524), ({'features': [0.8, 0.2], 'label': 0}, 0.6264982043070835), ({'features': [0.9, 0.1], 'label': 0}, 0.7632168761236874)]
    
    closest_k_pairs = sorted_distance_pairs[:k]
    
    return closest_k_pairs
    

def classification(query_point, dataset, k=1):
       #  Find indices for the K closest
    # desicion_dict = {"White(1)": 0, "Red(0)": 0}
    LABEL_MAP = {0: "Red", 1: "White", 2: "Rose"}
    
    closest_k_pairs = find_nearest(query_point, dataset, k)
    k_nearest_labels = [item['label'] for item, disct in closest_k_pairs]
    
    votes = Counter(k_nearest_labels)
    # print(f"Votes: {votes.most_common(2)[0][1]}")
    # print(f"Votes: {votes.most_common(2)[1][1]}")
    
    winner_label, winner_count = votes.most_common(1)[0]
     
    if len(votes) > 1 and votes.most_common(2)[0][1] == votes.most_common(2)[1][1]:
        final_decision = "Difficult to say (tie!), try to change K"
        
    final_decision = f"It's gonna be {LABEL_MAP[winner_label]} wine."
    
    print(f"{k} closest: {closest_k_pairs}")
    print(f"Финальное решение алгоритма: {final_decision}")
    return final_decision

    
   
# --- 2. "Новая" точка (которую мы хотим классифицировать) ---
# У нее нет метки (label), только признаки (features)    
    
new_point = [0.5, 0.75]
classification(new_point, wine_dataset,6) #white wine example

point_2 = [0.75, 0.25]
classification(point_2, wine_dataset, 7) # red wine sample

