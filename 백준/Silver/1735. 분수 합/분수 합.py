import math
a,b=map(int,input().split())
c,d=map(int,input().split())
down=math.lcm(b,d)
up=(down//b)*a+(down//d)*c
second=math.gcd(up,down)
up=up//second
down=down//second
print(up,down)