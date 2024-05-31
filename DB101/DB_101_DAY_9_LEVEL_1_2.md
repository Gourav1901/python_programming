Give short and concise answer for all the bellow listed questions :
1.What is a NoSQL Database, and explain the types of NoSQL database?
Defination :
NoSQL databases (aka "not only SQL") are non-tabular databases and store data differently than relational tables.
NoSQL databases come in a variety of types based on their data model.
Types
Key-value pair - simpler type of database where each item contains keys and values.
Document-oriented - store data in documents similar to JSON (JavaScript Object Notation) objects.
Column-oriented - store data in tables, rows, and dynamic columns.
Graph-based - store data in nodes and edges.
Example:
MongoDB : A document-oriented database, is a popular NoSQL database that stores data in JSON-like documents with dynamic schemas.
Cassandra : Optimized for handling large amounts of data across many commodity servers, providing high availability with no single point of failure.
Redis : An in-memory key-value store known for its speed and often used as a caching layer.

2.What is the difference between SQL and NoSQL databases?
Difference in Data Modeling :
One of the key differences is the way the data is modeled in the database.
Data Structure:
MySQL: Relational database (RDBMS). Stores data in fixed tables with rows and columns. Enforces relationships between tables using foreign keys.
MongoDB: NoSQL document-oriented database. Stores data in flexible JSON-like documents with various fields. Schema is less rigid and can evolve over time.
Schema:
MySQL: Fixed schema needs to be defined upfront. Changes to the schema can be complex and require downtime.
MongoDB: Schema-less. Documents can have different structures within a collection. Easier to adapt to changing data models.
Transactions:
MySQL: ACID compliant (Atomicity, Consistency, Isolation, Durability). Ensures data integrity in complex operations.
MongoDB: Eventually consistent. Prioritizes performance and scalability over strict ACID guarantees.
Scalability:
MySQL: Vertical scaling (adding more resources to a single server). Can become complex and expensive for very large datasets.
MongoDB: Horizontal scaling (adding more servers to distribute data). Easier to scale for high volume and high-performance applications.

3.How to choose between MongoDB and MySQL based on your requirements?
Choosing between MongoDB and MySQL depends on your project needs:

Data Structure: MongoDB is ideal for unstructured or semi-structured data, offering schema flexibility, while MySQL is suited for structured data with a predefined schema.
Scalability: MongoDB excels in horizontal scaling for large-scale applications, whereas MySQL typically scales vertically.
Transactions: MySQL is robust for complex transactions with strong ACID compliance; MongoDB handles large volumes of simple transactions well.
Use Case: MongoDB fits real-time analytics, CMS, and IoT applications. MySQL is best for e-commerce, banking, and applications needing complex queries and high data consistency.


4.What are collections and documents in a MongoDB database?
In MongoDB, a collection is a group of documents, similar to a table in a relational database. Collections do not enforce a schema, allowing documents within them to have different fields and structures.
A document is a record in a MongoDB collection, analogous to a row in a table. Documents are stored in BSON (Binary JSON) format and consist of field-value pairs. Each document has a unique identifier called _id. Documents in the same collection can have varying fields, providing flexibility in data modeling.
This schema-less design makes MongoDB suitable for applications with evolving data structures.