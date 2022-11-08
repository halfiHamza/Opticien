from __future__ import print_function
import mysql.connector
from mysql.connector.locales.eng import client_error
from mysql.connector import errorcode
import socket
from dateutil.parser import parse as dateParser
from datetime import datetime


class DbSocket:
    def __init__(self):
        super(DbSocket, self).__init__()
        self._server = 'localhost'
        self._port = 3306
        self._user = 'root'
        self._password = 'AAAAAa1@'
        self._database = 'panorama'
        # _Database tables content _____________________________
        self.tables = [
            '''
            CREATE TABLE IF NOT EXISTS `clients` (
                `id` INT NOT NULL AUTO_INCREMENT,
                `first_name` VARCHAR(255),
                `last_name` VARCHAR(255),
                `age` INT,
                `debt` DECIMAL(12,2),
                `phone` VARCHAR(20),
                `date` DATE,
                PRIMARY KEY(id)
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS `ordonnaces` (
                `id` INT NOT NULL AUTO_INCREMENT,
                `c_id` INT,
                `date` DATE,
                `correction_od` VARCHAR(255),
                `type_verre_od` VARCHAR(255),
                `correction_og` VARCHAR(255),
                `type_verre_og` VARCHAR(255),
                `add_og` VARCHAR(255),
                `ad_dog` VARCHAR(255),
                `remarque` VARCHAR(255),
                `prix_monture` DECIMAL(12,2),
                `total` DECIMAL(12,2),
                `verssment` DECIMAL(12,2),
                `rest` DECIMAL(12,2),
                PRIMARY KEY(id)
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS `pwd` (
                `id` INT NOT NULL AUTO_INCREMENT,
                `pwd` VARCHAR(255),
                PRIMARY KEY(id)
            );
            ''',
            '''INSERT INTO pwd(pwd) VALUE('admin');'''
        ]
        try:
            # _ Create tables if not exists ____________________
            for q in self.tables:
                self.execute_query(q)
        except:
            return None

        self.create_database()
        self.CreateTables()

    def real_ip(self, address):
        try:
            ip_address = socket.gethostbyname(address)
            return ip_address
        except socket.gaierror:
            return address

    def create_database(self):
        try:
            socket = mysql.connector.connect(user=self._user,
                                             password=self._password,
                                             host=self.real_ip(self._server),
                                             port=self._port)
            cursor = socket.cursor()
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {self._database}")
            socket.commit()
            return True
        except mysql.connector.Error as error:
            print(error)

    def execute_query(self, query, *args):
        try:
            socket = mysql.connector.connect(host=self.real_ip(self._server),
                                             port=self._port,
                                             user=self._user,
                                             password=self._password,
                                             database=self._database)
            socket.autocommit = True
            cursor = socket.cursor()
            cursor.execute(query, *args)
            result = cursor.fetchall()
            if result:
                return result
        except mysql.connector.Error as e:
            print(e)

    def CreateTables(self):
        global querys
        try:
            for q in self.tables:
                self.execute_query(q)
        except:
            return False

    # _ Insert new client to database ___________________________
    def clientInsert(self, data):
        try:
            self.execute_query(
                "INSERT INTO clients(first_name, last_name, age, phone, debt, date) VALUES(%s, %s, %s, %s, %s, %s)", tuple(
                    data)
            )

            return True
        except:
            return False

    # _ Insert new ordonnace to database ________________________
    def ordInsert(self, data):
        try:
            self.execute_query(
                "INSERT INTO ordonnaces(c_id, date, correction_od, type_verre_od, correction_og, type_verre_og, add_og, ad_dog, remarque, prix_monture, total, verssment, rest) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", tuple(data)
            )

            self.execute_query(
                f"UPDATE clients SET debt = debt + {data[-1]} WHERE id = {data[0]}"
            )

            return True
        except:
            return False
    
    # _ Edit old ordonnace in database ________________________
    def ordEdit(self, data):
        try:
            self.execute_query(
                f"UPDATE ordonnaces SET date='{data[1]}', "
                f"correction_od='{data[2]}', "
                f"type_verre_od='{data[3]}', "
                f"correction_og='{data[4]}', "
                f"type_verre_og='{data[5]}', "
                f"add_og='{data[6]}', "
                f"ad_dog='{data[7]}', "
                f"remarque='{data[8]}', "
                f"prix_monture={data[9]}, "
                f"total={data[10]}, "
                f"verssment={data[11]}, "
                f"rest={data[12]} WHERE id = {data[0]}"
            )

            # self.execute_query(
            #     f"UPDATE clients SET debt = debt + {data[-1]} WHERE id = {data[0]}"
            # )

            return True
        except:
            return False

    # _ Select ordonnace by client id ________________________
    def ordSelect(self, c_id):
        try:
            result = self.execute_query(
                f"SELECT id, DATE_FORMAT(date, '%d-%M-%Y'), correction_od, type_verre_od, correction_og, type_verre_og, add_og, ad_dog, remarque, CONCAT(CAST(prix_monture AS CHAR), ' Da'), CONCAT(CAST(total AS CHAR), ' Da'), CONCAT(CAST(verssment AS CHAR), ' Da'), CONCAT(CAST(rest AS CHAR), ' Da') FROM ordonnaces WHERE c_id = {c_id}"
            )
            return result
        except:
            return False

    # _ Delete client from database ___________________________
    def deleteClient(self, id):
        try:
            self.execute_query(
                f"DELETE FROM clients WHERE id = {id}"
            )
            self.execute_query(
                f"DELETE FROM ordonnaces WHERE c_id = {id}"
            )
            return True
        except:
            return False

    # _ Get client from database ___________________________
    def getClient(self, id):
        try:
            result = self.execute_query(
                f"SELECT * FROM clients WHERE id = {id}"
            )
            return result
        except:
            return False

    # _ Edit client on database ___________________________
    def editClient(self, id, data):
        try:
            self.execute_query(
                f"UPDATE clients SET first_name = '{data[0]}', last_name = '{data[1]}', age = {data[2]}, debt = {data[3]}, phone = '{data[4]}' WHERE id = {id}"
            )
            return True
        except:
            return False

    # _Get amount and frames quantity of each day ________________
    def dailyAmount(self):
        result = self.execute_query(
            f"SELECT DATE_FORMAT(date, '%d-%M-%Y'), COUNT(prix_monture), CONCAT(CAST(SUM(prix_monture) AS CHAR), ' Da') FROM ordonnaces WHERE prix_monture > 0 GROUP BY date"
        )
        return result

    # _Get amount and frames quantity of each month ________________
    def monthlyAmount(self):
        final = []
        result = self.execute_query(
            f"SELECT MONTH(date) AS month, DATE_FORMAT(date, '%M-%Y'), count(prix_monture), CONCAT(CAST(SUM(prix_monture) AS CHAR), ' Da') FROM ordonnaces WHERE prix_monture > 0 GROUP BY month;"
        )
        if result:
            for i in result:
                final.append(list(i)[1:])

        return final

    # Get day details _________
    def dayDetails(self, day):
        result = self.execute_query(
            f"SELECT CONCAT(CAST(prix_monture AS CHAR), ' Da') FROM ordonnaces WHERE prix_monture > 0 AND date = '{dateParser(day)}'"
        )
        if result:
            final = {item[0]: result.count(item) for item in result}
            return [(k, v) for v, k in final.items()]

    # Get week details _________
    def monthDetails(self, date):
        datem = datetime.strptime(date, "%B-%Y")
        result = self.execute_query(
            f"SELECT CONCAT(CAST(prix_monture AS CHAR), ' Da') FROM ordonnaces WHERE prix_monture > 0 AND MONTH(date) = {datem.month} AND YEAR(date) = {datem.year}"
        )
        if result:
            final = {item[0]: result.count(item) for item in result}
            return [(k, v) for v, k in final.items()]

    def cashActual(self):
        result = self.execute_query(
            "SELECT CONCAT(CAST(total AS CHAR), ' Da') FROM ordonnaces WHERE date = CURDATE()"
        )
        if result:
            return result[0][0]
