import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Profile, Todos
from django.views.generic import View
from django.shortcuts import get_object_or_404
import pudb

# Create your views here.

class Register(View):
	def post(self, request):
		try:
			data = json.loads(request.body.decode('utf-8'))
			username = data['username']
			password = data['password']
			user = User.objects.create_user(username=username, password=password)
			profile = Profile.objects.create(name=user)
			# not sure if I need this line
			user.save()
			return JsonResponse({'user':profile.token.hex})
		except:
			return JsonResponse({'something went wrong with your register. try again.': True})

class LoginView(View):
	def post(self,request):
		data = json.loads(request.body.decode('utf-8'))
		username = data['username']
		password = data['password']
		user = authenticate(username=username, password=password)
		if user:
			return JsonResponse({'token': user.profile.token.hex})
		else:
			return JsonResponse({'response': 'Does not exist'})

class CreateTodo(View):
	def post(self,request, token):
		try:
			data = json.loads(request.body.decode('utf-8'))
			content = data['content']
			profile = get_object_or_404(Profile, token=token)
			todo = Todos.objects.create(user_id=profile,content=content)
			todo.save()
			return JsonResponse({"message": "Created"})
		except:
			return JsonResponse({'response': 'failed'})

class ViewAll(View):
	def get(self, request, token):
		try:
			profile = get_object_or_404(Profile, token=token)
			todo_object = profile.todos_set.all()
			todo = [todo.to_json() for todo in todo_object ]
			return JsonResponse(json.dumps(todo), safe=False)
		except:
			return JsonResponse({'response': 'failed'})

class ViewUnfinished(View):
	def get(self, request, token):
		try:
			profile = get_object_or_404(Profile, token=token)
			unfinished_todos = profile.todos_set.filter(finished = False)
			response = [todo.to_json() for todo in unfinished_todos ]
			if not response:
				response = {"message": "No unfinished todos"}
			return JsonResponse(json.dumps(response), safe=False)
		except:
			return JsonResponse({'response': 'failed'})

