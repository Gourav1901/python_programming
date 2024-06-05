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