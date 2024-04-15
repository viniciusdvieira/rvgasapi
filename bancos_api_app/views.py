

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Instituicao
from django.shortcuts import render
@csrf_exempt
def home(request):
    return render(request, 'consulta_bancos.html')
@csrf_exempt
def listar_bancos(request):
    if request.method == 'GET':
        bancos = Instituicao.objects.all()
        data = [{'codigo_compensacao': banco.codigo_compensacao, 'nome': banco.nome} for banco in bancos]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def consultar_banco(request, codigo_compensacao):
    if request.method == 'GET':
        try:
            banco = Instituicao.objects.get(codigo_compensacao=codigo_compensacao)
            data = {'codigo_compensacao': banco.codigo_compensacao, 'nome': banco.nome}
            return JsonResponse(data)
        except Instituicao.DoesNotExist:
            return JsonResponse({'error': 'Banco não encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
