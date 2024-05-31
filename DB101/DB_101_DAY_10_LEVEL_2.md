1.How can you find employees with an id greater than or equal to 10?
Ans. db.user.find({id:{$gte:10}})

2.Find all employees who work in either the "Engineering" or "Marketing" departments.
Ans.db.user.find({'departmenrt':{$in:'Engineering','Marketing'}})

3.How do you find employees whose gender is in ["Female", "Agender", "Non-binary"]?
Ans db.user.find({'gender':{$in:["Female", "Agender", "Non-binary"]}})

4.Write a query to find all employees whose department is not in ["Services", "Human Resources"].
Ans.db.user.find({'department':{$nin:["Services", "Human Resources"]}});

5.How can you find employees whose gender is not in ["Male", "Female"]?
Ans.db.user.find({'gender':{$nin:["Male", "Female"]}});

6.Find employees who have a salary greater than 40000 and work in the "Marketing" department.
Ans.db.user.find({salary:{$gt:40000},department:"Marketing"})

7.How do you find employees whose id is less than 10 and gender is "Male"?
Ans db.user.find({id:{$lt:10},gender:'Male'})

8.Write a query to find employees who either have a salary less than 30000 or work in the "Training" department.
Ans.db.user.find({$or:[{salary:{$lt:30000}},{department:"Training"}]})

9.How can you find employees whose id is either 1, 5, or 10?
Ans db.user.find({id:{$in:[1,5,10]}})

10.Find all employees whose salary is not less than 60000.
Ans.db.user.find(salary:{$gte:60000})

11.How do you find employees whose id is not greater than 15?
Ans.db.user.find({id:{$lte:15}})

12.Write a query to find employees who have the email field.
Ans.db.user.find({email:{$exists:true}})

13.How can you find documents where the projects field does not exist (assuming some employees might have a 'projects' field)?
Ans.
db.user.find({project:{$exists:False}})

14.Retrieve all employees who work in the 'Sales' department, earn more than $60,000, and whose name contains the letter 'r'. Display their names in uppercase, ordered by salary in descending order. Limit the result to 3 entries.
Ans.
db.user.aggregate([
    { $match: { department: 'Sales', salary: { $gt: 60000 }, name: /r/i } },
    { $project: { _id: 0, name: { $toUpper: "$name" }, salary: 1 } },
    { $sort: { salary: -1 } },
    { $limit: 3 }
]);


15.Find employees whose name starts with 'H' and who earn a salary that is either exactly $66,433 or more than $70,000. Display their name in uppercase, email, and salary, sorted by salary in ascending order.
Ans.
 db.user.aggregate([
    { $match: { name: /^H/, $or: [ { salary: 66433 }, { salary: { $gt: 70000 } } ] } },
    { $project: { _id: 0, name: { $toUpper: "$name" }, email: 1, salary: 1 } },
    { $sort: { salary: 1 } }
]);
16.Retrieve the name, email, and department of employees whose salary is between $30,000 and $70,000 and contains the letter 'e' in their name. Display the results in uppercase and sort them by department.
Ans.
db.user.aggregate([
    { $match: { salary: { $gte: 30000, $lte: 70000 }, name: /e/i } },
    { $project: { _id: 0, name: { $toUpper: "$name" }, email: 1, department: 1 } },
    { $sort: { department: 1 } }
]);


17.Retrieve all employees who work in the 'Sales' department, earn more than $60,000, and whose name contains the letter 'r'. Display their names in uppercase, ordered by salary in descending order. Limit the result to 3 entries.
Ans
db.user.aggregate([
    { $match: { department: 'Sales', salary: { $gt: 60000 }, name: /r/i } },
    { $project: { _id: 0, name: { $toUpper: "$name" }, salary: 1 } },
    { $sort: { salary: -1 } },
    { $limit: 3 }
]);

18.Find all employees whose email domain is either 'intel.com' or 'bloglines.com', whose salary is above $60,000. Display their names in lowercase and order the results by name in ascending order, excluding duplicates.
Ans.
db.user.aggregate([
    { $match: { email:  {$regex: /@intel\.com|@bloglines\.com$/ }, salary: { $gt: 60000 } } },
    { $project: { _id: 0, name: { $toLower: "$name" } } },
    { $sort: { name: 1 } },
    { $group: { _id: "$name" } }
]);

19.Retrieve all female employees who work in the 'Marketing' department, earn between $30,000 and $35,000, and whose name starts with the letter 'U'. Display their names in uppercase and sort them by salary in ascending order.
Ans.
db.employees.aggregate([
    { $match: { gender: 'Female', department: 'Marketing', salary: { $gte: 30000, $lte: 35000 }, name: /^U/ } },
    { $project: { _id: 0, name: { $toUpper: "$name" }, salary: 1 } },
    { $sort: { salary: 1 } }
]);

20.Retrieve all employees whose salary is less than $50,000, whose name contains 'a', and who do not work in 'Services'. Display their names and salaries sorted by department and then by salary in descending order.
Ans.
db.user.aggregate([
    { $match: { salary: { $lt: 50000 }, name: /a/i, department: { $ne: 'Services' } } },
    { $project: { _id: 0, name: 1, salary: 1, department: 1 } },
    { $sort: { department: 1, salary: -1 } }
]);

21.List all employees who do not work in the 'Business Development' department, whose names do not contain the letter 'l', and whose salary is greater than $50,000. Display their names in lowercase, ordered by salary in descending order, and limit the result to 5 entries.
Ans.
db.user.aggregate([
    { $match: { department: { $ne: 'Business Development' }, name: { $not: /l/i }, salary: { $gt: 50000 } } },
    { $project: { _id: 0, name: { $toLower: "$name" }, salary: 1 } },
    { $sort: { salary: -1 } },
    { $limit: 5 }
]);

22.List all employees who either work in the 'Sales' department and have a salary less than $65,000, or work in the 'Marketing' department and have a salary greater than $30,000 but not equal to $34,337. Additionally, the employee's name should either start with 'D' or end with 'o'. Display their names in lowercase, ordered by salary in ascending order, and limit the result to 5 entries.
Ans.
db.user.aggregate([
    { $match: { 
        $or: [
            { department: 'Sales', salary: { $lt: 65000 } },
            { department: 'Marketing', salary: { $gt: 30000, $ne: 34337 } }
        ],
        $or: [
            { name: /^D/ },
            { name: /o$/ }
        ]
    } },
    { $project: { _id: 0, name: { $toLower: "$name" }, salary: 1 } },
    { $sort: { salary: 1 } },
    { $limit: 5 }
]);

23.Find all employees who work in the 'Services' department and have a salary more than $60,000, or employees who do not work in the 'Marketing' department and have a salary less than $70,000 but more than $50,000. Additionally, these employees should either have a name that starts with 'A' or their email should contain 'nps.gov'. Display their names in uppercase and emails in lowercase, ordered by name in ascending order, and limit the result to 4 entries.
Ans.
db.user.aggregate([
    { $match: { 
        $or: [
            { department: 'Services', salary: { $gt: 60000 } },
            { department: { $ne: 'Marketing' }, salary: { $gt: 50000, $lt: 70000 } }
        ],
        $or: [
            { name: /^A/ },
            { email: /nps\.gov/i }
        ]
    } },
    { $project: { _id: 0, name: { $toUpper: "$name" }, email: { $toLower: "$email" } } },
    { $sort: { name: 1 } },
    { $limit: 4 }
]);
