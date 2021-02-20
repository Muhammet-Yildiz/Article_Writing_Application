
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from article import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name ="index"),
    path('about/', views.about,name ="about"),
    path('user/',include("user.urls")),
    path('articles/',include("article.url")),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

