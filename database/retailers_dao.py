from typing import List

from database.DB_connect import DBConnect
from model.retailer import Retailer

class RetailersDAO:

    @staticmethod
    def get_retailers() -> set[Retailer] | None:
        cnx =DBConnect.get_connection()
        result = set()
        query = """SELECT DISTINCT * FROM go_retailers"""
        if cnx is not None:
            cursor = cnx.cursor(dictionary = True)
            cursor.execute(query)
            for row in cursor.fetchall():
                read_retailer = Retailer(row["Retailer_code"],
                                         row["Retailer_name"],
                                         row["Type"],
                                         row["Country"])
                result.add(read_retailer)
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore di connessione")
            return None

    @staticmethod
    def get_retailer(retailer_code) -> Retailer | None:
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT gr.*
                            FROM go_retailers gr
                            WHERE Retailer_code =%s"""
            cursor.execute(query, (retailer_code,))
            row = cursor.fetchone()
            row_product = Retailer(row["Retailer_code"],
                                  row["Retailer_name"],
                                  row["Type"],
                                  row["Country"])
            cursor.close()
            cnx.close()
            return row_product
        else:
            print("Errore nella connessione")
            return None

