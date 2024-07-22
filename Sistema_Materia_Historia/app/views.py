from django.shortcuts import render
# Importing view class from django.views
from django.views import View 

# Importing all models from app/models.py
from .models import*

class IndexView(View):
    # Defining get method
    def get(self, request):
        
        return render (request, 'index.html')
      # Defining post method
    def post(self, request):
        pass

# Index View
class DisciplinaView(View):
    # Defining get method
    def get(self, request):
        disciplina = Disciplina.objects.all()
        return render (request, 'disciplina.html', {'disciplina': disciplina})
      # Defining post method
    def post(self, request):
        pass

# Index View
class CursoView(View):
    # Defining get method
    def get(self, request):
        curso = Curso.objects.all()
        return render (request, 'curso.html', {'curso': curso})
      # Defining post method
    def post(self, request):
        pass

# Index View
class AlunoView(View):
    # Defining get method
    def get(self, request):
        aluno = Aluno.objects.all()
        return render (request, 'aluno.html', {'aluno': aluno})
      # Defining post method
    def post(self, request):
        pass

# Index View
class TopicoView(View):
    # Defining get method
    def get(self, request):
        topico = Topico.objects.all()
        return render (request, 'topico.html', {'topico': topico})
      # Defining post method
    def post(self, request):
        pass

# Index View
class ProfessorView(View):
    # Defining get method
    def get(self, request):
        professor = Professor.objects.all()
        return render (request, 'professor.html', {'professor': professor})
      # Defining post method
    def post(self, request):
        pass

# Index View
class Periodo_HistoricoView(View):
    # Defining get method
    def get(self, request):
        periodo_historico = Periodo_Historico.objects.all()
        return render (request, 'periodo_historico.html', {'periodo_historico': periodo_historico})
      # Defining post method
    def post(self, request):
        pass


# Create your views here.