from selenium import webdriver
import time

class Desafio:
    def __init__(self):
        self.navegador = webdriver.Chrome(
            executable_path=r"./Dependences/chromedriver.exe")

    def encontrarNotebooks(self):
        self.navegador.get(
            'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
        self.navegador.maximize_window()
        time.sleep(1)
        lista = self.navegador.find_elements_by_class_name('caption')
        notebooks = []
        for item in lista:
            dados = {
                "preco": "",
                "descricao": ""
            }
            dados['preco'] = float(item.text.split('\n')[0][1:])
            dados['descricao'] = item.text.split('\n')[2]
            notebooks.append(dados)
        notebooks.sort(key=lambda i: i['preco'])
        dadosNoteboks={
            "Dados":notebooks
        }
        return dadosNoteboks

if __name__ == "__main__":
    desafio = Desafio()
    desafio.encontrarNotebooks()
