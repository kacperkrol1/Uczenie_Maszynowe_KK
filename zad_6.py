def combine_and_pow(numbers1, numbers2):
    numbers = list(set(numbers1 + numbers2))
    return [x ** 3 for x in numbers]


result = combine_and_pow([1, 2, 3], [3, 4, 5])
print(result)
