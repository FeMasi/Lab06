import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._brand = None
        self._retailer = None

    def populate_dd_anno(self):
        anni = self._model.get_years()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno[0]))
        self._view.update_page()

    def read_anno(self, e):
        self._anno = e.control.data

    def read_brand(self, e):
        self._brand = e.control.data

    def read_retailer(self, e):
        self._retailer = e.control.data

    def populate_dd_brand(self):
        brands = self._model.get_brands()
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand[0]))
        self._view.update_page()

    def populate_dd_retailer(self):
        retailers = self._model.get_retailers()
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=retailer.retailer_code,
                                                                     text=retailer.retailer_name,
                                                                     data=retailer,
                                                                     on_click=self.read_retailer))
        self._view.update_page()

    def handle_top_vendite(self, e):
        self._view.pr_ring.visible = True
        self._view.btn_top_vendite.disabled = True
        self._view.btn_analizza_vendite.disabled = True
        self._view.update_page()
        top_vendite = self._model.get_top_vendite(self._anno, self._brand, self._retailer)
        self._view.pr_ring.visible = False
        self._view.btn_top_vendite.disabled = False
        self._view.btn_analizza_vendite.disabled = False
        self._view.lst_result.controls.clear()
        if len(top_vendite) == 0:
            self._view.lst_result.controls.append(ft.Text("Nessuna vendita con i filtri selezionati"))
        else:
            for vendita in top_vendite:
                self._view.lst_result.controls.append(ft.Text(vendita))
        self._view.update_page()

    def handle_analizza_vendite(self, e):
        pass
