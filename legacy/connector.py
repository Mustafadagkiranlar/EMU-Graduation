import mysql.connector

def save_palte(plate,location,photo=""):
    connection = mysql.connector.connect(host='localhost',
                                    database='grad',
                                    user='root',
                                    password='Dagkiranlar')
    cursor = connection.cursor()
    query = "INSERT INTO detections (plate, photo_of_vehicle, location) VALUES (%s, %s, %s)"
    values = (plate,photo,location)
    # Execute the query
    print(cursor.execute(query, values))

    connection.commit()

    connection.close()
    cursor.close()

def show_data():
    connection = mysql.connector.connect(host='localhost',
                                        database='test',
                                        user='root',
                                        password='Dagkiranlar')
    cursor = connection.cursor()
    query = "select * from table_test"
    cursor.execute(query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)
    connection.close()
    cursor.close()
    print("\nPrinting each row")
    for row in records:
        print("id = ", row[0], )
        print("text = ", row[1],"\n")

if __name__ == "__main__":
    show_data()