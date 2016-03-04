# Building An API

### Learning Objectives
***Students will be able to...***

* Build an API using Django

---
### Context

* Continuing to become Full Stack Developers

---
### Lesson

##### Part 1 - What is an API?

* API - stands for application program interface
* Technically everything is an API
* However 99% of the time when API's are being discussed people are most likely talking about Web APIs
* These will take in a request and serve data to you in JSON format
* You may remember the homeworks involving the `OMDB API` or the `MarkIt API`
* We made a `request` and got data back in the form of `JSON`
* APIs should be built with a RESTful design

##### Part 2 - What is REST?

* What the hell is a RESTful API?

***Five Min Exercise***

* As a group, write on the board what CRUD is, and the four main HTTP verbs
	* Bonus if you can name all 8 HTTP verbs
* Research RESTful API structure. We will come back to discuss

***REST***

* REST stands for Representational State Transfer
* Building an RESTful API involves organizing your endpoints in an organized format with their respective HTTP Verbs
* What is the difference between 

```
GET localhost:8000/
GET localhost:8000/create
POST localhost:8000/create
GET localhost:8000/update/1
POST localhost:8000/update/1
```
* A RESTful framework will map to the FOUR MAIN CRUD operations in HTTP:
	* `GET`, `POST`, `PUT`, `DELETE`
* Notice we can have the same endpoint for two different operations. This is because they will be responding with different things 

##### Part 3 - JSON vs. XML

* We've discussed this earlier in the course but a brief overview
* Both JSON and XML are file formats.
	* XML is an older file format and is used with many older languages
	* You may find it used many times in large organizations such as Universities, or Banks. This is because their entire system is running on older technologies
	* JSON is the ideal file format for dealing with API's or even making APIs
	* JSON looks like a dictionary and we can navigate it as such
* Speaking of JSON, this is what we will be doing in our API assignments

##### Part 4 - Django JSON syntax

* If you don't have it already google `JSON Viewer` and install the JSON Viewer from the chrome web store.
	* This will format your JSON to human readable
* Django has a built in JSON Response library

```
from django.http import JsonResponse

def get_todos(request, user_key):
	
	return JsonResponse({"key":"value"})
```
* What is that? There's some error? 
* We have to exempt our CSRF (Cross Site Resource Forgery)
* The CSRF protection is not needed because we want to allow users to perform all CRUD operations to the database. 
* Check out the below example to exempt our CSRF

```
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
	pass
```
* You will also have to include an exempt to your urls file if you are using class based views

```
from django.views.decorators.csrf import csrf_exempt

url(r'^stocks$', csrf_exempt(MyView.as_view()))
```
* The JSON data will not be in the `request.POST` dictionary.
* Instead it will be in the `request.body`

##### Resources

* Here are resources regarding REST, CSRF tokens, and curl. (A bash command that you will be using for the homework)
* [Tutorial Point for HTTP Request](http://www.tutorialspoint.com/http/http_requests.htm)
* [Andrew Havens Beginners Guide to Creating a REST API](http://www.andrewhavens.com/posts/20/beginners-guide-to-creating-a-rest-api/)
* [Miguel Grinberg Design a RESTful API with Python and Flask](http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [What exactly is RESTful programming?](http://stackoverflow.com/questions/671118/what-exactly-is-restful-programming)
- [Representational State Transfer Wiki](https://en.wikipedia.org/wiki/Representational_state_transfer)
- [CSRF Exemption for APIs](http://stackoverflow.com/questions/10741339/do-csrf-attack-worries-apply-to-apis)
- [curl](http://superuser.com/questions/149329/what-is-the-curl-command-line-syntax-to-do-a-post-request)
- [*Universally unique identifier*](https://en.wikipedia.org/wiki/Universally_unique_identifier)
- [UUID module](https://docs.python.org/3/library/uuid.html#uuid.UUID)
* We use UUID's to give our users unique identifiers 
* Below is an example of how to make that key:

```
from uuid import uuid4
key = uuid4().hex
```
* Now when a user makes a request the complete URL should look like the below example

```
GET http://mytodolist.com/todos/<user_token>/
```
