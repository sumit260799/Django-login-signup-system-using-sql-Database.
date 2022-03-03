from django.shortcuts import render,HttpResponse
import mysql.connector as sql
# Create your views here.
#def inde(request):
    #return render(request,'signup_page.html')
   # return render(request,'signup.html')
    #return HttpResponse('this is homepage')
  
fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def index(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="sumit99",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup.html')
