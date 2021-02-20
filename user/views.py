from django.shortcuts import render,redirect

from django.views.generic import ListView

from django.contrib.auth.decorators import login_required


from .forms import RegisterForm
from .forms import LoginForm,UserUpdateForm,ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User 

from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

def register(request) :
    all_user = User.objects.all().order_by("username")
    all_email = User.objects.all()
    form = RegisterForm(request.POST or None)
    if  form.is_valid() :
        email =form.cleaned_data.get("email")
        username = form.cleaned_data.get("username")

        password = form.cleaned_data.get("password")

        newUser = User(username=username,email=email )
        newUser.set_password(password)

        newUser.save()

        login(request,newUser)

        messages.success(request,"Başarıyla kayıt oldunuz  Giriş yapınız ")

        return redirect("index")

    else :
        context = {
            "form" : form ,
            "all_user":all_user,
            "all_email":all_email
        }
        return render(request,"register.html",context)




def loginUser(request):
    form = LoginForm(request.POST or None )
    context = {
        "form" : form 
    }

    if form.is_valid() :

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user =authenticate(username =username,password =password)
        if user is  None :
            messages.info(request,"Kullanıcı Adı  veya Parola  yanlış ")
            return render(request,"login.html",context)
        else :
            messages.success(request,"Başarıyla giriş yaptınız ")
            login(request, user)
            return redirect("index")
 
    else :
    
        return render(request,"login.html",context)



def logoutUser(request):    

    logout(request) 
    messages.success(request,"Başarıyla cıkış yaptınız ")
    return redirect("index")




def User_Profile(request):

    if request.method == "POST" :
        
        u_form =  UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST , request.FILES or None ,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid() : 
            u_form.save()
            p_form.save()
            messages.success(request,"Kullanıcı bilgileri , fotoda  basarıyla güncellendi .. .")
            return redirect('user:profile')

    else : 
        u_form =  UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm( instance=request.user.profile)

    context ={ 

        "u_form":u_form ,
        "p_form":p_form
    }


    return render(request ,"profile.html",context)




