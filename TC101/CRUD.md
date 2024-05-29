#crud operation in mongoDB

   crerat -> insertOne, insterMany 

   collection -> user

   db.user.insterOne([{name:"Gourav",age:23,phone:3444534424}])
   db.user.insertMany([{name:"Gourav",age:43,phone:3444534424},
                       {name:"Gourav",age:56,phone:3444534424},
                       {name:"Gourav",age:24,phone:3444534424},
                       {name:"Gourav",age:23,phone:3444534424},
                       ])

  find ,findOne

  db.user.find()
  db.user.find({name:"Gourav"})

  operation -> updateOne,updateMany

  db.user.updateOne({obj_id:1{$set{phone:489485594}}})
  db.user.updateMany({city:"Indore"},{$set:{Indre,M.P}})

  operation deleteOne, deleteMany

  db.user.deleteOne({objid:1})
  db,user.deleteMany({name:"Gourav"})      
