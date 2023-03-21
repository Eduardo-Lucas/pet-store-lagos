import uuid
from django.db import models
from django.db.models import Count

from core.choices import Sexo, UnidadeFederativa

class Tutor(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    nome = models.CharField(max_length=100)
    celuar = models.CharField(max_length=14, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    rg = models.CharField(max_length=14, null=True, blank=True)
    rua = models.CharField(max_length=14, null=True, blank=True)
    numero = models.CharField(max_length=14, null=True, blank=True)
    complemento = models.CharField(max_length=14, null=True, blank=True)
    bairro = models.CharField(max_length=14, null=True, blank=True)
    cidade = models.CharField(max_length=14, null=True, blank=True)
    uf = models.CharField(max_length=14, null=True, blank=True, choices=UnidadeFederativa.choices, 
                          default='RJ')
    email = models.EmailField(max_length=40, null=True, blank=True)
    observacao = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'tutor'
    
    @property
    def quantidade_de_pets(self) -> int:
        qtd = Pet.objects.filter(tutor=self.id).count()
        return qtd

    def __str__(self) -> str:
        if self.quantidade_de_pets == 0:
            return f'{self.nome} não possui nenhum pet cadastrado!'
        if self.quantidade_de_pets > 1:
            return f'{self.nome} possui {self.quantidade_de_pets} pets cadastrados!'
        else:
            return f'{self.nome} possui apenas {self.quantidade_de_pets} pet cadastrado'


class Raca(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    nome = models.CharField(max_length=100)

    class Meta:
        db_table = 'raca'

    def __str__(self) -> str:
        return self.nome
    

class Especie(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        db_table = 'especie'

class Pet(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    tutor = models.ForeignKey(Tutor, db_index=True, on_delete=models.PROTECT, 
                              related_name='meu_dono')
    nome = models.CharField(max_length=100)
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT)
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT) 
    sexo = models.CharField(max_length=10, choices=Sexo.choices)
    idade = models.IntegerField(default=0)
    observacao = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.nome} - Tutor: {self.tutor.nome}'
    
    class Meta:
        db_table = 'pet'