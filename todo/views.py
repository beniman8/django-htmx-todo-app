from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


from .models import Name


def todo(request):
    todos = Name.objects.all()

    return render(request,'todo/index.html',{'todos':todos})

@require_http_methods(['POST','GET'])
def edit_todo(request,pk):
    todo = Name.objects.get(pk=pk)

    if request.method == 'POST':
        todo.title = request.POST.get('title','')
        todo.save()
        return render(request,'todo/partial.html',{'todo':todo})

    return render(request,'todo/edit.html',{'todo':todo})


@require_http_methods(['POST'])
def add_todo(request):
    todo = None
    title = request.POST.get('title','')


    if title:
        todo = Name.objects.create(title=title)


    return render(request,'todo/partial.html',{'todo':todo})


@require_http_methods(['PUT'])
def update_todo(request,pk):
    todo = Name.objects.get(pk=pk)
    todo.is_done = True
    todo.save()

    return render(request,'todo/partial.html',{'todo':todo})



@require_http_methods(['DELETE'])
def delete_todo(request,pk):
    todo = Name.objects.get(pk=pk)
    todo.delete()

    return HttpResponse()