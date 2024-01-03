import random
print("Let's start the game ----")
print("[ATTENTION] 1 for Sneak, 2 for Water, 3 for Gun\n")
p = int(input("Your choice(1,2,3): "))
c = random.randint(1, 3)
print(f"Computer's choice: {c}")
v = [c, p]
l = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]]
#       0       1       2        3      4        5      6       7       8
if v == l[0] or v == l[4] or v == l[8]:
    print("Game Draw.")
elif v == l[2] or v == l[3] or v == l[7]:
    print("You Lose the Game.")
else:
    print("Yow Win the Game.")
