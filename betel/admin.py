from django.contrib import admin
from betel.models import Hospede, Familiar

# Register your models here.

class FamiliarInline(admin.StackedInline):
    model = Familiar

@admin.register(Hospede) 
class HospedeAdmin(admin.ModelAdmin): 
    list_display = ('nome_do_hospede', 'sexo', 'data_de_admissao', 'n_de_matricula', 'data_desligamento_obito', 'nascimento') 
    inlines = [FamiliarInline]

    
@admin.register(Familiar) 
class FamiliarAdmin(admin.ModelAdmin): 
    list_display = ('hospede','nome','data_de_nascimento','parentesco_vinculo') 
