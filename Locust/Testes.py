from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def consultaLivros(self):
        self.client.get("/", name="Consulta de Livros")
        

    @task
    def about(self):
       livroID = random.randint(1, 200)
       response = self.client.get(f"/{livroID}/", name="Consulta de Livro Randomico")
       if response.status_code == 200:
           print(f"Livro {livroID} encontrado com sucesso.")
       else:
           print(f"Livro {livroID} não encontrado.")
#
   # @task
   # def contact(self):
   #     self.client.get("/contact")