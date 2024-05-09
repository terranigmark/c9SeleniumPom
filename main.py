from test_suite.e2e_tests.purchasing_items import TestMadison


def pruebas_madison():
    pruebas_madison_island = TestMadison()
    pruebas_madison_island.setup_class()
    pruebas_madison_island.test_comprando_una_camisa_oxford()
    pruebas_madison_island.teardown_class()


def pruebas_api():
    pass


if __name__ == '__main__':
    pruebas_madison()
    pruebas_api()