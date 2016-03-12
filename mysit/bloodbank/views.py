#welcome to views page -django 

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from bloodbank.forms import *
#from login.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
#from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from bloodbank.models import *
from django.template import Context, Template
import subprocess
from django.http import HttpResponse
from mongoscript import *
from test import *
from django.contrib.auth.decorators import login_required
from googlebooks import *

# 2 variables declared outside all functions : used for global purposes.
global_query_variable=None
author_name=None

# index funxtion servers starting of page 
def index(request): 
	return render(request,'bloodbank/boot.html',)

@login_required
def welcome(request):
	if request.method == 'GET':
		# print "inside get"
		return render(request,'bloodbank/search.html')
	else:
		if "addcat_submit_button" in request.POST:
			form=search_addcat_form(request.POST)
			if form.is_valid():
				p=form.cleaned_data['categoryname']
				if(add_category(p)):
					return HttpResponse("Searched book category you wish to add is beig added ")
				else:
					return HttpResponse("Searched bookcategory you wish to add already present ")

		else: 
			form=search_addbook_form(request.POST)
			if form.is_valid():
				query=form.cleaned_data['bookname']
				
				global p
				global global_query_variable
				global author_name
				
				gb_bookname,gb_authorname=googlebook_search(query)
				 #search query in google books
				
				global_query_variable=gb_bookname[0]
				
				p=check_book(global_query_variable)
				
				# print gb_bookname[0],gb_authorname[0][0]
				# global_query_variable=query
				author_name=gb_authorname[0][0]
				
				if(p):
					global_query_variable=None
					# print "inside dis"
					# print p
					return HttpResponse("Searched book %s already present " % p)
				else:
					# print str(query)
					# s=[]
					# s=di_collection()
					# context={'list':s[1:]}
					# if request.method == 'POST':
					# 	print "hello2"
					subprocess.call(['./mini.sh', str(query)])
					# 	# return HttpResponse("Searched book missing to be added")
					# 	return render(request,'bloodbank/drop.html',context)
					# 	# subprocess.call(['ls'])
					# else:
					# 	print "hello"
					return HttpResponseRedirect('/bloodbank/welcome/find')
			
			return HttpResponse("Welcome to MEc bloodbank site")

#def signup(request):
#template = loader.get_template('bloodbank/index.html')
#return HttpResponse("Welcome , to mec bloodbank ONLINE PORTAL ")
#return render(request,'bloodbank/index.html',)
link=[]
def find(request):
	if request.method == 'GET':
		form=categoryform()
		s=[]
		s=di_collection()
		link=links()
		# print link[2]
		form.fields['choices'].choices = [(x,x) for x in link]
		context={'list':s[1:],'list2':form}
		return render(request,'bloodbank/drop.html',context)
	else:
		
		form=categoryform(request.POST)
		# print request.POST
		l=[]
		l=request.POST.getlist('choices')
		s=request.POST.get('categoryname')
		# print p
		global global_query_variable
		global author_name
		add_book(s,global_query_variable,l,author_name)
		global_query_variable=None
		author_name=None
		# if form.is_valid():
		# print "SDf"
		# print form.cleaned_data['categoryname']
		# print form.cleaned_data['choices']
	
		# print form.get('choices')
		# for item in form.cleaned_data['choices']:
			# print item

		# add_collection(catname)
		
		return HttpResponse("The book has been added")



#@csrf_protect
def signup(request):    
	if request.method == 'GET':
#print 'ddd'
		return render(request,'bloodbank/index.html',)
	else:								# If the form has been submitted...
		form=CForm(request.POST) # A form bound to the POST data
		# print "ddd"
		if form.is_valid():		       
			 #print "ddd"
		
			
			c =Customer()
			
			if form.clean_password2():
				c.password=form.cleaned_data['pass1']
				p= User.objects.create_user(
			username=form.cleaned_data['firstname'],
			first_name=form.cleaned_data['firstname'],
			password=form.cleaned_data['pass1'],
			last_name=form.cleaned_data['lastname'])
				c.age=form.cleaned_data['age']
				c.email=form.cleaned_data['email']
				c.user=p
				c.save()
				from m1 import *
				db = get_db() 
				add_country(db,`form.cleaned_data['firstname']`)
				print get_country(db)
				print "end"
				return HttpResponseRedirect('/bloodbank/welcome')


def login_new(request):
	if request.method == 'GET':
		return render(request,'bloodbank/login.html',)
	else:
		# print request.POST
		if "yoyo" in request.POST:
			form=searchbookform(request.POST)
			if form.is_valid():
				option=form.cleaned_data['yoyi']
				searchquery=form.cleaned_data['queryname']
				gb_bookname,gb_authorname=googlebook_search(searchquery)
				m=[]
				if option == "authorname":
				 	print "SDf"
				 	searchquery=gb_authorname[0][0]
				 	print searchquery
				 	m=displaybook(searchquery,0)
				 	print m	
				else:
				 	
				 	# print "hiihi"
				 	# print searchquery
				 	
				 	searchquery=gb_bookname[0]
				 	# print searchquery
				 	m=displaybook(searchquery,1)
				 	# print m
			 	for items in m:
			 		print items
			 		pp=items['choices']
			 		p1=items['bookname']
			 		p2=items['authorname']
			 		print pp
			 	context={'list':pp,'list2':p1,'list3':p2}
			 	# print "LL"
			 	return render(request,'bloodbank/disp.html',context) 

			# print "hihi"
			return HttpResponse("hooolahhhh vada mone")
		else:
			form=Lform(request.POST)
			if form.is_valid():
				username = form.cleaned_data['firstname']
				password = form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				# print "insrde login"
				if user is not None:
					if user.is_active:z
def users(request):
	p=User.objects.all()
	#print p
	template = Template("My name is {{ my_name }}.")
	context = Context({"my_name": "Adrian"})
	template.render(context)
	print template
	return HttpResponse("List")








# def check(request):
# 	from m1 import *
# 	db = get_db() 
# 	add_country(db,"hihi")
# 	print get_country(db)


# 	return HttpResponse("Welcome to MEc mongo bloodbank site")


	