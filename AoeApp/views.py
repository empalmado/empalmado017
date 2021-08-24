from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Sign_up_form, Free_Quotation_form, CreateUserForm, StatusForm
from .models import Sign_up, Free_Quotation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users



def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'Project/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username or Password is Incorrect')

		context = {}
		return render(request, 'Project/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


# @login_required(login_url='login')
def Home(request):
    picture = Free_Quotation.objects.all()
    return render(request, 'Project/Home.html', {'picture': picture})

@login_required(login_url='login')
def About_us(request):
    return render(request, 'Project/AboutUs.html')


@login_required(login_url='login')
def Contact_us(request):
    return render(request, 'Project/ContactUs.html')


def Warning(request):
    return render(request, 'Project/warningpage.html')


# def Signup(request):
#     form = Sign_up_form()
#     if request.method == 'POST':
#         form = Sign_up_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login')
#     context = {'form' :form}
#     return render(request, 'Project/Signup.html', context)

# @login_required(login_url='login')
# def Table(request):
#     table = Sign_up.objects.all()
#     return render(request, 'Project/table.html', {'table': table})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def Table1(request):
    table = Free_Quotation.objects.all()
    done = table.filter(status='Done').count()
    pending = table.filter(status='Pending').count()
    form = StatusForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/table')
    context = {'form':form,'table': table, 'done': done, 'pending': pending}
    return render(request, 'Project/table1.html', context)

@allowed_users(allowed_roles=['Users'])
@login_required(login_url='login')
def Free_Quote(request):
    form = Free_Quotation_form()
    if request.method == 'POST':
        form = Free_Quotation_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' :form}
    return render(request, 'Project/FreeQuotation.html', context)


@login_required(login_url='login')
# def update(request, pk):
#     # person = Sign_up.objects.get(id=pk)
#     # form = Sign_up_form(instance=person)
#     # if request.method == 'POST':
#     #     form = Sign_up_form(request.POST, instance=person)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('/table')
#     # context = {'formn' :form}
#     # return render(request, 'Project/FreeQuotation.html', context)

def update(request, pk):
    user = Free_Quotation.objects.get(id=pk)
    form =  StatusForm(instance=user)

    if request.method == 'POST':
        form = StatusForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/table1')

    context = {'form':form}
    return render(request, 'Project/FreeQuotation.html', context)





