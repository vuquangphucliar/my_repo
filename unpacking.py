def distance():
    points=[(1.2,1.5),(-3.1,5.6),(4.5,2.6),(1.4,6.8),(2.1,-8.4)]
    point2=[]
    for x,y in points:
        tol=abs(x)+abs(y)
        point2.append(tol)
    for i in range(len(point2)):
        if point2[i]== max(point2):
            print(f'Point {points[i]} has max distance to O(0,0): {max(point2)}')
