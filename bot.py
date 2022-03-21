import os
import json
import requests
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SocialNetwork.settings")
# django.setup()
# from django.conf import settings


BASE_URL="http://localhost:8000"

## User Sign up

first_name = input('Enter first_name: ')
last_name = input('Enter last_name: ') 
email = input('Enter email: ')
password = input('Enter password: ')
if not first_name and not last_name and not email and not password:
	print('please fill first first_name')
url = f"{BASE_URL}/api/sign-up"
data = {"first_name":first_name,"last_name":last_name,"email":email,"username":email,"password":password}
response = requests.post(url,data = data)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
    	print(key,jData[key])
else:
    response.raise_for_status()


## For Login User

email = input("Enter your email: ")
password = input('Enter your password: ')
if not email and not password:
	print("Please enter all fields")
url = f"{BASE_URL}/api/token/"
data = {"username":email,"password":password}
response = requests.post(url,data =data)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
    	print(key)
    access_token= jData[key]
    print(access_token)
else:
	print('Enterd data did not match to any User')
	response.raise_for_status()


## For Post creation

title = input("Enter Post Title: ")
description = input("Enter description: ")
url = f"{BASE_URL}/api/post"
data = {"title":title,"description":description}
headers = {"Authorization":f"Bearer {access_token}"}
response = requests.post(url,data = data,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
    	print(key,jData[key])
else:
	print('Enterd data did not match to any User')
	response.raise_for_status()



## For Like/Dislike Post

post = input("Enter post id to like/dislike post: ")
if not post:
	print('post id is required')
url = f"{BASE_URL}/api/like-dislike"
headers = {'Authorization':f'Bearer {access_token}'}
data = {
    "post":post
}
response = requests.post(url,data = data,headers = headers)
if(response.ok):
	jData = json.loads(response.content)
	print("The response contains {0} properties".format(len(jData)))
	print("\n")
	for key in jData:
		print(key,jData[key])
else:
	response.raise_for_status()


## For Viewing all posts]

url = f"{BASE_URL}/api/post"
headers = {'Authorization':f'Bearer {access_token}'}
response = requests.get(url,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
    	print(key,jData[key])
else:
	response.raise_for_status()



## For viewing single user post

params = int(input("enter post ID to view that post: "))
if not params:
	print("Post id required")
url = f"{BASE_URL}/api/post/{params}"
headers = {'Authorization':f'Bearer {access_token}'}
response = requests.get(url,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
    	print(key,jData[key])
else:
	response.raise_for_status()


## For Delete post

params = int(input('Enter post ID to delete that post: '))
url = f"{BASE_URL}/api/post/{str(params)}"
headers = {'Authorization':f'Bearer {access_token}'}
response = requests.delete(url,headers = headers)
if(response.ok):
    jData = json.loads(response.content)
    print("The response contains {0} properties".format(len(jData)))
    print("\n")
    for key in jData:
    	print(key,jData[key])
else:
	response.raise_for_status()

