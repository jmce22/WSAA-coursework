# to test that each basic crud operations work as they should

from gymDAO import gymDAO

member = {
  "name":"John Lampard", 
  "sex":"male",
  "age": 47,
  "height":174.5,
  "weight":86.0
  }

#create
#gym = gymDAO.create(member)
#member_id = gym["id"]
# find by id
#result = gymDAO.findByID(member_id);
#print ("test create and find by id")
#print (result)

#update
new_member_values= {"name":"John Lampardo", "sex":"male", "age":45, "height":177.5, "weight":89.0}
gymDAO.update(11,new_member_values)
result = gymDAO.findByID(11);
print("test update")
print (result)

# get all 
#print("test get all")
#allMembers = gymDAO.getAll()
#for member in allMembers:
#  print(member)

# delete
#gymDAO.delete(8)
