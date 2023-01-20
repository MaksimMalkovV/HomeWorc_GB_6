from math import sqrt
doc1 = list(map(int, input("Введит две координаты через пробел точки А: ").split()))
doc2 = list(map(int, input("Введит две координаты через пробел точки В: ").split()))
def dist(x,y):
    return sqrt(sum(map(lambda p: (p[0]-p[1])**2,zip(x,y))))
print(f"Расстояние между точками А {doc1} и В {doc2} в 2D пространстве равно -> "+"{0:.3f}".format(dist(doc1,doc2)))