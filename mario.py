# This is the Mario exercise
while True:
    x = int(input("Height: "))
    if x > 1 or x < 8:
        break

for i in range(1, x + 1):
    blank = x - i
    hashtag = i
    for j in range(1, blank + 1):
        print(" ", end="")
    for j in range(1, hashtag + 1):
        print("#", end="")
    print("  ", end="")
    for j in range(1, hashtag + 1):
        print("#", end="")
    for j in range(1, blank + 1):
        print(" ", end="")
    print("\n")
    
# primera linea x-1 blanks 1 hash 2 blanks 1 hash x-1 blacks
