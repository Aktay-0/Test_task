from django.shortcuts import render
from django.shortcuts import redirect
from .models import Storage

# Create your views here.

def user_profile(request):
    storages = Storage.objects.all()
    storage = storages[0]
    message = ""

    if request.method == "POST":
        summ = float(request.POST['summ'])
        op = int(request.POST['op'])
        if op == 0 and summ != 0:
            storage.addBalance(summ)
            return redirect('user_profile')
        elif op == 1 and summ != 0:
            if storage.subBalance(summ) == False:
                message = "Операция не может быть выполнена! Недостаточно средств."
            else:
                return redirect('user_profile')

    return render(request, 'task/user_profile.html', {'storage' : storage, 'message' : message})
