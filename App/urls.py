from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import(

    blogDetail, PortfolioDetail, servicedetail, Error, home, team,
    services,
    contact,
    career,
    blogsindex,
    aboutus,
    carrerindex,
    portfolio,
    blogsindex,
    termcondition,
    Portfolionft,
    privacypolicy,
    pricepackage,
    passwordreset, admindashboard, dashboardindex, packages, customer, Portfolio, Service, NFTs,
    TeamForm, carreerForm, BlogArticleForm, admin_login, admin_logout, changepasword






)

urlpatterns = [
    path('', home, name='home'),
    path('blogDetail', blogDetail, name='blogDetail'),
    path('PortfolioDetail', PortfolioDetail, name='PortfolioDetail'),
    path('servicedetail', servicedetail, name='servicedetail'),
    path('Error', Error, name='Error'),
    path('team', team, name='team'),
    path('services', services, name='services'),
    path('contact', contact, name='contact'),
    path('career', career, name='career'),
    path('admin_login/', admin_login, name='admin_login'),
    path('blogsindex', blogsindex, name='blogsindex'),
    path('portfolio', portfolio, name="portfolio"),
    path('aboutus', aboutus, name="aboutus"),
    path('carrerindex', carrerindex, name="carrerindex"),
    path('termcondition', termcondition, name="termcondition"),
    path('Portfolionft', Portfolionft, name="Portfolionft"),
    path('privacypolicy', privacypolicy, name="privacypolicy"),
    path('pricepackage', pricepackage, name="pricepackage"),
    path('passwordreset', passwordreset, name="passwordreset"),
    # Admin Dashboard
    path('admindashboard/', admindashboard, name="admindashboard"),
    path('dashboardindex', dashboardindex, name="dashboardindex"),
    path('packages', packages, name="packages"),
    path('customer', customer, name="customer"),
    path('Portfolio', Portfolio, name="Portfolio"),
    path('Service', Service, name="Service"),
    path('NFTs', NFTs, name="NFTs"),
    path('carreerForm', carreerForm, name="carreerForm"),
    path('TeamForm', TeamForm, name="TeamForm"),
    path('BlogArticleForm', BlogArticleForm, name="BlogArticleForm"),
    path('admin_logout', admin_logout, name="admin_logout"),
    # password
    # 'password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset/done/',auth_views.PasswordReset.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),
    # path('', include('blog.urls')),
    path('changepasword', changepasword, name="changepasword"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
