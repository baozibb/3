#zyx
list=['dfds','dfas','5467']
print(type(list))
list = ','.join(list)
print(type(list))
with open('g.txt', 'w')as f:
    f.write(list)