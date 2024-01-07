name = "hello"
online = True # 注意 python 中布尔值为大写
age = 18
price = 3.14 # 浮点数

print(name, online, age, price)


print(name[0:2])

print(type(name), type(online), type(age), type(price)) # str bool int float

new_price = float("3")

print(new_price, type(new_price)) # 3.0 float


array = [1, 2, 3, 4, 5, 6]
print(len(array))

print(array[0], array[1])

my_dict = { "a": 1, "b": True, "c": "hello"}

print(my_dict["a"])