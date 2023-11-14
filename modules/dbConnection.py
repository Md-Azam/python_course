import mysql.connector

mydb = mysql.connector.connect(host="localhost",username="root",password="Azam@#1234",database='pydb'
                               ,port="3306",charset="utf8")
print(mydb.connection_id)
db_cursor = mydb.cursor()



def delete_data_by_id(id):
    try:
        # Define the DELETE query with a parameterized WHERE clause
        query = "DELETE FROM book WHERE bookid = %s"  # Replace your_table with the actual table name

        # Execute the query with the parameter
        db_cursor.execute(query,(id,))
        mydb.commit()

        print(f"Row with ID {id} deleted successfully.")

    except mysql.connector.Error as err:
        # Rollback changes if an error occurs
        mydb.rollback()
        print(f"Error: {err}")

    finally:
    # Close the cursor and connection
        db_cursor.close()
        mydb.close()
def update_byId(id):
    try:
        # Define the UPDATE query with a parameterized WHERE clause and SET clause
        query = "UPDATE book SET author = %s WHERE bookid = %s"  # Replace your_table and column_name
        author="sanam"

        # Execute the query with the parameters
        db_cursor.execute(query, (author, id))

        # Commit the changes to the database
        mydb.commit()

        print(f"Data with ID {id} updated successfully.")

    except mysql.connector.Error as err:
        # Rollback changes if an error occurs
        mydb.rollback()
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        db_cursor.close()
        mydb.close()
update_byId(4)




