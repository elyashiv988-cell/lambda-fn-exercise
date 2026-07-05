 
# 1 manager son price

manager_son_price=lambda price, is_manager_son : price-price/100*20 if is_manager_son else price+price/100*17

print(manager_son_price(100,True))

# 2 final price after discount

final_price=lambda price,discount: price-discount if 0<discount<=100 else price
print(final_price(100,20))

# 3 full name

full_name= lambda first_name, last_name: first_name+" "+last_name
print(full_name("eli","cohen"))

# 4 grade status

grade_status= lambda grade: "pass" if grade<=55 else "fail"
print(grade_status(40))

# 5 larger number

larger=lambda n1,n2: n1 if n1>=n2 else n2
print(larger(4,7))

# 6 distance from 10

distance_from_10= lambda num: 10-num if num<10 else num-10
print(distance_from_10(14))

# 7 get item total

item_total=lambda item : item["price"]*item["amount"]
print(item_total({"name": "Pen", "price": 5, "amount": 10}))

# 8 Turn a regular complex function into a lambda

shipping_cost= lambda weight,express: 50 if weight>5 and express else 30 if express else 25 if weight >5 else 10
print(shipping_cost(3,True))
print(shipping_cost(8,True))
print(shipping_cost(8,False))
print(shipping_cost(2,False))

# 9 Turn a regular complex function into a lambda

access_message=lambda age,has_ticket,is_vip: "vip entrance" if is_vip else "regular entrance" if age>=18 and has_ticket else "buy ticket" if age>=18 else "too toung"
print(access_message(25, True, False))
print(access_message(25, False, False))
print(access_message(15, True, False))
print(access_message(15, False, True))

# 10 Turn a complex lambda into a regular function
 
def ticket_price(age,is_student):
    if age<12:
        return 20
    elif is_student:
        return 30
    else:
        return 50

print(ticket_price(10, False))
print(ticket_price(20, True))
print(ticket_price(20, False))


