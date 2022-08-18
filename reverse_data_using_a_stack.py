from array_stack import ArrayStack

stack = ArrayStack()

data = list(range(5))

for i in data:
  stack.push(i)

# reverse data
new_data = []

while not stack.is_empty():
  new_data.append(stack.pop())

print(new_data)