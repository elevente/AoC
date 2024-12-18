input = """Game 1: 10 green, 9 blue, 1 red; 1 red, 7 green; 11 green, 6 blue; 8 blue, 12 green
Game 2: 11 red, 7 green, 3 blue; 1 blue, 8 green, 5 red; 2 red, 12 green, 1 blue; 10 green, 5 blue, 7 red
Game 3: 2 red, 7 green, 1 blue; 1 blue, 8 red; 7 green, 19 red, 5 blue; 1 blue, 10 green, 18 red; 10 red, 6 blue, 4 green
Game 4: 2 blue, 5 green, 2 red; 7 red, 3 green; 3 blue, 2 red; 16 green, 2 blue
Game 5: 1 blue, 9 red; 5 blue, 9 green, 6 red; 8 red, 10 blue, 3 green; 3 red, 13 green, 4 blue; 5 green, 9 red, 6 blue; 4 green, 8 red, 7 blue
Game 6: 1 red, 2 green; 2 red, 1 blue; 5 red, 10 green, 2 blue; 1 blue, 2 green, 3 red; 1 red, 6 green
Game 7: 9 blue, 14 green, 5 red; 10 green, 8 blue, 2 red; 20 green, 1 red; 4 blue, 17 green, 4 red
Game 8: 16 blue, 16 green, 8 red; 16 blue, 6 red, 10 green; 13 blue, 8 green, 16 red; 10 red, 13 green, 13 blue
Game 9: 8 blue, 10 green, 4 red; 18 green, 14 blue, 12 red; 4 green, 10 blue, 17 red; 16 red, 6 blue, 5 green; 11 red, 9 blue; 16 green, 13 red, 7 blue
Game 10: 5 green, 2 red, 13 blue; 3 red, 2 green, 17 blue; 3 green, 12 blue, 15 red; 7 blue, 14 red; 3 red, 4 green, 17 blue
Game 11: 8 green, 10 blue, 15 red; 11 blue, 4 green, 3 red; 10 blue, 4 green, 5 red; 7 blue, 1 green, 4 red; 2 red, 9 blue; 18 red, 8 green, 2 blue
Game 12: 16 red, 10 green; 12 red, 8 blue, 3 green; 8 red, 10 green, 7 blue; 10 green, 12 red
Game 13: 5 green, 2 red; 13 blue, 4 green, 4 red; 8 blue, 4 green
Game 14: 9 green, 3 red, 1 blue; 1 blue, 3 red, 1 green; 6 green; 3 green, 5 red; 1 blue, 4 red
Game 15: 13 red, 2 blue, 7 green; 6 green, 4 red, 7 blue; 8 blue, 11 red, 4 green; 1 green, 7 blue, 10 red; 3 blue, 9 green, 6 red; 6 green, 11 red, 1 blue
Game 16: 1 red, 14 green; 4 green, 1 blue, 4 red; 3 red, 1 blue, 5 green; 5 red, 1 blue, 14 green; 1 blue, 1 red, 12 green; 6 red, 14 green, 1 blue
Game 17: 14 green, 14 red; 19 green, 3 blue, 10 red; 4 green, 10 red, 1 blue
Game 18: 9 green, 1 blue, 12 red; 1 green, 10 red; 1 blue, 3 red
Game 19: 6 blue, 3 red, 3 green; 12 blue; 11 red, 14 blue, 3 green; 14 blue, 13 red, 1 green; 5 blue, 9 red
Game 20: 10 blue, 11 green, 3 red; 2 red, 16 green; 6 blue, 16 green, 4 red; 14 green, 7 red, 1 blue; 5 red, 9 blue, 11 green
Game 21: 1 red; 4 red; 2 red, 2 green, 1 blue
Game 22: 11 green, 3 blue, 3 red; 12 blue, 6 green; 1 red, 5 blue, 1 green; 9 blue, 6 green; 10 green, 1 red, 8 blue
Game 23: 13 blue, 3 green; 3 red, 5 green, 6 blue; 2 red, 11 green, 9 blue
Game 24: 1 blue, 1 green; 1 blue; 1 red
Game 25: 7 red, 1 green, 14 blue; 17 blue, 4 red, 6 green; 7 blue, 5 red; 2 red, 6 green, 20 blue
Game 26: 10 green, 8 red, 11 blue; 13 green, 2 blue, 4 red; 1 blue, 6 green, 9 red
Game 27: 9 green, 1 blue, 6 red; 7 red, 14 green; 13 green, 2 red; 2 red, 13 green; 2 green, 7 red
Game 28: 10 red, 6 green; 7 green, 11 red, 1 blue; 8 red, 5 green; 10 green, 13 red; 17 red, 3 green
Game 29: 4 blue, 3 red, 13 green; 9 green, 2 red, 1 blue; 11 green, 5 blue, 2 red; 1 blue, 7 green, 2 red; 4 blue, 1 red, 12 green
Game 30: 6 blue, 1 green, 3 red; 1 green, 3 red, 1 blue; 6 green, 2 red, 2 blue
Game 31: 11 red; 5 red, 2 green; 3 green, 6 red, 1 blue; 1 green, 18 red; 2 green, 14 red
Game 32: 11 blue, 12 green, 11 red; 5 red, 14 blue, 5 green; 5 blue, 7 green, 18 red
Game 33: 8 blue, 4 green, 11 red; 14 blue, 11 red, 3 green; 3 green, 1 blue; 17 red, 2 green, 9 blue; 7 green, 7 blue, 3 red; 2 green, 3 red, 7 blue
Game 34: 1 blue, 17 green; 2 blue, 1 red, 10 green; 10 green, 1 red; 6 green, 1 red, 1 blue; 2 green, 2 blue, 1 red
Game 35: 1 blue, 5 red, 5 green; 4 blue, 3 green, 8 red; 5 green, 14 blue; 5 green, 4 blue, 14 red
Game 36: 13 green, 7 red, 2 blue; 2 red, 2 green; 1 red, 12 green; 7 green, 8 red
Game 37: 11 red, 4 green, 1 blue; 12 red, 3 green, 5 blue; 1 blue, 12 red, 1 green; 9 red, 10 green; 7 red, 2 blue, 5 green; 7 green, 1 red, 4 blue
Game 38: 14 red, 20 blue, 6 green; 14 red, 12 green, 13 blue; 10 green, 10 red, 9 blue; 9 green, 9 blue, 15 red
Game 39: 4 blue; 8 green, 7 blue; 12 green, 2 blue, 5 red; 2 blue, 3 green, 3 red; 5 red, 1 green, 1 blue; 6 red, 1 blue
Game 40: 7 green, 10 red, 3 blue; 2 blue, 1 red, 7 green; 2 red, 5 blue, 11 green; 4 blue, 12 red, 6 green; 13 green, 7 blue, 9 red; 14 blue, 7 green, 8 red
Game 41: 14 red, 17 blue, 3 green; 18 blue, 4 green, 17 red; 2 green, 17 red, 8 blue; 7 green, 13 blue, 6 red
Game 42: 1 blue, 16 green; 14 green; 17 blue, 4 green, 7 red; 6 red, 7 blue, 8 green
Game 43: 8 red, 15 blue; 8 red, 1 green, 11 blue; 17 blue, 3 red
Game 44: 10 red, 2 green, 11 blue; 8 green, 4 blue, 6 red; 6 green, 2 blue, 10 red; 1 blue, 12 red, 7 green
Game 45: 1 blue, 4 red, 4 green; 2 red, 5 green; 3 green, 6 blue, 1 red; 12 blue, 1 red, 2 green
Game 46: 2 blue; 1 red, 4 blue; 2 blue, 15 red; 3 blue, 4 green, 5 red; 4 green, 13 red; 1 blue, 3 green, 9 red
Game 47: 13 blue, 2 green, 2 red; 2 green, 12 blue, 3 red; 2 green, 1 blue
Game 48: 1 blue, 4 green, 11 red; 2 blue, 5 red, 8 green; 6 red
Game 49: 1 red, 10 green; 3 green, 8 blue, 5 red; 7 red, 5 green, 7 blue
Game 50: 12 blue, 5 green, 1 red; 7 blue, 2 red; 12 blue, 3 green; 16 blue; 1 blue, 3 green; 2 red, 14 blue, 11 green
Game 51: 6 blue, 15 red, 1 green; 15 red, 2 blue, 1 green; 12 red, 2 green
Game 52: 5 green, 11 blue, 5 red; 18 green, 4 red, 10 blue; 14 green, 8 blue, 8 red; 2 red, 9 green, 11 blue; 9 blue, 5 red, 10 green
Game 53: 1 red, 1 green; 2 green, 1 red, 2 blue; 2 green, 1 blue
Game 54: 4 blue, 3 red, 7 green; 4 blue, 13 green; 1 red, 2 green, 7 blue; 5 blue, 5 red, 17 green
Game 55: 8 red, 11 green, 11 blue; 1 green, 15 blue, 6 red; 7 red, 8 blue, 11 green; 2 green, 1 red, 11 blue; 11 blue, 3 red; 3 red, 7 blue, 10 green
Game 56: 13 blue, 3 green; 1 red, 1 green, 7 blue; 17 blue, 2 red; 3 blue, 4 green, 4 red
Game 57: 9 green, 11 blue, 12 red; 13 red, 6 green, 1 blue; 4 blue, 1 green, 14 red; 11 red, 6 blue, 3 green
Game 58: 7 green, 2 blue, 6 red; 1 red, 4 green; 1 blue, 8 green, 10 red
Game 59: 3 green, 11 red, 3 blue; 1 blue, 5 red, 8 green; 10 green, 9 red; 5 green, 5 red, 1 blue; 4 green, 8 blue; 13 green
Game 60: 2 blue, 11 green, 7 red; 5 red, 9 green, 2 blue; 3 blue, 2 red, 8 green; 6 red, 2 blue, 9 green; 5 red, 4 green, 2 blue; 6 red, 5 blue, 11 green
Game 61: 7 blue, 5 green, 8 red; 12 blue, 1 red, 11 green; 15 blue, 14 red, 15 green; 14 red, 7 blue, 6 green; 9 blue; 3 green, 10 blue, 11 red
Game 62: 8 red, 1 blue, 1 green; 2 red, 1 blue, 8 green; 11 blue, 15 red, 4 green; 1 red, 5 green, 2 blue; 15 green, 11 blue, 12 red
Game 63: 6 red, 3 green, 7 blue; 8 red, 2 green; 4 green, 3 red, 4 blue; 6 blue, 3 red, 10 green; 4 blue, 6 red, 9 green; 8 blue, 10 green, 5 red
Game 64: 1 blue, 9 red, 1 green; 17 red, 3 blue; 8 red, 2 green; 12 red, 8 blue
Game 65: 15 blue, 2 red; 1 green, 14 blue; 10 green, 1 red, 10 blue; 10 green, 1 red, 12 blue; 13 blue, 1 green
Game 66: 18 green, 3 red, 7 blue; 19 blue, 2 red; 5 red, 8 blue, 11 green; 1 red, 15 blue, 12 green; 13 blue, 6 green; 12 blue, 6 green
Game 67: 1 blue, 2 green, 6 red; 7 red, 5 blue; 9 red, 13 blue, 5 green; 4 green, 4 blue, 5 red; 11 blue, 7 red; 3 blue, 9 red
Game 68: 2 blue, 8 green, 16 red; 11 green, 13 blue; 6 red, 7 green, 1 blue; 4 green, 7 red, 8 blue
Game 69: 7 green, 3 blue, 5 red; 11 green, 4 blue; 1 red, 15 green, 10 blue; 8 green, 12 blue, 4 red
Game 70: 8 blue, 8 green; 4 blue, 1 red, 6 green; 1 green, 1 blue; 7 green, 4 blue
Game 71: 7 red, 13 blue, 4 green; 2 blue, 11 red, 9 green; 14 blue, 6 green, 2 red; 10 red, 6 blue, 10 green
Game 72: 1 blue, 9 green, 1 red; 4 blue, 6 green, 1 red; 1 red, 3 green, 3 blue; 10 green, 3 blue, 2 red; 3 blue, 1 red, 1 green; 3 green, 1 red, 3 blue
Game 73: 4 green, 15 red, 6 blue; 1 green, 12 red; 2 green, 16 red; 1 green, 12 red, 2 blue; 6 red, 4 green, 2 blue; 19 red, 3 blue, 2 green
Game 74: 14 green, 2 blue, 3 red; 13 green, 4 red; 3 green, 4 blue; 3 blue, 3 red; 2 red, 12 green; 3 blue, 3 green
Game 75: 13 red, 10 blue, 1 green; 14 blue, 9 red, 2 green; 8 blue; 1 green, 13 red, 11 blue
Game 76: 2 red, 8 blue, 12 green; 11 green, 2 red; 2 red, 2 blue, 10 green; 5 blue, 2 green; 3 red, 11 green, 8 blue
Game 77: 4 blue, 8 red, 14 green; 15 green, 12 red, 5 blue; 8 red, 5 green, 1 blue
Game 78: 8 red, 19 blue, 4 green; 18 blue, 2 red; 12 blue, 4 green, 8 red; 17 blue, 2 green, 9 red; 9 red, 10 blue, 1 green; 6 green, 9 blue, 1 red
Game 79: 1 blue, 11 red, 2 green; 2 red, 2 green, 6 blue; 11 red, 2 blue, 2 green; 11 red, 2 green, 4 blue
Game 80: 1 red, 9 blue; 1 red, 5 blue, 8 green; 5 green, 1 red, 4 blue; 2 green, 9 blue, 1 red; 7 blue, 1 green, 1 red
Game 81: 1 green, 1 blue, 7 red; 3 blue, 7 green, 6 red; 5 green; 3 blue; 3 red, 4 blue, 1 green; 5 red, 9 green
Game 82: 12 blue, 4 red, 4 green; 7 red, 4 blue; 3 green, 10 red, 3 blue; 6 blue, 13 red; 4 blue, 5 red, 1 green
Game 83: 1 red, 1 green, 18 blue; 20 blue, 16 red, 1 green; 17 blue, 12 red; 1 green, 9 blue, 7 red
Game 84: 6 blue, 7 green, 6 red; 6 red, 10 green, 1 blue; 5 red, 8 green; 13 green, 2 red, 7 blue
Game 85: 1 blue, 7 red, 11 green; 1 red; 8 red, 10 green, 4 blue; 4 red, 11 green, 1 blue; 1 blue, 6 green
Game 86: 9 green, 2 blue; 3 red, 1 green, 2 blue; 1 green, 5 blue, 9 red; 1 blue, 2 green; 9 red, 1 green, 4 blue
Game 87: 15 red, 1 green, 16 blue; 1 green, 6 red, 17 blue; 7 red, 1 green, 3 blue; 8 red, 3 blue, 1 green; 15 red, 1 green
Game 88: 7 green, 3 red, 10 blue; 8 blue, 8 red, 3 green; 18 green, 1 blue, 7 red; 8 red, 7 green, 10 blue
Game 89: 5 red, 16 blue; 7 blue; 5 blue, 4 red; 3 blue, 4 green, 6 red; 1 red, 2 green, 16 blue
Game 90: 19 blue, 5 green, 4 red; 2 green, 20 blue, 1 red; 18 blue
Game 91: 10 red, 11 blue, 1 green; 18 red, 12 blue; 11 blue, 10 red
Game 92: 3 green, 1 blue; 8 red, 5 green; 10 red, 3 green
Game 93: 5 green, 1 blue, 5 red; 1 blue, 2 red, 7 green; 2 green, 6 red, 1 blue; 7 green, 1 blue, 2 red; 6 red, 1 green
Game 94: 3 red, 6 blue, 2 green; 5 blue, 9 red; 11 blue, 5 red, 2 green; 2 green, 3 red, 14 blue; 5 red, 13 blue; 6 blue, 2 green, 8 red
Game 95: 4 red, 3 green, 17 blue; 1 red, 5 green, 4 blue; 15 blue, 11 green; 5 green, 1 red, 4 blue; 11 blue, 2 green, 17 red
Game 96: 3 red, 20 blue, 18 green; 1 red, 1 blue, 20 green; 18 blue, 4 green, 8 red
Game 97: 11 green; 7 red, 8 green, 2 blue; 4 green, 17 red; 4 green, 7 red; 14 green, 18 red, 2 blue
Game 98: 2 blue, 7 green, 1 red; 9 green, 10 red, 5 blue; 13 blue, 10 red, 8 green; 8 green, 11 red, 12 blue; 5 blue, 4 green, 2 red
Game 99: 2 blue, 13 green; 1 blue; 1 red, 2 blue, 2 green; 1 red, 1 blue
Game 100: 1 red, 14 green; 17 green, 12 red; 3 green, 7 red, 3 blue; 4 green, 13 red, 3 blue; 5 green, 11 red, 5 blue"""

lines = input.split("\n")
total = 0
RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14
for line in lines:
    gameId = line.split(":")[0].split(" ")[1]
    rounds = line.split(":")[1].split(";")
    maxBlue = 0
    maxGreen = 0
    maxRed = 0
    for roundt in rounds:
        buzi2 = roundt.split(",")
        for b2 in buzi2:
            buzi = b2.strip().split(" ")
            if buzi[1] == "blue":
                if int(buzi[0]) > int(maxBlue):
                    maxBlue = buzi[0]
            if buzi[1] == "green":
                if int(buzi[0]) > int(maxGreen):
                    maxGreen = buzi[0]
            if buzi[1] == "red":
                if int(buzi[0]) > int(maxRed):
                    maxRed = buzi[0]
    totalix = int(maxGreen) * int(maxBlue) * int(maxRed)
    total += totalix
print(total)