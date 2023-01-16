from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('Hello World!')
    # params={'name':'Rakshya'}
    # return render(request, 'index.html',params)
    return render(request,'index.html')

def about(request):
    # return HttpResponse('Hello World!')
    # params={'name':'Rakshya'}
    # return render(request, 'index.html',params)
    return render(request,'about.html')
def error(request):
    # return HttpResponse('Hello World!')
    # params={'name':'Rakshya'}
    # return render(request, 'index.html',params)
    return render(request,'error.html')
def analyze(request):
    #Get the text 
    djtext=request.POST.get('text','default')

    #Check checkbox values 
    removepunc=request.POST.get('removepunc','off') 
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    # charactercounter=request.GET.get('charactercounter','off')
    
   

    #Check which checkbox is on
    
    if removepunc=="on":
    #analyzed=djtext 
     punctuations= ".?!,:;-[]{}()""@#$%^&*''"
     analyzed= ""
     for char in djtext:
        #Removed Punctuations
        if char not in punctuations:
            analyzed = analyzed + char     
     params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
     djtext=analyzed
     #return render(request,'analyze.html',params) 

     #Uppercase
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to Uppercase:','analyzed_text':analyzed}
        djtext=analyzed
       # return render(request,'analyze.html',params) 
   
   #New Line Remover
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n":
                analyzed=analyzed+char
        params={'purpose':'Removed Newline','analyzed_text':analyzed}       
        djtext=analyzed
       
        #return render(request,'analyze.html',params)
    
    #Space Remover
    if(spaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
             analyzed = analyzed + char
        params={'purpose':'Removed ExtraSpace','analyzed_text':analyzed}       
        djtext=analyzed
        #return render(request,'analyze.html',params) 

    #Character Counter
    # if(charactercounter=="on"):
    #     analyzed= ""
    #     analyzed=('No. of characters given in the text are : '+str(len(djtext)))
    #     params = {'purpose': 'Characters Counted', 'analyzed_text': analyzed}
    #     djtext=analyzed
        
    if(removepunc!="on" and newlineremover!="on" and spaceremover!="on" and fullcaps!="on"):
    #    return HttpResponse("Please select the operation ! ") 
         params={'purpose':'Please select the operation!'}
         return render(request,'error.html',params)
    if(djtext== ""):
        params={'purpose':'Please enter the text!'}
        return render(request,'error.html',params)

    return render(request, 'analyze.html', params) 
 

