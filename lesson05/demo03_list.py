classmates = ['Michael', 'Bob', 'Tracy']

print(classmates)

print(len(classmates)) # 4

classmates.append('Adam')

print(len(classmates)) # 4

classmates.insert(1, 'jack')

print(classmates) # ['Michael', 'jack', 'Bob', 'Tracy', 'Adam']

top = classmates.pop()

print(top) # Adam