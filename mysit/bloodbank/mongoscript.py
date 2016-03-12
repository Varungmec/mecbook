from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.my

# import gridfs
# fs = gridfs.GridFS(db)
# a=fs.put("Sdfsdf")
# b = fs.put(fs.get(a), filename ="one")
# out=fs.get(b)
# print out.filename

# print fs.get(a).read()

def add_book(categoryname,bookname,choicelist,authorname):
    
    
    p=db.get_collection(categoryname)
    p.insert({"bookname" :bookname,"choices" :choicelist,"authorname":authorname})

    
    # db.np.insert({"hello" : "kname"})
    # print "inside func"
    # print type(np)
# def get_country(db,na):
    # return db.na.find_one()


# add_country(db,"network")

def check_book(missing_book):
	#funciton to search if searched book present in database
	categories=db.collection_names()
	for category in categories:
		p=db.get_collection(category)
		l=p.find({"bookname":missing_book})
		for items in l:
		 	# print "a"
		 	# print items["bookname"]
		 	return items["bookname"]

	return 0	 	

def di_collection():
	l=[]
	c=db.collection_names()
	for document in c:
		l.append(document)
		# print l
	return l	

def add_category(missing_category):
	#Function to check if "query" category is already present in database
	categories=db.collection_names(missing_category)
	if missing_category not in categories:
		db.create_collection(missing_category)
		print "collection not present"
		return 1
	else:
		print "Already collection present"
		return 0


def displaybook(query,flag):
	f=0
	c=db.collection_names()
	s=[]
	for document in c:
		p=db.get_collection(document)
		# cursor = db.restaurants.find({"borough": "Manhattan"})
		if flag == 1:
			l=p.find({"bookname":query})
			
			for items in l:
			 	# print "a"
			 	s.append(items)
				f=1		
			# print s
		else:
			print "insi"
			l=p.find({"authorname":query})
			
			for items in l:
				s.append(items)
				print s
				f=1

	if f == 0:
		s=[]
		return s
		print "not found"
	else:
		return s

		

