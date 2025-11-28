'''
"One-Hot Encoding" (Ручная Векторизация)
Цель: Научиться преобразовывать категориальные данные (строки) в численный формат, понятный для моделей.

Связь с ML: Это фундаментальная операция в ML. Модели не понимают слова "красный" или "синий". Их нужно превратить в векторы, например, [1, 0] и [0, 1]. Мы эмулируем эту логику.

Задача: У вас есть список тегов для постов в блоге: tags = ['python', 'ml', 'python', 'data', 'ml', 'statistics']

Нужно написать функцию encode_one_hot(data), которая:

1) Находит все уникальные теги в data.
2) Создает "словарь" (mapping), где каждому уникальному тегу присваивается свой индекс (например, 'python': 0, 'ml': 1, 'data': 2, 'statistics': 3).
3)Преобразует исходный список tags в список списков (векторов). Длина каждого вектора равна количеству уникальных тегов. В векторе везде стоят нули, кроме одной позиции — на месте индекса, соответствующего тегу.

Ожидаемый результат для tags (порядок векторов может отличаться):
[
  [1, 0, 0, 0],  # 'python'
  [0, 1, 0, 0],  # 'ml'
  [1, 0, 0, 0],  # 'python'
  [0, 0, 1, 0],  # 'data'
  [0, 1, 0, 0],  # 'ml'
  [0, 0, 0, 1]   # 'statistics'

На что обратить внимание:

Как получить уникальные элементы из списка? (Подсказка: set()).
Как создать словарь "элемент -> индекс"? (Подсказка: enumerate()).
Как создать список из нулей нужной длины? (Подсказка: [0] * n).

Это отличная задача на комбинацию словарей и list comprehensions.
'''
# tags_dict = {
#   'python': 0,
#   'ml': 1,
#   'data': 2,
#   'statistics': 3
# }


def encoding(strings: str) -> list:
  #  initialize expected result
  matrix = []
  # fing unique values
  unique_strs = set(strings)
  #  Create a dict to have tag: index
  tags_dict = {tag: index for index, tag in enumerate(unique_strs)}
  
  # loop in intital list(tags) 
  for tag in strings:
      # craete a vector with len from unique values 
      vector = [0 for item in range(len(unique_strs))]
      #  Find a vector position equals tag position(index) and assigning 1 instead of 0
      vector[tags_dict[tag]] = 1
      #  appen to final result(matrix)
      matrix.append(vector)
  
  return matrix

result = encoding(['python', 'ml', 'python', 'data', 'ml', 'statistics', "blue", 'red', 'black', 'pink'])
print(result) #[
#   [1, 0, 0, 0],  # 'python'
#   [0, 1, 0, 0],  # 'ml'
#   [1, 0, 0, 0],  # 'python'
#   [0, 0, 1, 0],  # 'data'
#   [0, 1, 0, 0],  # 'ml'
#   [0, 0, 0, 1]  # 'statistics'
# ]   