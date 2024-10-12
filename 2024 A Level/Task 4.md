>Name your Jupyter Notebook as:
>
>`TASK4_<your name>_<centre number>_<index number>.ipynb`

# Task 4

A holiday company has 10 villas that customers can hire. A program is being created to store the customer bookings and allow the company staff to check the availability of the villas on requested dates.

The text files `customerBookings.txt` and `villas.txt` store the current data.

The data in `villas.txt` is stored in the following format:

```plaintext
villa ID, villa name, country, cost
```

The data in `customerBookings.txt` is stored in the following format:

```plaintext
booking ID, customer ID, villa ID, start date, number of days
```

You do not need to consider how data about the customers will be stored.

You can assume the year is 2025.

For each of the sub-tasks, add a comment statement at the beginning of the code, using the hash symbol `#`, to indicate the sub-task the program code belongs to, for example:

<pre>
# Task 4.1
Program code
</pre>

---

## Task 4.1

Write a Python program that uses SQL to create a database with two tables: one table to store data about the villas and one table to store data about customer bookings.

Define the primary and foreign keys for each table.

[7]

---

## Task 4.2

Write a Python program that uses SQL to insert the data from each of the two text files into the appropriate field in each database table.

[4]

Run your program to test the data has been entered correctly.

[1]

---

## Task 4.3

A new table `Villa_Booking` needs creating to store every date that each villa has been booked.

This will have two fields: one for the villa ID and one for the date.

For example, if villa number 1 is booked from the 01-Jan for 4 days, the following data will be inserted into `Villa_Booking`:

```plaintext
1    01-Jan
1    02-Jan
1    03-Jan
1    04-Jan
```

Write a Python program that uses SQL to create `Villa_Booking` and populate it with the existing customer bookings.

[5]

---

## Task 4.4

Write a Python function to:
- take as input the villa name, start date, and number of days a customer would like to book
- use SQL to check the availability of the villa for the customer's request
- output a list of all the requested dates that the villa is available
- output a list of all the requested dates that the villa is not available.

All outputs must have an appropriate message.

[6]

Test your program with the following data:

- Villa name: `Dolphin`
- Month: `Apr`
- Date: `8`
- Number of days: `4`

[1]

Save your Jupyter Notebook for Task 4.
