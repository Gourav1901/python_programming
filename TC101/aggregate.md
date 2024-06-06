db.collection.aggregate([
  {
    $match: {
      RATING: { $gt: 3.5 }
    }
  }
])

db.collection.aggregate([
  {
    $match:{
      rating:{$gt:3.5}
    }
  }
])

db.collection.aggregate([
  $match{
    rating:{$gt:3.5}
  },
  {
  $limit:5
  },
  {
    $sort:{
      rating:-1
    }
  }
])


db.collection.aggragate([
  $match:{
    rating:{$gt:3.5}
  },
  {$limit:5},
  {$sort:rating:-1}
])




db.collection.aggragate([{$match:
{rataing:{$gt:3.5},
{$limit:5},
{$skip:3}
{$sort:{$rating:-1}}
}
}])



orders    customer
ID               on Id 
                   
customerd         custimerID
orderId             name email
product 
quantity

db.orders.aggregate([
  $lockups:{
    localfeild:customerID,
    Foregien customerID,

  }
])


db.orders.aggregate([
  {$lockup:{
    from:"customer_id",
    localField:"customer_id",
    as:"customerDetails"
   }
  },
  {
    $unwind:""
  }
])





orders     customers

id           id
orderid      customerId
customerid   name 
product     email
quantity


db.orders.aggragte([
  {$lookup{
    from:"orders",
    localField:"customerid",
    ForeignField:"customerid",

  }
  AS:"$customerDetails"
  }

  {$unwind:"$customerDetails"}
])