from django.urls import path


from .views import ListEquities


urlpatterns = [
    path("", ListEquities.as_view(), name="list_equities"),
]
