from django.contrib import admin

from .models import *

admin.site.register(Disciplina)
admin.site.register(Topico)
admin.site.register(Turma)
admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Periodo_Historico)


# Register your models here.