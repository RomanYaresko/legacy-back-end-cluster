from ast import If
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from user_communication.views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('account/reg/', Account.as_view(), name="register"),
    path('account/log/', Account.as_view(form_class = UserLog), name="login"),
    path('account/logout/', logout, name="logout"),
    path('account/', account, name="account"),
    path('lab/new_figure/', CreateFigure.as_view(), name="new_figure"),
    path('lab/', Lab.as_view(), name="lab"),
    path('user/<slug:username_slug>/', User.as_view(), name="user"),
    path('home/', cache_page(60)(Index.as_view()), name="home"),
    path('admin/', admin.site.urls),
    path('__debug__/', include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:

    urlpatterns = [
        path('__debug__/', include("debug_toolbar.urls")),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
