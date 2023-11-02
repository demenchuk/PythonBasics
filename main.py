

n1 = int(input("Введіть перше число: "))
n2 = int(input("Введіть друге число: "))
n3 = int(input("Введіть третє число: "))


max_num = max(n1, n2, n3)

min_num = min(n1, n2, n3)


middle_num = n1 + n2 + n3 - max_num - min_num


print(max_num)
print(middle_num)
print(min_num)