from turtle import update
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from App.models import portfolioTable
from App.models import customerTable

# Create your views here.

# Admin Dashboard


def admindashboard(request):
    if request.user.is_authenticated:
        return render(request, 'admindashboard.html', {'name': request.user})
    else:
        return redirect('/admin_login/')


def dashboardindex(request):
    return render(request, 'dashboardindex.html')


def packages(request):
    return render(request, 'packages.html')


def customer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        customerR = customerTable(
            name=name, email=email, phone=phone, desc=desc)
        customerR.save()

    return render(request, 'customer.html')


def Portfolio(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        filename = request.FILES["filename"]
        longDesc = request.POST.get("longDesc")
        portfolio = portfolioTable(title=title, desc=desc,
                                   filename=filename, longDesc=longDesc)
        portfolio.save()

    return render(request, 'Portfolio.html')


def Service(request):
    return render(request, 'Service.html')


def NFTs(request):
    return render(request, 'NFTs.html')


def carreerForm(request):
    return render(request, 'carreerform.html')


def TeamForm(request):
    return render(request, 'teamform.html')


def BlogArticleForm(request):
    return render(request, 'Article.html')
# Admin dashboard end


def blogDetail(request):
    return render(request, 'blog-detail.html')


def PortfolioDetail(request):
    return render(request, 'portfolio-detail.html')


def servicedetail(request):
    return render(request, 'service-detail.html')


def Error(request):
    return render(request, '404.html')


# sarah
def home(request):
    return render(request, 'index.html')


def team(request):
    return render(request, 'team.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def career(request):
    return render(request, 'career.html')


# def blogs(request):
#     return render(request, 'blogs.html')

# def login(request):
#     return render(request, 'login.html')

# sapna
def blogsindex(request):
    return render(request, 'blogs-index.html')


def portfolio(request):

    return render(request, 'portfolio-index.html')


def carrerindex(request):
    return render(request, 'carreerindex.html')

# def contactus(request):
#     return render(request,'contactus.html')


def aboutus(request):
    return render(request, 'about-us-2.html')


def passwordreset(request):
    fm = PasswordChangeForm(user=request.user)
    return render(request, 'passwordreset.html', {'form': fm})


def Portfolionft(request):
    return render(request, 'portfolio-nft.html')


def termcondition(request):
    return render(request, 'faq.html')


def privacypolicy(request):
    return render(request, 'privacy-policy.html')


def pricepackage(request):
    return render(request, 'pricepackage.html')

# Login Admin


def admin_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return redirect('/admindashboard/')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})


def admin_logout(request):
    logout(request)
    return redirect('/admin_login/')


def changepasword(request):
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            return HttpResponseRedirect('/admindashboard/')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'ChangePassword.html', {'form': fm})
