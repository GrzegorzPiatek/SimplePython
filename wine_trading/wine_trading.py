while True:
    t = int(input())
    if t == 0:
        break
    moves = 0
    inhabitants = list(map(int, input().split()))
    for i in range(1, t):
        moves += abs(inhabitants[i-1])
        inhabitants[i]+= inhabitants[i-1]
    print(moves)
