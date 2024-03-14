def hello():
  print("Hello User")

hello()

def pack(item,item2,item3):
  print(item,item2,item3)
  return (item, item2, item3)
pack("pencil","book","paper")

def eat_lunch(list):
  if len(list) == 0:
    print("My Lunchbox is empty")
  else:
    print("First i eat", list[0])
    for item in list[1:]:
      print("Next i eat", item)

meal = ["sandwich", "apple", "banana", "cookies"]
eat_lunch(meal)