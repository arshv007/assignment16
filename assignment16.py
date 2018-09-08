#Ques1
import pymongo
client=pymongo.MongoClient()
database=client['Students']
print('STUDENTS DATABASE CREATED')
collection=database['Student Data']
print('STUDENTS DATA TABLE CREATED')
#Ques2 & ques 3 combined
for i in range (1,11):
    print('Enter Detail Of Student {}:'.format(i))
    name=input('Name:')
    marks=int(input('Marks:'))
    collection.insert_one({'Name':name,'Marks':marks})
print('VALUES INSERTED')
#Ques4
data=collection.find({'Marks':{"$gt" : 80}})
for details in data:
    print('MARKS GREATER THAN 80',details)

