1.Write a MongoDB query to increase the salary of all employees in the 'Sales' department by 5%.
Ans db.user.updateMany({department:"Sales"},{$mul:{salary:1.05}})

2.How would you update the salary of the employee with id: 10 to increase it by 10%?
Ans. db.user.updateMany({id:10},{$mul:{salary:1.10}})

3.Create a MongoDB query that sets the minimum salary to 35000 for all employees in the 'Engineering' department whose salary is currently below this value.
Ans.db.user.updateMany({department:"Engineering",salary:{$lt:35000}},{$set:{salary:35000}})

4.How can you ensure the salary of the employee with id: 5 is not more than 32000? Use a MongoDB query to adjust if necessary.
Ans db.user.updateOne({id:5,salary:{$gt:32000}},{$set:{salary:32000}})


5.Write a query to remove the email field from all employees in the 'Marketing' department.
Ans db.user.updateMany({department:"Marketing"},{$unset:{email:""}})

6.How would you double the salary of the employee with id: 3 using a MongoDB query?
Ans.db.user.updateOne({id:3},{$mul:{salary:2}})

7.Suppose the field 'department' has been decided to be renamed to 'division' across
 the database. How would you update the structure for the employee with id: 2?
Ans db.user.updateOne({id:2},{$rename:{"department":"division"}})

8.Write a MongoDB query to insert a new employee with id: 21, name: 'Alexa', gender: 'Female', salary: 55000, and department: 'IT' if no employee with id: 21 exists.
Ans. db.user.updateOne({id:21},{$setOnInsert:{name: 'Alexa', gender: 'Female', salary: 55000, 'department': 'IT'}},{$upsert : true})

9.How can you add 'projectAlpha' to a new array field named 'projects' for the employee with id: 4?
Ans db.user.updateOne({id:4},{$setOnAdd:{'projects':'projectAlpha'}});

10.If you need to add multiple projects ('projectBeta', 'projectGamma') to the 'projects' array for the employee with id: 7, how would you construct the MongoDB query?
Ans db.user.updateOne({id:7},{$addToSet:{'projects':{$each:['projectBeta','projectgama']}}})

11.Write a query to remove the last project from the 'projects' array for the employee with id: 4.
Ans. db.user.updateOne({id:4},{$pop:{projects:1}})

12.Construct a MongoDB query to remove the first project from the 'projects' array for the employee with id: 7.
Ans. db.user.updateOne({id:7},{$pop:{'projets': -1}})

13.How can you remove 'projectBeta' from the 'projects' array for any employee that has it listed, for instance, the employee with id: 7?
Ans. db.user.updateOne({id:7},{$pull:{'projects':'projectBeta'}})

14.How do you find the employee with an id exactly equal to 5?
Ans.db.user.findOne({id:5});

15.Write a MongoDB query to find the employee whose department is exactly "Business Development".
Ans.db.user.find({'department':'Business Development'})

16.How can you find all employees whose gender is not "Male"?
Ans.db.user.find({'gender':{$ne:"Male"}}) 

17.Write a query to find all documents where the department is not "Sales".
Ans.db.user.find({'department':{$ne:"Sales"}})

18.Find all employees whose salary is greater than 50000.
Ans. db.user.find({'salary':{$gt:5000}});

20.How do you find all employees with an id greater than 15?
Ans. db.user.find({id:{$gt:15}})

21.Write a query to find all employees whose salary is greater than or equal to 80000.
Ans.db.user.find({'salary':{$gte:80000}});