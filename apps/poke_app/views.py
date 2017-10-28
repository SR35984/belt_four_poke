from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User, Poke

def flash_errors(errors, request):
    for error in errors:
       messages.error(request, error)

def current_user(request):
    return User.objects.get(id=request.session['user_id'])

def user(request, id):
	context={
		'user': current_user(request),
	}
	return render(request, 'poke_app/index.html')

def index(request):
    return render(request, 'poke_app/index.html')

def register(request):
    if request.method =="POST":
        errors = User.objects.validate_registration(request.POST)

        if not errors:
            user = User.objects.create_user(request.POST)
            request.session['user_id'] = user.id
            return redirect(reverse('dashboard'))

        flash_errors(errors, request)
    return redirect(reverse('landing'))

def login(request):
    if request.method == "POST":
        check = User.objects.validate_login(request.POST)
        print check

        if 'user' in check:
            request.session['user_id'] = check['user'].id

            return redirect(reverse('dashboard'))

        flash_errors(check['errors'], request)
    return redirect(reverse('landing'))


def logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id')
    return redirect(reverse('landing'))


def dashboard(request):
	if 'user_id' not in request.session:
		return redirect('/')

	user = current_user(request)
	users = User.objects.exclude(id=request.session['user_id'])
	pokes = Poke.objects.all().distinct('poked_id')
	poke_count = Poke.objects.filter(poked_by=request.session['user_id']).count()
	list_of_users = Poke.objects.filter(poked_by=request.session['user_id']).exclude(id=request.session['user_id']).distinct('poker')

	context = {
		'user': user, 
		'users': users, 
		'pokes': pokes, 
		'poke_count': poke_count,
		'list_of_users': list_of_users 
	}
	return render(request, 'poke_app/dashboard.html', context)

def poke(request, user_id):
	poker = User.objects.get(id=request.session['user_id'])
	poked_by = User.objects.get(id=user_id)
	poke = Poke()
	poke.counter+=1
	return redirect('/pokes')