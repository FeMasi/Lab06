from database.DB_connect import DBConnect
from model.product import Product

class ProductDao:

    @staticmethod
    def get_brands() -> list[tuple[str]]:
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = ("""SELECT DISTINCT gp.Product_brand
                        FROM go_products gp""")
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            cnx.close()
            return rows
        else:
            print("Errore nella connessione")
            return None

    @staticmethod
    def get_product(product_number) -> Product | None:
        """
        Function that reads all the products in the database and returns them as a set.
        :param product_number: the identification number of the product we want to retrieve.
        :return: a set of products or None if there are connection errors
        """
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT gp.*
                    FROM go_products gp
                    WHERE Product_number =%s"""
            cursor.execute(query, (product_number,))
            row = cursor.fetchone()
            row_product = Product(row["Product_number"],
                                    row["Product_line"],
                                    row["Product_type"],
                                    row["Product"],
                                    row["Product_brand"],
                                    row["Product_color"],
                                    row["Unit_cost"],
                                    row["Unit_price"])
            cursor.close()
            cnx.close()
            return row_product
        else:
            print("Errore nella connessione")
            return None
