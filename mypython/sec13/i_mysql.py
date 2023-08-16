import os
import mysql.connector
from mysql.connector import errorcode


def convert_to_binary_data(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

def insert_image_to_table(image_name, filename):
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            passwd='^Kimjml5v2!',
            db='my_emp'
        )

        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS image_table")
        cursor.execute(
            '''
            CREATE TABLE image_table (
            id INT AUTO_INCREMENT,
            image_name VARCHAR(255),
            image_data MEDIUMBLOB,
            PRIMARY KEY (id)
            )       
            '''
        )
        sql_insert = """
            INSERT INTO image_table (image_name, image_data)
            VALUES (%s, %s)
        """
        image_binary = convert_to_binary_data(filename)
        insert_blob_tuple = (image_name, image_binary)
        result = cursor.execute(sql_insert, insert_blob_tuple)
        connection.commit()

    except mysql.connector.Error as error:
        print({error})

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    image_folder = "C:\pywork\img"
    images = os.listdir(image_folder)
    for image in images:
        print(os.path.join(image_folder,image))
        insert_image_to_table(image, os.path.join(image_folder, image))


    '''
    CREATE TABLE image_table (
            id INT AUTO_INCREMENT,
            image_name VARCHAR(255),
            image_data MEDIUMBLOB,
            PRIMARY KEY (id)
    );
    '''
