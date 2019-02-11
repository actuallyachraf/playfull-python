from statistics import mean


def best_fit(points):

    x_ = mean([p[0] for p in points])
    y_ = mean([p[1] for p in points])


    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    
    

    top = sum([(x - x_)*(y - y_) for (x,y) in zip(xs,ys)])

    bottom = sum([(x-x_)**2 for x in xs])

    slope = top / bottom

    intercept = y_ - (slope * x_)


    return (slope,intercept)


if __name__ == '__main__' :

    points = [(8,3),(2,10),(11,3),(6,6),(5,8),(4,12),(12,1),(9,4),(6,9),(1,14)]


    print(best_fit(points))
