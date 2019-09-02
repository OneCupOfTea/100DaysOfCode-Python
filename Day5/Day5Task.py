x= "apple"
y= "orange"
z= "limon"

basket= [x , y , z]

n = [5]
[basket[sum(n[:i]):sum(n[:i+1])] for i in range(len(n))]

print(basket)