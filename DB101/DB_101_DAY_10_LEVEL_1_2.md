Give short and concise answer for all the bellow listed questions :
1.Explain about data types in mongodb
MongoDB Server stores data using the BSON format which supports some additional data types that are not available using the JSON format.
String - Stores string values; it's UTF-8 encoded.
Boolean - Stores a true or false value.
Number (Int32 , Long , Decimal)
Int: A 32-bit integer.
NumberLong: A 64-bit integer, suitable for storing larger numbers.
NumberDecimal: Provides precise decimal representation, useful for financial calculations.
Timestamp - Stores a Unix timestamp (the number of seconds since the Unix epoch).
ObjectID - A unique identifier for documents, typically used as the primary key.
Array - Can hold multiple values, including nested arrays.
Embedded Documents: Allows embedding of document structures within a document.
Date
Date() method which returns the current date as a string.
new Date() constructor which returns a Date object using the ISODate() wrapper.
ISODate() constructor which returns a Date object using the ISODate() wrapper.

2.What is mongo compass and what is mongo shell ?
Mongo Compass, the GUI for MongoDB, allows for easy data import and export:
Import: Can import data from JSON or CSV files into a collection.
Export: Allows exporting data from a collection to a JSON or CSV file.
In MongoDB shell (mongosh), you can use JavaScript's typeof operator to check the type of a field within a returned document:

3.What is ordered and unordered insert operation ?
Ordered :
Ordered: MongoDB processes the insert operations in the order provided. If an error occurs, MongoDB stops the operation.

db.test.insertMany(
  [
    { _id: 1, name: "Raj" },
    { _id: 1, name: "rahul" },
    { _id: 2, name: "Bishal" },
  ],
  { ordered: true }
);
Unordered :
Unordered: Specified with { ordered: false }, allows MongoDB to continue processing insert operations even if one fails.

db.test.insertMany(
  [
    { _id: 1, name: "Raj" },
    { _id: 1, name: "rahul" },
    { _id: 2, name: "Bishal" },
  ],
  { ordered: false }
);

4.Explain about Comparison Operators in mongodb
Comparison Operators
Descriptions
$eq: Matches values that are equal to a specified value.
$ne: Matches all values that are not equal to a specified value.
$gt, $lt, $gte, $lte: Used for greater than, less than, greater than or equal to, and less than or equal to operations.
$in: Matches any of the values specified in an array.
$nin: Matches none of the values specified in an array.

5.Explain about Logical Operators in MongoDB
Logical Operators
Descriptions
$and: Joins query clauses with a logical AND, returns all documents that match the conditions.
$or: Joins query clauses with a logical OR, returns all documents that match any condition.
$not: Inverts the effect of a query expression and returns documents that do not match the expression.

6.Explain about Element Operators in mongodb.
Element Operators
Description :
$exists : Matches documents that have the specified field.
$type : Selects documents if a field is of the specified type.
$size : Selects documents if the array field is a specified size.
Example :
1. $exists: Matches Documents that Have the Specified Field
This operator can be used to find documents where a specific field either exists or does not exist.

Example: Find hotels that have a CATEGORY field.

db.hotels.find({ CATEGORY: { $exists: true } });
2. $type: Selects Documents if a Field is of the Specified Type
This operator allows you to select documents where a field is of a specific type, such as string, integer, array, etc. MongoDB uses BSON types for this operation, so you'll need to refer to MongoDB's BSON type documentation for the specific codes or type aliases.

Example: Find hotels where RATING is stored as a double (BSON type).

db.hotels.find({ RATING: { $type: "double" } });
3. $size: Selects Documents if the Array Field is a Specified Size
This operator is useful for querying documents based on the size of an array field.

Example: Find hotels that offer exactly 3 amenities.
db.hotels.find({ AMENITYS: { $size: 3 } });
