from django.shortcuts import render
from.models import Aluno
from django.http import HttpResponse

def alunoView(request):

    aluno_list = Aluno.objects.all()
    aluno_str = '\n'.join([str(aluno) for aluno in aluno_list])
    return HttpResponse(aluno_str)


# Create your views here.
