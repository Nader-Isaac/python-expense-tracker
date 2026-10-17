# personal expenses tracker 
expeneses = {"food" : 15 , "transport" : 10 , "clothes" : 70 , "coffe" : 5 , "books" : 20}
print(expeneses.items())
for name , amount in expeneses.items():
    print(f"{name} : {amount}")
expeneses_list = list(expeneses.items())    
print(expeneses_list)   
print(expeneses_list[0])
print(expeneses_list[-1]) 
total = 0
for value in expeneses.values():
    total =+ value
print(f"your total expnes is : {total}")
budget = 100
if total >= budget : 
    print ("you reach your daily budget")
else:
    print(f"you still have a {budget - total} in your daily budget !")    