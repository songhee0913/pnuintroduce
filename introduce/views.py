from django.shortcuts import render
from .models import Introduce

def introduce_list(request):
    # DB로부터 Shop목록을 Fetch할 예정
    qs = Introduce.objects.all() # QuerySet 타입
    return render(request, 'introduce/introduce_list.html', {
    'introduce_list': qs,
    })

def introduce_detail(request, pk):
    introduce = Introduce.objects.get(pk=pk)
    return render(request, 'introduce/introduce_detail.html', {
        'introduce': introduce,
    })