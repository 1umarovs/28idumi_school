from django.urls import path
from . import views
from members.views import login_user,logout_user,register_user

app_name = 'main'

urlpatterns = [
    path('' , views.Home, name='homePage'),
    path("News/detail/<slug:slug>", views.News_detail, name="newDetail"),
    path("News/", views.NewsPage, name="News"),
    # path("Search", views.searchbar, name="search"),
    path('about/', views.About , name='about'),
    path("only_us/", views.Elements, name="elements"),
    path("courses/", views.Courses, name="courses"),
    path("contact/", views.Contact, name="Contact"),
    path("achivments/", views.Achivments, name="achivments"),
    path("achivments/<slug:slug>", views.AchivmentsDetail, name="achivmentsDetail"),
    path("login/", login_user, name="login"),
    path("logout/",logout_user, name="logout"),
    path("registration/", register_user , name="register"),
    path("teachers/<slug:slug>", views.TeachersDetail, name="teacherProfile"),
]