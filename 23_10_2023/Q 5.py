items =[1,2,3,4,5]
try:
   print(items[6])   
except Exception as e:
     print("number is not in the list and", e) 
print(e.__class__)