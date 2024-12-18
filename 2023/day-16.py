import numpy

# sys. setrecursionlimit(10000)

input = r"""\.........-......|...../................................-...........|.../.\\...\|...................|.........
../..\...............-../............\.........-......-................././........|......................|...
......../..-........../................../...|.....-......................\.....-..............|............/|
......-......-............................\..\............../................./.-.................\.....|.\|..
...-....-|....................-...-..../...................-....../...........|.............\.....-...........
..\............../..../................|...........|/......|..........-\.........|...../....................|.
\...........\.\....../...|..........--.................|......//...../..-.....|.....-.........................
..................................................|...........\.\.................../.....................\...
.....-...................-............./.......................|............/...|..........................-..
..............-......\..............\................................-.|../................|....|../\....|....
./../\..............-..............|.........................|\................................|.-./.....|....
..........\....-................./........../............../........\-..........\....-........................
.........-....../.............\../-......-.............\........\......./......-|..\.........\............-...
......-....|.......|.............................\..-.............\......-......................|......|......
....\......../.............................||....-.............-.........................\........../.........
........-......................................................\.........../...|./............-|..............
......\..-........|./..................\../....|.........-\...-..-....\...-................\..................
|./.....\.-......../.-|.............\..\.\......-.|............/.|..\|....................../.................
................................../..-........\.\..|.-..|/...-...............-............\........-..../.....
.......|............\../......\...../.......................|........|...-.|...\...-....\......|..............
.................-......./........../.......|/........|....-\........../..............-................../....
..../...................-..\.........|................../..|.../...............|-\............../.............
.............................|....../............................|..|.........../....../....-.|..||....\......
.....//.........\..........\.|...-./.......|.-..\...\.......\.-.............../.....|..............-.|........
.-...........\.\..........\|..\.....\.|...........--.............\.....-./.......\................../.........
............\....................................\.......-....../.....\....../....-.....................-.....
\.......\...-.|......./\..|...\......|......../.....-.....|......./................./.........../.............
/.|.....................................................\./.........\...|......|.......................|./..-.
....|............./....\...-.\...../.......\.................|.............|......\..../.../..\...........\...
..........................|...........|.../............\..\....\............-|...................\.../......\.
.......|\.\............./...../.......././..../.....-..|...\.......|..........\............/-.................
.|\....|.....-.-......\-..........\.....................\...........................-...|.....|..-...........|
/\......|....-.............................-/....|..|........./.........................................../.-.
...............................|....................||....|.|....|./............./.|........./............\...
.......-......................./.............\....-....-...-..\........................................-......
.......-....|.........../................-.....................................|............../...............
.-..................\.../...../\...\.......................\...............-...//..\......\-.|..........|.....
..\............................././\............../....-..........|..\....\.-./...............................
...-.|/...........||......\...-.........................................|.....................................
......|.././...........|......................./.||................\........\........|.|.....\...|....|.......
...-......./............../.....|..-..-.|..-.......|..|....................\...\.......\........|.............
/../.................|............................/.............../....-/..|.....\...|........................
.........-.........|............/.......-.............-...../.\|.......\...-..\.-.....|..../...........-\..|..
......................................\........|..../....|.......\......-.................|...................
...\.......|.....|....\....................-............-....|......\.........\...................|...........
.....\.............\...-........|.............................-|......./.........-............//.......|......
............/../...........-/.........................-...|...|...\............./....-..|..........\\.........
..\......................\/./.........................\..-............-\..-...................................
............................\...|.........|...|.\.......|............/.........|.................\............
............|..|...........\..................../........|............-....-./.....\.-..-.................../.
...................-.-.......-.\............-....\........-./.|../|.../.............\.......\............-....
..../............../........../\...............-.............../......|.\/.........../......|.................
...\......\.....................\..|...............-.......................-.-|....../..................-.....
.........\...\.............|........../.........................................................-...\......-..
..-...........-\.........\....\.............../........\./........../....\......../...........................
............|.............-.../.................|......../..-.........../............./...................\..\
........-...................................-.....\-.........|............../..../...\\.|..........\....-.....
..\..\.\.\.........../..|...\............/...|......................-.........................|...............
\.../...../..........|.....\...|./...|............./......\........................-.....-.....\..............
|....................-..-............................../...../..............-.../...-...|../../.\.............
................/......-...|....|..........\\......-..............|\........|./.\...|.......................|.
........../....................|./..........................|..................-.........|.........|..........
..../.....\...|.......|../....................\...\..-...\...\...........|............./.-.....--.............
.........|-..........................\..-......--......../................\......\...../.|...|....../....-....
.......|.............\............./...............././/../..........\.........|\..........|..................
....\........|.../......./....\./...//.............\..................|./.....................................
..........-.|\............/..-...........\........-....|....../........-.|.................-/.-.........|.../|
.....-\........\........|.|...............................-...........\./..........................-........\.
............../........./../--|.........................-....................\......-..\...\..........\......\
..|...............................\........\......\..\.....-\............|....................................
..\|.................\-......|...............\.........|.|...|........................|..../......-...-|...-..
...........................\......................-.............................|........./......./....-......
.........-..../........../.......|../.....-.........................../.../...........|....-./.\..............
.-........./..-/...........\.......-.......-.........//.-.-......................................|...-........
........../.....|...........\....../\............-......-......../....................|......................-
.......||....-.../....|....../....-.......|...................................................................
.....|./........\.-.....|..................|....\....../......\.......-|.....|../....\...\.\........|./......-
.-.|./............-....../............-..................|....|......-.....\................||.\\.............
....-...-........./.........../.........\....|.\....|..\.\............................-.......//......\..-.\..
...../.........................................|..........|.-|..\./............\.-.../......./............-..|
.../..........\..............\..../...\.........\................./.|....../........|............-...-.-..../.
..\.\................\....../....................|......../\|...../...\....-..../...\.....|..../...\..........
......\..-.\........................-.....................-............|.|.............-...-..................
................\...\...../../....../.../................/.........\.\.................|......................
......................|..................-./.........\..\.......-..........|..\.......\...-...|...............
..........-.........................-................................./......../.....-.|......................
.......-\............./...............-............|.....................-..\.................-......\....-...
..........................................\......./......\........-|..|.....\........\......./................
........//...........-........../......./..............|...../..-..................../...\......-..........-..
./....|..-|...|......-.............\.|.........................\...............-\.............................
|....................|....................../............................../...........\...|...-..............
\......./....|.../.|....................|..............|..................|................\..................
.........|......\.............../....\...................................|.\........./..-.................|./.
......../..................\..................../.........................||./.-.............../..............
......................./.........|.|........-../........./.....|............./......|......-....|...../.......
................|......./............\...-......../..................\..\..../.......\.../.........-/.........
.........-.....\......-.....................-..-.........//...........................|...\-............../...
.....|............-...../.\......................|........|...........\..........|./......./.\.........\../...
..\..........-.../.......|......./.................../............\............|......../....|................
.....\....................-...........-......//...........\....|..\...-.....................\.............../.
..-.....|......\.......|.../......................\...|...\..\.....|...........................\..........|...
....-....-...|.\-...-..\............../......-./...........\/............\-..|.........................\......
......./.....-|.|.......|....\|||......\.............................................\......-.................
.................-\................/.-...............|............|...|.-......-..............................
...|.............|...............|.......-.................-.........|.../..................................|.
..-.../.....-.........................-....|......|/...../....\.............................-...............-.
.|.........-../....................../............|................\.....|........\...........................
.\\............\................-../.../....\.................................|.-.....|.....\.........-.....|.
.............../..................../..\.............-..\.......\...\..../..-........-..../-.....|............
\.................................-..............|...\./......../...........................|.........|......."""

