objects = ['1', 2, '3', [1, 2, 3], 3, {1, 3}, {}]

print(len(set([id(obj) for obj in objects])))

