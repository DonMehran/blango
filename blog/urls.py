# other imports
import blog.views
from django.urls import path, include

urlpatterns = [
    # other patterns
    path("", blog.views.index),
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail")
]