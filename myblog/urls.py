from django.conf.urls import url
from django.contrib import admin
import blogposts.views
import sitepages.views
#to get images
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blogposts.views.home, name="home"),
    #post_id is just a variable which will later be used in views.py to obtain post.id
    url(r'^posts/(?P<post_id>[0-9]+)/$', blogposts.views.post_details, name="blogpost_details"),
    url(r'^about/', sitepages.views.about, name="about")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
