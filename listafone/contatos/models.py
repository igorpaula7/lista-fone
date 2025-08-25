from django.db import models


class Categoria(models.Model):
   nome = models.CharField(max_length=50) # CharField pra strings
   cor = models.CharField(max_length=7) # Código Hexadecimal


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    foto_de_perfil = models.ImageField(upload_to="fotos_perfil/", blank=True, null=True)
    # Imagem Joga em pasta, pode ser nulo ou ficar em branco no formulário
    data_criacao = models.DateField(auto_now_add=True) # Define na criação
    data_atualizacao = models.DateField(auto_now=True) # Define ao atualizar
    favorito = models.BooleanField(default=False) # Falso por padrão
    emergencia = models.BooleanField(default=False) # Falso por padrão 
    categoria = models.ForeignKey(Categoria,  on_delete=models.SET_NULL, null=True)
    # Caso a categoria seja deletada, é setado como sem categoria
