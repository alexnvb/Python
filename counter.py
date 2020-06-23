from collections import Counter

data = [13, 29, 37, 49, 29, 7, 25, 5, 50, 2, 18, 0, 14, 16, 14, 4, 6, 14, 2, 5, 41, 27, 10, 11, 33, 6, 7, 47, 35, 35, 48, 0, 38, 1, 41, 15, 26, 46, 4, 23, 5, 32, 45, 37, 2, 33, 20, 30, 46, 20, 10, 14, 44, 25, 3, 27, 6, 22, 9, 20, 18, 43, 5, 33, 27, 41, 38, 20, 6, 2, 18, 29, 34, 40, 41, 8, 44, 30, 21, 10, 6, 1, 12, 0, 22, 28, 47, 4, 5, 1, 11, 21, 1, 44, 24, 42, 42, 41, 14, 24]

num_count = Counter(data)

for i in  sorted(num_count.items(), key=lambda parameter_list: (parameter_list[1],parameter_list[0]), reverse=True):
    print(str(i[0])+': '+str(i[1]))