exampleInput = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

directions = {
    "up": 0,
    "right": 1,
    "down": 2,
    "left": 3
}

map = [[*x] for x in input.split("\n")]

def move(mapH, startY, startX, directionz):
    if not(isinstance(startY, int)) or not(isinstance(startX, int)) or directionz < 0:
        print("nope", startY, startX, directionz)
        return -1
    match directionz:
        case 0:
            if startY > 0:
                return [startY - 1, startX]
            else:
                return -1
        case 1:
            if startX < len(mapH[0]) - 1:
                return [startY, startX + 1]
            else:
                return -1
        case 2:
            if startY < len(mapH) - 1:
                return [startY + 1, startX]
            else:
                return -1
        case 3:
            if startX > 0:
                return [startY, startX - 1]
            else:
                return -1
        case _:
            return -1

def go(mapA, start, direction, activated, tab):
    # activated[start[0]][start[1]] += 10 ** direction
    # print("activate", start[0], start[1], 10 ** direction, activated[start[0]][start[1]])
    # print(tab, "starting at", start, direction, mapA[start[0]][start[1]])
    # if (start == -1):
        # print("akurvakfaszat 1")
    # else:
        # print("durva 1", start)
    nextC = move(mapA, start[0], start[1], direction)
    # if nextC == -1:
    #     print(tab, "stopping at", start, direction, mapA[start[0]][start[1]])
    i = 0
    while(nextC != -1):
        i += 1
        # if i >= 14:
        #     print(tab, "running 1", nextC, direction)
        # print(tab, "current move", nextC, direction, mapA[nextC[0]][nextC[1]])
        activated[nextC[0]][nextC[1]] += 10 ** direction
        # print("activate", nextC[0], nextC[1], 10 ** direction, activated[nextC[0]][nextC[1]])
        if mapA[nextC[0]][nextC[1]] == "|" and (direction == directions["right"] or direction == directions["left"]):
            direction = directions["up"]
            go(mapA, nextC, directions["down"], activated, tab + 1)
        if mapA[nextC[0]][nextC[1]] == "-" and (direction == directions["up"] or direction == directions["down"]):
            direction = directions["left"]
            go(mapA, nextC, directions["right"], activated, tab + 1)
        if mapA[nextC[0]][nextC[1]] == "\\":
            if direction == directions["up"]:
                direction = directions["left"]
            elif direction == directions["right"]:
                direction = directions["down"]
            elif direction == directions["down"]:
                direction = directions["right"]
            else:
                direction = directions["up"]
        if mapA[nextC[0]][nextC[1]] == "/":
            if direction == directions["up"]:
                direction = directions["right"]
            elif direction == directions["right"]:
                direction = directions["up"]
            elif direction == directions["down"]:
                direction = directions["left"]
            else:
                direction = directions["down"]
        if (nextC != -1):
            # print("akurvakfaszat 2")
        # else:
            # print("durva 2", nextC)
            nextC = move(mapA, nextC[0], nextC[1], direction)
        # if nextC != -1 and activated[nextC[0]][nextC[1]] > 0:
        #     print("activated", nextC, activated[nextC[0]][nextC[1]], direction, '{:0>4}'.format(activated[nextC[0]][nextC[1]])[3 - direction])
        if nextC != -1 and int('{:0>4}'.format(activated[nextC[0]][nextC[1]])[3 - direction]) > 0:
            nextC = -1
            # print("lol") 
        # if i >= 19 or tab > 10 or (nextC == [6, 1] and direction == 0):
        #     print(tab, "running 2", nextC, direction)
        #     break
        # if nextC == -1:
        #     print(tab, "stopping at", nextC, direction)

def A(startY, startX, direction):
    activated = numpy.zeros((len(map), len(map[0])), dtype=int)
    # activated[0][0] = 10
    go(map, [startY, startX], direction, activated, 0)
    # print(activated)
    totalActivated = 0
    for y in activated:
        for x in y:
            if x > 0:
                totalActivated += 1
    return totalActivated

def B():
    max = 0
    for i in range(len(map[0])):
        current = A(len(map), i, directions["up"])
        if current > max:
            max = current
    print(max)

B()
# 8331