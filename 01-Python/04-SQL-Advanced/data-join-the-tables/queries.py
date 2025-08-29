# pylint:disable=C0111,C0103
import sqlite3
conn = sqlite3.connect('data/ecommerce.sqlite')
c = conn.cursor()


def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    query = """
    SELECT ord.OrderID as order_id,
    cus.ContactName as customer_name,
    emp.FirstName as employee_first_name
    FROM Orders ord
    JOIN Employees emp ON emp.EmployeeID = ord.EmployeeID
    JOIN Customers cus ON cus.CustomerID = ord.CustomerID
    ORDER BY ord.OrderID
    """
    db.execute(query)
    results = db.fetchall()
    return results

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    query= """SELECT c.ContactName,
    ROUND(SUM(od.UnitPrice * od.Quantity),2) AS total
    FROM OrderDetails od
    JOIN Orders o
    ON o.OrderID = od.OrderID
    JOIN Customers c
    ON o.CustomerID = c.CustomerID
    GROUP BY c.ContactName
    ORDER BY total ASC
    """
    db.execute(query)
    results = db.fetchall()
    return results


def best_employee(db):
    '''Implement the best_employee method to determine who’s
    the best employee!
    By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like:
    ('FirstName', 'LastName', 6000 (the sum of all purchase)).
    The order of the information is irrelevant'''

    query = """SELECT e.FirstName, e.LastName,
    ROUND(SUM(od.UnitPrice * od.Quantity),2) AS total
    FROM OrderDetails od
    JOIN Orders o
    ON o.OrderID = od.OrderID
    JOIN Employees e
    ON o.EmployeeID = e.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY total DESC
    """
    db.execute(query)
    results = db.fetchall()
    return results[0]

def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query = """WITH Totalordens AS (
SELECT c.ContactName,
    COUNT(o.OrderID) AS total
    FROM Orders o
    JOIN Customers c
    ON o.CustomerID = c.CustomerID
    GROUP BY c.ContactName
    )
SELECT Customers.ContactName,
COALESCE(Totalordens.total,0)
FROM Customers
LEFT JOIN Totalordens
ON Totalordens.ContactName = Customers.ContactName
ORDER BY total ASC
"""

    db.execute(query)
    results = db.fetchall()
    return results
