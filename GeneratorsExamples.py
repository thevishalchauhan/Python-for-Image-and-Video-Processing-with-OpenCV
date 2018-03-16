def take(count,iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter +=1
        yield item


def distinct(iterable):
    seems = set()
    for item in iterable:
        if item in seems:
            continue
        yield item
        seems.add(item)

def pipeline():
    items = [1,1,2,3,4,5,5,4]
    for item in take(3,distinct(items)):
        print(item)

def lucas():
    yield 0
    a = 0
    b = 1
    while True:
        a,b=b,a+b
        yield a
        if a > 30:
            return
    
if __name__ == "__main__":
    pipeline()
    for i in lucas():
        print(i)
    import time
    start = time.time()
    print(sum(x*x for x in range(1,100001) if x%2==0))
    print(time.time()-start)
