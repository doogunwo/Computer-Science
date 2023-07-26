def solution(wallpaper):
    answer = []
    y1 = []
    x1 = []
    for y in range(wallpaper):
        
        for x in range(len(wallpaper[y])):
            
            if wall[y][x] == "#":
                
                y1.append[y]
                x1.append[x]
    
    return answer

wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
answer = solution(wallpaper)
