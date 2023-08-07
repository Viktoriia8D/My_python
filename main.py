import random

row_1 = ['⬜', '⬜', '⬜']
row_2 = ['⬜', '⬜', '⬜']
row_3 = ['⬜', '⬜', '⬜']
map1 = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")

# position_column = int(int(position)/10)
# position_row = int(position)%10

position = input("Where do you want to put the treasure? ")

map1[int(position)%10-1][int(int(position)/10)-1] = " x"

print(f"{row_1}\n{row_2}\n{row_3}")
