from django.db import models

# Create your models here.

class Hospede(models.Model): 
    nome_do_hospede = models.CharField(max_length=50, help_text='Insira o nome do hóspede') 

    SEXO = (
        ('M',	'Masculino'),
        ('F',	'Feminino'),
    )

    sexo = models.CharField(
        max_length=1,
        choices=SEXO,
    )
    data_de_admissao = models.DateField(null=True, blank=True)
    n_de_matricula = models.CharField(max_length=12)
    data_desligamento_obito = models.DateField(null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)
 
    class Meta: 
        ordering = ['nome_do_hospede'] 

    def __str__(self): 
        return self.nome_do_hospede 
    
class Familiar(models.Model):
    hospede = models.ForeignKey('Hospede', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, help_text='Insira o nome do hóspede')
    data_de_nascimento = models.DateField(null=True, blank=True)
    parentesco_vinculo = models.CharField(max_length=20)
 
    class Meta: 

        ordering = ['hospede', 'nome'] 

    def __str__(self): 

        return f'{self.hospede} -> {self.nome}' 
