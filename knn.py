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


# --- 2. "Новая" точка (которую мы хотим классифицировать) ---
# У нее нет метки (label), только признаки (features)
new_point = [0.25, 0.75]

import math 



point_a = [1, 5, 2] 
point_b = [3, 1, 6]

#  calc disctance between point
# v1 - point 1
# v2 - point 2
def euclidean_distance(v1, v2):
    points = list(zip(v1, v2))

    sum = 0
    for p in points:
        sum += (p[0] - p[1]) ** 2
        
    result = math.sqrt(sum)
    return result
    
euclidean_distance(point_a, point_b)

# fin closest neighbours
def find_nearest(query_point, dataset, k=1):
    distance_pairs = []
    for index, item in enumerate(dataset):
        dist_from_item = euclidean_distance(query_point, item["features"]) # calc dist for each item in dataset 
        distance_pairs.append((dist_from_item, index))
    

    sorted_distance_list = sorted(distance_pairs)
    closest_k_pairs = sorted_distance_list[:k]
    
    #  Find indices for the K closest
    closest_idx = []
    closest_from_dataset =[]
    desicion_dict = {"White(1)": 0, "Red(0)": 0}
    for dist, index in closest_k_pairs:
        closest_idx.append(index)
        closest_from_dataset.append(dataset[index])
        if dataset[index]['label'] == 1:
            desicion_dict['White(1)'] += 1
        else:
            desicion_dict['Red(0)'] += 1
    
    final_decision = ""
    if desicion_dict['Red(0)'] > desicion_dict['White(1)']:
        final_decision += "It's gonna be RED wine."
    elif desicion_dict['Red(0)'] < desicion_dict['White(1)']:
        final_decision += "It's gonna be WHITE wine."
    else: 
        final_decision += "Difficult to say, try to change query point"
    
    print(f"Индексы ближайших сосeдей из датасета: {closest_idx}")
    print(f"Данные ближайших соседей из датасета по их индексу: {closest_from_dataset}")
    print(f"Словать контроля решения: {desicion_dict}")
    print(f"Финальное решение алгоритма: {final_decision}")
    return final_decision
   
    
    

   
    
    

find_nearest(new_point, wine_dataset, 3)
