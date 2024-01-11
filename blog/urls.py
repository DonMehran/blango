# other imports
import blog.views
from django.urls import path, include

urlpatterns = [
    # other patterns
    path("", blog.views.index)
]