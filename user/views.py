from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout #kullanıcının olup olmadığını sorgulayacak
# Create your views here.

def register(request):

    #"""" ile gösterilen kısımlar uzun ve karmaşık olduğu için başka bir yöntem kullancazç

    form = RegisterForm(request.POST or None)#post mu get mi diye kontrol etmemize gerek kalmıyor
    if form.is_valid():#clean metodu çağrılıyo bu şekilde yazmamız lazım

            #true döndüğü durumda ordaki değğerleri alıyooruz
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            #kullanıcıyı oluşturcaz
            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()
            #bu şekilde kullanıcımızı kayıt etmiş olduk
            login(request,newUser)#kayıt olduktan sonra otomatik şekilde login olmuş oldu
            messages.success(request,"Başarıyla Kayıt Oldunuz...")
            return redirect("index")#kayıt olduktan sonra anasayfa gelcek bu şekilde    

    context = {
       "form": form
        
    }  #is valid true değilse aynı sayfayı render almak için bu kısmı koyduk
    return render(request,"register.html",context) 


    """ if request.method == "POST":# formun post olup olmadığını sorguladık
        form = RegisterForm(request.POST)#postsa formdan gelen bilgilerle doldurduk

        if form.is_valid():#clean metodu çağrılıyo bu şekilde yazmamız lazım

            #true döndüğü durumda ordaki değğerleri alıyooruz
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            #kullanıcıyı oluşturcaz
            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()
            #bu şekilde kullanıcımızı kayıt etmiş olduk
            login(request,newUser)#kayıt olduktan sonra otomatik şekilde login olmuş oldu
            return redirect("index")#kayıt olduktan sonra anasayfa gelcek bu şekilde
        context = {
            "form": form
        
        }  #is valid true değilse aynı sayfayı render almak için bu kısmı koyduk
        return render(request,"register.html",context) 

    else:
        form = RegisterForm() 
        context = {
            "form": form

        }  
        return render(request,"register.html",context)     """
    # form = RegisterForm()
    # context = {
    #     "form": form
    # }
    # return render(request,"register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
         "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is None :
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş Yaptınız.")
        login(request,user)
        return redirect("index")



    
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")