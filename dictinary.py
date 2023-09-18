#used to store info that come as a key value pair.
customers = {
    "name": "Geofry Kimutai",
    "age":23,
    "is_a_programmer": True
}
#to acess it
print(customers.get('sex', "default value"))  