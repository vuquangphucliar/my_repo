class Vector:
    def __init__(self,point) -> None:
        self.point=point


    def __add__(self,other):
        if len(self.point)!=len(other.point):
            print('Size Error!')
        else:
            a=[]
            for i in range(len(self.point)):
                a.append(self.point[i]+other.point[i])
            return a

    def __sub__(self,other):
        if len(self.point)!=len(other.point):
            print('Size Error!')
        else:
            hieu=[]
            for i in range(len(self.point)):
                hieu.append(self.point[i]-other.point[i])
            return hieu

    def __mul__(self,other):
        tich=0
        for i in range(len(self.point)):
            tich+=self.point[i]*other.point[i]
        return tich

    def __eq__(self,other):
        if len(self.point)!=len(other.point):
            print('Size Error!')
        else:
            if set(self.point)|set(other.point)==set(self.point):
                return True
            else:
                return False

vt1=input().split()
vt2=input().split()

vt1=list(map(lambda x : float(x) ,vt1))
vt2=list(map(lambda x : float(x) ,vt2))

vector1=Vector(vt1)
vector2=Vector(vt2)

print(vector1+vector2)
print(vector1-vector2)
print(vector1*vector2)
print(vector1==vector2)
