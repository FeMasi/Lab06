
from database.sales_dao import SalesDao
from database.products_dao import ProductDao
from database.retailers_dao import RetailersDAO
from model.sale import Sale
class Model:
    def __init__(self):
        self.sales_list = SalesDao.get_sales()


    def get_years(self):
        return SalesDao.get_years()

    def get_brands(self):
        return ProductDao.get_brands()

    def get_retailers(self):
        return RetailersDAO.get_retailers()

    def get_filtered_sales(self, anno, brand, retailer):
        filtered_sales = []
        for sale in self.sales_list:
            if ((anno is None or sale.get_year() == int(anno)) and
                    (brand is None or sale.get_brand() == brand) and
                    (retailer is None or sale.get_retailer() == retailer)):
                filtered_sales.append(sale)
        return filtered_sales

    def get_top_vendite(self, anno, brand, retailer) -> list[Sale]:
        filtered_sales = self.get_filtered_sales(anno, brand, retailer)
        filtered_sales.sort(reverse = True)
        return filtered_sales[0:5]

    def get_statistiche_vendite(self, anno, brand, retailer):
        filtered_sales = self.get_filtered_sales(anno, brand, retailer)
        giro_affari=sum([sale.ricavo for sale in filtered_sales])
        num_retailer=set([sale.retailer_code for sale in filtered_sales])
        num_prodotti = set([sale.product_number for sale in filtered_sales])
        return giro_affari, len(num_retailer), len(num_prodotti), len(filtered_sales)
