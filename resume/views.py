from django.shortcuts import render

from django.conf import settings

from django.core.files.storage import FileSystemStorage

import zipfile

# Create your views here.


### globe variables starts

pather = ""

### globe variables ends


def viewer(request):
    
    without = False
    
    if request.method == 'POST':
        
        lister = [ { "name": "candidate1", "link": "http://google.com" }, { "name": "candidate2", "link": "http://medium.com" } ]
    
        imp = request.POST['parters']
    
        if imp == "1" :
    
            myfile = request.FILES['myfile']

            fs = FileSystemStorage()

            filename = fs.save("resume/files/"+myfile.name.replace(" ","_"), myfile)

            upload_file_url = fs.url(filename)

            zip_ref = zipfile.ZipFile(filename, 'r')

            path1 = "resume/output/"+filename.split("/")[2]

            zip_ref.extractall(path1)

            path2 = path1+"/"+ myfile.name.split(".")[0]

            print "path for the algorithm : " + path2

            pather = path2

            
            ### function call should happen here : Functions analysing all the files in the folder
            
            # => use the variable pather as the folder path 

            
            
            

            ### Code space ends

            
            zip_ref.close()
            
            without = "part2"

            return render(request, 'resume/startpage.html', { 'parter': without })    
        
        else:
            
            parter = 3
            
            texter = request.POST['texter']
            
            
            ### function call should happen here : After he presses the search candidates 
            
            # => texter is the job description input variable
            
			# => Pather is the folder path
			
            # => use the variable lister and store the result as list of dict
            
            
            
            
            ### code space ends
            
            
            return render(request, 'resume/startpage.html', { 'parter': without, 'many': lister })    
        
        
    print "Initial Window"
        
    without = "part1"
    
    return render(request, 'resume/startpage.html', { 'parter': without })

