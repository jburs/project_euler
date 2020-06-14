#
# sum of multiples of 3 or 5 below 1000
#
#

x,sum,y=3,0,5
store3=[0]
store5=[0]
while(x < 1000):
    sum += x
    store3.append(x)
    x+=3

while(y < 1000):
    if not y in store3:
        sum=sum+y
        store5.append(y)
    y+=5


print (sum)
print (store3)
print (store5)
