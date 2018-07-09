from django.conf.urls import url
from django.contrib import admin
from blogposts import views
#to get images
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    #post_id is just a variable which will later be used in views.py to obtain post.id
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_details, name="blogpost_details"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
