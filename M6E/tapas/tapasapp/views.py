from django.shortcuts import render, redirect, get_object_or_404
from .models import Dish, Account 

# Create your views here.

def better_menu(request, pk=None):
    if pk is None:
        return redirect('tapasapp/login.html')

    user = Account.objects.filter(pk=pk).first()
    if not user:
        return redirect('tapasapp/login.html')

    all_dishes = Dish.objects.all()
    
    return render(request, 'tapasapp/better_list.html', {'dishes': all_dishes,'user': user})

def add_menu(request, pk):
    user = get_object_or_404(Account, pk=pk)
    if(request.method=="POST"):
        dishname = request.POST.get('dname')
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.create(name=dishname, cook_time=cooktime, prep_time=preptime)
        return redirect('better_menu', pk=user.pk)
    else:
        return render(request, 'tapasapp/add_menu.html', {'user': user})

def view_detail(request, upk, dpk):
    user = get_object_or_404(Account, pk=upk)
    d = get_object_or_404(Dish, pk=dpk)
    return render(request, 'tapasapp/view_detail.html', {'user': user, 'd': d})

def delete_dish(request, upk, dpk):
    user = get_object_or_404(Account, pk=upk)
    Dish.objects.filter(pk=dpk).delete()
    return redirect('better_menu', pk=user.pk)

def update_dish(request, upk, dpk):
    user = get_object_or_404(Account, pk=upk)
    d = get_object_or_404(Dish, pk=dpk)

    if(request.method=="POST"):
        cooktime = request.POST.get('ctime')
        preptime = request.POST.get('ptime')
        Dish.objects.filter(pk=dpk).update(cook_time=cooktime, prep_time=preptime)
        return redirect('view_detail', upk=user.pk, dpk=d.pk)
    else:
        return render(request, 'tapasapp/update_menu.html', {'user': user, 'd':d})
    
def login_view(request):
    msg = request.GET.get('msg')

    if(request.method=='POST'):
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        user = Account.objects.filter(username=uname, password=pword).first()

        if user:
            return redirect('basic_list', pk=user.pk)
        else:
            return render(request, 'tapasapp/login.html', {'error': 'Invalid login'})
        
    return render(request, 'tapasapp/login.html', {'msg': msg})

def signup(request):
    if(request.method=='POST'):
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        if Account.objects.filter(username=uname).exists():
            return render(request, 'tapasapp/signup.html', {'error': 'Account already exists'})
        else:
            Account.objects.create(username=uname, password=pword)
            return redirect('/?msg=Account created successfully')
        
    return render(request, 'tapasapp/signup.html')

def basic_list(request, pk):
    user = get_object_or_404(Account, pk=pk)
    return render(request, 'tapasapp/basic_list.html', {'user': user})

def manage_account(request, pk):
    account_details = get_object_or_404(Account, pk=pk)
    return render(request, 'tapasapp/manage_account.html', {'user': account_details})

def change_password(request, pk):
    user = get_object_or_404(Account, pk=pk)
    
    if request.method == 'POST':
        current_pword = request.POST.get('current_pword')
        new_pword = request.POST.get('new_pword')
        confirm_pword = request.POST.get('confirm_pword')

        if current_pword != user.password:
            return render(request, 'tapasapp/change_password.html', {
                'user': user,
                'error': 'Current password is incorrect'
            })

        elif new_pword != confirm_pword:
            return render(request, 'tapasapp/change_password.html', {
                'user': user,
                'error': 'New passwords do not match'
            })

        elif new_pword == current_pword:
            return render(request, 'tapasapp/change_password.html', {
                'user': user,
                'error': 'New password cannot be the same as current password'
            })

        user.password = new_pword
        user.save()
        return redirect('manage_account', pk=user.pk)
    return render(request, 'tapasapp/change_password.html', {'user': user})

def delete_account(request, pk):
    user = get_object_or_404(Account, pk=pk)
    user.delete()
    return redirect('logout')

def logout(request):
    request.session.flush()
    return redirect('login')