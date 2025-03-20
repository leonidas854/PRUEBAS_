from django.shortcuts import render
from django.http import JsonResponse
from reynas.solution import solution


def resolver_nqueens(request,n):
    sol = solution()
    ans = sol.solve_queens(n)
    
    
    return JsonResponse({'sol:':len(ans),'respuestas':ans})





# Create your views here.
