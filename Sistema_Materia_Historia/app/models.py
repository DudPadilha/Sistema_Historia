from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    detalhamento = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return f'{self.nome}'

class Topico(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Topicos"

    def __str__(self):
        return f'{self.nome}'

class Turma(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Turmas"

    def __str__(self):
        return f'{self.nome}'
    
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Cursos"

    def __str__(self):
        return f'{self.nome}'
    
class Disciplinas_Curso(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cursos"

    def __str__(self):
        return f'{self.nome} {self.disciplina} {self.turma}'
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Professores"

    def __str__(self):
        return f'{self.nome} {self.email} {self.topico}'

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    datanasc = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Alunos"

    def __str__(self):
        return f'{self.nome} {self.matricula} {self.datanasc} {self.curso}'

class Periodo_Historico(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    detalhamento = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "Periodos Historicos"

    def __str__(self):
        return f'{self.topico}  {self.detalhamento}'
