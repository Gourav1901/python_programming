Give short and concise answer for all the bellow listed questions :
1.How do you list all the databases present in your MongoDB server?
show databases or show dbs 

2.What command is used to create or switch to a database in MongoDB?
   use newb101

3.How can you create a collection named "students" in your MongoDB database?
   db.createCollection("students")

4.Write the command to insert a single document into the "students" collection with at 
least three fields: name, age, and course.
db.students.insertOne({"name" : "Ram" , "age" : 23, "course" : "DB101"})

5.How would you insert multiple documents into the "students" collection in a single command?
db.students.insertMany( [ {"name" : "Raju" , "age" : 21, "course" : "DB101"}])

6.What command is used to find or read all documents in the "students" collection?
db.students.find()

7.How can you read or find the first document in the "students" collection?
db.students.findOne()

8.Describe the command to update the course field of a specific student named "John Doe" to "Data Science".
db.students.updateOne({"name": "John due"}, {$set : {"course": "Data Science"}})

9.What command would you use to increment the age field of all documents in the "students" collection by 1?
db.students.updateMany({"course": "DB101"}, {$inc: {"age": 1}})  # inc increment 

10.How can you delete a document with a specific name from the "students" collection?
db.students.deleteOne({"name" : "Ram"})

11.Write the command to delete all documents from the "students" collection where the age is greater than or 
equal to a specific value.
db.students.deleteMany({"age" : {$gte : 25}})    #gte  greater than 

12.How do you find documents in the "students" collection where the course field is "Data Science"?
db.students.findOne({"course":"Data Science"})