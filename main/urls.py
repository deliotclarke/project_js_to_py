from django.urls import path
from main import views
from main.models import comment

homeListView = views.HomeListView.as_view(
    queryset=comment.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="main/home.html",
)

urlpatterns = [
    path("", homeListView, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("comment/", views.add_comment, name="comment"),
]
