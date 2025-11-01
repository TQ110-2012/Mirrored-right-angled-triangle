rows = int(input("Please enter the number of rows: "))
print("Mirrored Right-Angled Triangle")
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(' ', end='')  
    for j in range(1, i + 1):
        print('*', end='')  
    print() 