from Filer import Filer

filer  = Filer("http://seaweedfs:8888")
result = filer.upload(path="twitch/person.csv",file=open("./test-data/person.csv"))
print("Upload",result)
file = filer.get(
    path=result.get("FullPath")
)
print("Get",file)

#file = filer.remove(
#    path="twitch/{}".format(result.get("name"))
#)
#print("Delete",file)

#result = filer.list("twitch")
#print("List",result)


#result = filer.upload_append(path="twitch/upload.txt",file=open("./test-data/upload-append.txt"))
#print("Append",result)