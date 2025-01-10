from django.db import models  # Importa o módulo de modelos do Django para definir classes representando tabelas no banco de dados.

# Define a classe `Category` que representa a tabela de categorias no banco.
class Category(models.Model):  
    title = models.CharField(max_length=100)  # Um campo de texto com limite de 100 caracteres para o título da categoria.
    slug = models.SlugField(unique=True)  # Um campo para armazenar slugs únicos (usados em URLs amigáveis).
    description = models.TextField(max_length=500, blank=True, null=True)  # Um campo de texto com até 500 caracteres, opcional.
    active = models.BooleanField(default=True)  # Um campo booleano que indica se a categoria está ativa (padrão: True).

    # Método para retornar uma representação em string da categoria (usado no admin e logs).
    def __unicode__(self):  
        return self.title  # Retorna o título da categoria.
