def sum(values):
  s = 0;
  for v in values: 
    s += v
  return s

array = [1, 3, 5, 7, 9]
print(sum(array))


def show_name(name = "frank"):
  print(name)


show_name()
show_name("park")