
steps = 0
def foo(n):
    global steps
    if len(str(n)) == 1:
        return steps
    steps += 1;
    return foo( eval('*'.join([ x for x in str(n) ])) )

def r( n ):
    string = '*'.join([ x for x in str( n ) ])
    print(eval( string ))

def diz(n,d):
    c,r = 0,n
    while True:
        rf = r / d
        if not ((rf-int(rf)) == 0): break
        c += 1; r = rf
    return c

def d( n ):
    dig = [int(x) for x in str(n)]
    c2,c3,c7 = 0,0,0
    for x in dig:
        c2 += diz(x,2)
        c3 += diz(x,3)
        c7 += diz(x,7)

def nn(r,min,max):
    global steps
    r1,r2,r3 = 0,0,0

    for x in range(min,max):
        for y in range(min,max):
            for z in range(min,max):
                number = "2"*x + "3"*y + "7"*z
                if number == '':
                    continue

                steps = 0
                steps = foo(number)

                if steps == r:
                    print('Multiplicative Prersistence nº: 2^{} * 3^{} * 7^{} :'.format(x,y,z) ,number )
                    exit()

pp = [ 2,11,29,47,277,769,6788,68889,2677889,26888999,3778888999,277777788888899 ]
for x in pp:
    steps = 0
    foo(x)
    d(x)
    print('-'*20+ ': ' + str(x),steps)

# nn( number of steps, minmum multiplayer, maxmum multiplayer )
nn( 9 , 0, 50 )
