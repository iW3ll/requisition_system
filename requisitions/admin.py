from django.contrib import admin
from .models.models import Estudante, Requisicao, Material, ItemRequisicao

admin.site.register(Estudante)
admin.site.register(Requisicao)
admin.site.register(Material)
admin.site.register(ItemRequisicao)