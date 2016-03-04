# Making a To Do API!

##### Description

* Now we're going to make an API for a Todo list using Django
* Like many web APIs, we will not be rendering HTML. 
* We will be creating a web based interface that allows users to interact and perform CRUD operations with our DB
* This interaction will be done using HTTP requests (GET or POST) and our clients will be expecting to send or receive JSON.
* In an API routes/urls are known as `endpoints`
* These `endpoints` are the entry points to the database resources
* We will be following `RESTful` practices when building this API

##### Objective 1

* You will have two Models: `Users` and `Todos`
* The Users model will have two fields: 
	* `name`
	* `token`
* The Todos model will have five fields: 
	* `content`
	* `user_id`
	* `created_date`
	* `updated_date`
	* `finished`
	
***Hints***

* What library do we have to control date and time? These may also be specific model fields.
* Don't forget about the `boolean` data type

##### Objective 2

* A User will have many Todos.
* Each user model will be assigned a random key on creation that must be passed with every request. 
	* This will require the use of a `UUID`
	* Take a look at the bottom of the Resources section in today's lesson plan for more information

##### Objective 3

* RESTful, RESTful, RESTful
* We are making a RESTful API. 
* Our GET and POST routes should be organized
* Remember they can target the same endpoint, but what we return from each will and should be competely different.

***GET ROUTES***

- Create an endpoint that returns all of that User's todos, whether they are finished or not.
- Create an endpoint that only returns that User's incomplete todos.
- Create an endpoint that only returns that User's todos for a given date.

You should be able to use and test these in your browser. All errors due to user submission (bad key, incorrect endpoint) should return a 404 status code to the client.

***POST ROUTES***

* To make a proper POST request, you are going to `curl` from your terminal and send in the data to the server.  You will need to pass in the user token as below:

```     
curl -X POST "http://127.0.0.1:8000/todos/" -d "token=81a8d4a4cf0b9c65&todo=buy beer"
```
* Create an endpoint that saves a new todo to the database for the given user's token.
* Create an endpoint that marks a given todo complete for the given user.
* Create an endpoint that updates a given todo for the given user.
* Create an endpoint that deletes a given todo for the given user.
