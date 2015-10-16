def func(elem):
    """увеличивает значение каждого элемента списка"""
    return elem+10 #возвращаем новое значение
arr=[1,2,3,4,5]
print(list(map(func, arr)))
input()
