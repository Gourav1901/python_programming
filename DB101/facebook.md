//Facebook

// user  - name, email

{
  _id:Object(),
  username:string,
  email:string,
  password_hash:string,

  profile:{
    firstName:string,
    LastName:string,
    gender:string,
    bio:string,
    age:int32,
    coverImage:string
  },

  contact: {
    phone:string,
    address:string,

  },
  
  settingConfigs:{
    privacy:string,
    notification:{
      email:boolean,
      phone:boolean
    }
  },

  createdAt:ISODate,
  updatedAt:ISODate

}


//post - title,image,content

{
  _id:ObjectID,
  title:string,
  content:string,
  createdAt:ISODate,
  updatedAt:ISODate,
}

//Comments - text, data, likes

{
  _id:ObjectID,
  description:string,
  createdAt:ISODate,
  updatedAt:ISODate,
},

//Friendship -- map

{

}

//Likes
{
  _id:ObjectID,

}





