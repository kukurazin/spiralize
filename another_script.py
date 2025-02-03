#n > 2

import os
import time

n = 10
symbol = ". "
alt = "# "
def square(n):
    data = [[symbol for _ in range(n)] for _ in range(n)]
    

    x = 0
    y = 0
    
    
    while True:
        #check if can move RIGHT
        if data[y][x + 2] == alt or data[y + 1][x + 1] == alt:
            data[y][x] = alt
            os.system('cls')
            return "\n".join(" ".join(map(str, row)) for row in data)
        #move RIGHT
        for r in range(x, n):
            try:
                if data[y][r + 2] == alt:
                    x = r
                    break
            except: ZeroDivisionError
            data[y][r] = alt
            x = r
            os.system('cls')
            print("\n".join(" ".join(map(str, row)) for row in data))
            time.sleep(0.1)
            
        #check if can move DOWN
        if data[y + 2][x] == alt or data[y + 1][x - 1] == alt:
            data[y][x] = alt
            os.system('cls')
            return "\n".join(" ".join(map(str, row)) for row in data)
        #move DOWN
        for d in range(y, n):
            try:
                if data[d + 2][x] == alt:
                    data[d][x] = alt
                    y = d
                    break
            except: ZeroDivisionError
            data[d][x] = alt
            y = d
            os.system('cls')
            print("\n".join(" ".join(map(str, row)) for row in data))
            time.sleep(0.1)
            
        #check if can move LEFT
        if data[y][x - 2] == alt or data[y - 1][x - 1] == alt:
            data[y][x] = alt
            os.system('cls')
            return "\n".join(" ".join(map(str, row)) for row in data)
        #move LEFT
        for l in range(x - 1, -1, -1):
            try:
                if  y != n -1 and data[y][l - 2] == alt:
                    x = l
                    data[y][l] = alt
                    break
            except: ZeroDivisionError
            data[y][l] = alt
            x = l
            os.system('cls')
            print("\n".join(" ".join(map(str, row)) for row in data))
            time.sleep(0.1)
            
        #check if can move UP
        if data[y - 2][x] == alt or data[y - 1][x + 1] == alt:
            data[y][x] = alt
            os.system('cls')
            return "\n".join(" ".join(map(str, row)) for row in data)
        #move UP
        for u in range(y - 1, -1, -1):
            try:
                if  data[u - 2][x] == alt:
                    data[u][x] = alt
                    y = u
                    break
            except: ZeroDivisionError
            data[u][x] = alt
            y = u
            os.system('cls')
            print("\n".join(" ".join(map(str, row)) for row in data))
            time.sleep(0.1)
    

print(square(n))
