from django.http import JsonResponse

def suma(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        resultado = a + b
        return JsonResponse({'resultado': resultado})
    except ValueError:
        return JsonResponse({'error': 'Valores no válidos'}, status=400)

def resta(request):
    try:
        a = float(request.GET.get('a', 0))
        b = float(request.GET.get('b', 0))
        resultado = a - b
        return JsonResponse({'resultado': resultado})
    except ValueError:
        return JsonResponse({'error': 'Valores no válidos'}, status=400)

def multiplicacion(request):
    try:
        a = float(request.GET.get('a', 1))
        b = float(request.GET.get('b', 1))
        resultado = a * b
        return JsonResponse({'resultado': resultado})
    except ValueError:
        return JsonResponse({'error': 'Valores no válidos'}, status=400)

def division(request):
    try:
        a = float(request.GET.get('a', 1))
        b = float(request.GET.get('b', 1))
        if b == 0:
            return JsonResponse({'error': 'No se puede dividir por cero'}, status=400)
        resultado = a / b
        return JsonResponse({'resultado': resultado})
    except ValueError:
        return JsonResponse({'error': 'Valores no válidos'}, status=400)
