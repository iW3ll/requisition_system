from django.db import models
from django.utils.timezone import now
from datetime import datetime
from django.utils import timezone



class Estudante(models.Model):
    ESCOLHA_CURSO = [
        ('Computação', 'Computação'),
        ('Elétrica', 'Elétrica'),
        ('Superior - Computação', 'Superior - Computação'),
        ('Superior - Matemática', 'Superior - Matemática'),
    ]

    CAMISA = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]

    id_estudante = models.AutoField(primary_key=True)
    nome_estudante = models.CharField(max_length=45)
    matricula = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    bolsista_pae = models.BooleanField()
    curso = models.CharField(max_length=50, choices=ESCOLHA_CURSO)

    # Itens
    deseja_caderno = models.BooleanField(default=False)
    deseja_garrafa = models.BooleanField(default=False)
    camisa = models.CharField(max_length=50, null=True, blank=True, choices=CAMISA)  # Checkbox para escolher camisa

    # Campos de data
    created = models.DateTimeField(editable=False, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """ Override o método save para gerenciar as datas de criação e modificação. """
        if not self.pk:  # Verifica se o objeto ainda não tem um 'pk' (que é o id, o campo chave primária)
            self.created = timezone.now()  # Define o timestamp de criação
        self.modified = timezone.now()  # Atualiza o timestamp de modificação
        return super(Estudante, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome_estudante
    
class Requisicao(models.Model):
    id_requisicao = models.AutoField(primary_key=True)
    data_requisicao = models.DateTimeField(auto_now_add=True)
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)

    def __str__(self):
        return f"Requisição {self.id_requisicao}"

class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    nome_material = models.CharField(max_length=45)
    estoque_disponivel = models.IntegerField()

    def __str__(self):
        return self.nome_material

class ItemRequisicao(models.Model):
    id_item_requisicao = models.AutoField(primary_key=True)
    requisicao = models.ForeignKey(Requisicao, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade_requisitada = models.IntegerField()
    status = models.CharField(max_length=11)
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Item {self.id_item_requisicao} da Requisição {self.requisicao.id_requisicao}"