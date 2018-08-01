import random

class point:
    count = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
        point.count +=1

    def __hash__(self) -> int:
        hash = 3
        hash = 71 * hash + self.x
        hash = 71 * hash + self.y
        return hash

    def __eq__(self, o: object) -> bool:
        return (self.x == o.x and self.y == o.y)


if __name__ == '__main__':

    list_point = set()
    for i in range(0,1000):
        list_point.add(point(random.randint(0,1000),random.randint(0,1000)))
    count = 0
    # print (list_point)
    while(count<1000):
        for i in list_point:
            count += 1
        if(count <1000):
            for i in range(1000-count,1000):
                list_point.add(point(random.randint(0, 1000), random.randint(0, 1000)))

    with open("output.txt","w") as file:
        for i in list_point:
            file.write(str(i.x)+" "+str(i.y)+"\n")
        file.close()
