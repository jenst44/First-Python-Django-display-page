from django.shortcuts import render
from apps.interests.models import Interests, Users
def index(request):
	context = {
		'interests': Interests.objects.all(),
		'users': Users.objects.all()
	}
	return render(request, 'index.html', context)
def home(request):
	return render(request, 'home.html')
def show(request, user_id):
	context = {
		'user': Users.objects.get(id=user_id),
	}
	return render(request, 'user.html', context)