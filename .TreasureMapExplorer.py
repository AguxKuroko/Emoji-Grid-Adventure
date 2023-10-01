
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")
miejsce_w_l = position[1] # to numer listy np 3
pozycja = position[0] # to numer indexu np 2
miejsce_w_l = int(miejsce_w_l)
pozycja = int(pozycja)
x = (pozycja - 1)

if miejsce_w_l == 1:
    row1[x] = "X"
elif miejsce_w_l == 2:
    row2[x] = "X"
else:
    row3[x] = "X"

print(f"{row1}\n{row2}\n{row3}")
