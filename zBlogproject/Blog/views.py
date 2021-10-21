
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from Blog.form import sign,Edit_Pofile,Admin_Pofile,Login_form,Postform,EditPassword
from django.contrib.auth import authenticate,login ,logout,update_session_auth_hash
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group,User

# Create your views here.
def home(request):
    p=Post.objects.all()
    return render(request,"home.html",{'post':p})

def about(request):
    return render(request,"About.html")

def contact(request):
    return render(request,"contact.html")



def Signup(request):
    if request.method=="POST":
        fm=sign(request.POST)
        if fm.is_valid():
            con=fm.save()
            gp=Group.objects.get(name="Author")
            con.groups.add(gp)

            messages.success(request,"Sucessfully register your data!!!")
    else:
        fm=sign()
    return render(request,'signup.html',{"form":fm})



def Login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
           fm=Login_form(request=request,data=request.POST)
           if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,"Successfully login!!")
                return HttpResponseRedirect('/d/')
                
        else:
            fm=Login_form()
        return render(request,"login.html",{'forms':fm})
    else:
        return HttpResponseRedirect('/d/')


def Dash(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()

        user1=request.user
        full_name=user1.get_full_name()

        gps=user1.groups.all()


        
        return render(request,'Dashboard.html',{'post':posts,'full':full_name,'group':gps})
    else:
        return HttpResponseRedirect("/l/")



def Add(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=Postform(request.POST)
            if fm.is_valid():
                tt=fm.cleaned_data['Title']
                ds=fm.cleaned_data['Desc']
                ch=Post(Title=tt,Desc=ds)
                ch.save()
                messages.success(request,"Add Successfully!!!")
        else:
            fm=Postform()
        return render(request,"add.html",{'form':fm})
    else:
        return HttpResponseRedirect("/l/")



def Edit(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            ed=Postform(request.POST,instance = pi )
            if ed.is_valid():
                ed.save()
                messages.success(request,"Add Successfully!!!")
        else:
            pi=Post.objects.get(pk=id)
            ed=Postform(instance=pi)
        return render (request,"edit.html",{'edit':ed})
    else:
        return HttpResponseRedirect('/l/')





def Delete(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=Post.objects.get(pk=id)
            fm.delete()
            return HttpResponseRedirect("/d/")
    else:
        return HttpResponseRedirect('/l/')







def Profile(request):
    # if request.user.is_authenticated:
        if request.method=="POST":
            if request.user.is_superuser==True:
                fm=Admin_Pofile(request.POST,instance=request.user)
                
                #This is used for rendering user profile in admin profile
                details=User.objects.all() 

            else:
                fm=Edit_Pofile(request.POST,instance=request.user)
                details=None

            if fm.is_valid():
                fm.save()
                messages.success(request,"update successfully!!")
        else:
            if request.user.is_superuser==True :
                fm=Admin_Pofile(instance=request.user)
                details=User.objects.all()

            else:
                fm=Edit_Pofile(instance=request.user)
                details=None
        return render(request,'profile.html',{'form':fm,'name':request.user.username,'data':details})
    # else:
    #     return HttpResponseRedirect('/l/')




def Detail(request,id):
    pi=User.objects.get(pk=id)
    fm=Edit_Pofile(instance=pi)
    return render(request,"detail.html",{'form':fm,'name':request.user})





def Logout(request):
    logout(request)
    return HttpResponseRedirect('/l/')


def changepass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
          ps=EditPassword(user=request.user,data=request.POST)
          if ps.is_valid():
            ps.save()
            update_session_auth_hash(request,ps.user)
            messages.success(request,"Successfully Change password !!")
            return HttpResponseRedirect('/profile/')
        else:
            ps=EditPassword(user=request.user)
        return render(request,"changepass.html",{'pass':ps,"name":request.user})
    else:
        return HttpResponseRedirect("/l/")



