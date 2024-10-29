You are tasked to create a web application for a factory admin, just that he only knows how to "click here and type there".
The webapp will generally allow the admin to input and output information like Factory status and goods produced using HTML forms while you will code how it interacts with the database.
# Task 1
Create a database "FACTORY.db".

Create a table "Good" which is the type of goods produced in the factory. It has the following attributes:
- GoodName
- Category
- GoodID

Create a table "Production" which contains the details of each production in the factory:
- ProductionID
- GoodID
- MachineID
- Quantity
- Quality

Create a table "Machine" which contains the details of each machine in the factory:
- MachineID (auto incremented)
- MachineName
- Status

# Task 2
Create a Web Application that executes an appropriate query and displays a table containing ProductionID, GoodName, Quantity, Quality, MachineName and Status for each production.

Add a form for each row that allows the user to delete the production.

# Task 3
Add a form below the table that allows the user to enter a production with the following details:
- GoodID
- Category
- Quantity
- Quality
- MachineID
Use program code in the server (including database querying) to validate if any good in the database and machine matches the respective IDs. Insert the new production if both IDs match. Display a suitable message for both cases.
