# employee id=100 name=vipin  department=hr salary=25000

# create a dictionary product with keys id,title,price,brand

product={"id":1000,"title":"goodday","price":35,"brand":"britania"}

print(product["price"]) #display product price

# update product price as 50

product["brand"]="parle"

print(product)

product["use_by_date"]="12-10-2024"

print(product)

product["price"]=100

print(product)


product["offer"]=5

print(product)

# chk key is exist or not

# exist
# not exist

# add offer as 10 if offer  exist else add offer as 20

if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)