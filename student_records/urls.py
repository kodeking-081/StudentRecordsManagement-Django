from django.urls import path
from student_records import views

urlpatterns = [
    path("",views.student_list, name="student-list"),
    path("delete/<int:id>/",views.delete_record, name="delete-record"),
    path("add/",views.add_record, name="add-record"),
    path("details/<int:id>",views.show_record, name="view-record"),
    path("edit/<int:id>/", views.update_details, name="update-details"),
]