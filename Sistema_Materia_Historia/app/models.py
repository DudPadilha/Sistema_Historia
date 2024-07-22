from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, null=True)
    detalhamento = models.TextField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return f'{self.nome}'
    
class Curso(models.Model):
    nome = models.CharField(max_length=100, null=True)
    turma = models.CharField(max_length=100, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "Cursos"

    def __str__(self):
        return f'{self.nome} {self.turma} {self.disciplina}'
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100, null=True)
    matricula = models.CharField(max_length=20, unique=True, null=True)
    datanasc = models.DateField(null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Alunos"

    def __str__(self):
        return f'{self.nome} {self.matricula} {self.datanasc} {self.curso}'

class Topico(models.Model):
    nome = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = "Topicos"

    def __str__(self):
        return f'{self.nome}' 

class Professor(models.Model):
    nome = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "Professores"

    def __str__(self):
        return f'{self.nome} {self.email} {self.topico} {self.disciplina}'



    
class Periodo_Historico(models.Model):
    nome = models.CharField(max_length=100, null=True)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, null=True)
    periodo = models.CharField(max_length=100, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
    contexto = models.TextField(max_length=10000, null=True)
    principais = models.TextField(max_length=10000, null=True)
    impactos_e_consequencias = models.TextField(max_length=10000, null=True)
    legado = models.TextField(max_length=10000, null=True)
    

    class Meta:
        verbose_name_plural = "Periodos_Historicos"

    def __str__(self):
        return f'{self.nome} {self.topico} {self.periodo} {self.professor} {self.contexto} {self.principais} {self.impactos_e_consequencias} {self.legado}'
