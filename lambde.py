 
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