from . import views
from django.urls import path

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("data/", views.DataTable.as_view(), name="data"),
    path("upload-data/", views.UploadDetails.as_view(), name="upload-data"),
    path("update-data/<int:pk>", views.UpdateDetails.as_view(), name="update-data"),
    path("delete-data/<int:pk>", views.DeleteDetails.as_view(), name="delete-data"),
    path("update-total-hits/", views.update_total_hits, name="update-total-hits"),
    path('rate-data/', views.rate_data, name='rate-data'),
    path("user-details/", views.UserDetails.as_view(), name="user-details"),
    path("user-update/<int:pk>",
         views.UpdateSingleUserData.as_view(), name="user-update"),

    path("dum", views.dummy, name="dum"),
    path("personal-detail", views.PersonalDetails.as_view(), name="personal-detail"),
    path("manage-permission/<int:pk>",
         views.ManageUserPermissions.as_view(), name="manage"),

    path("update-your-detail/<uuid:uuid>",
         views.UpdateYourDetail.as_view(), name="update-your-detail"),

    #     path("c", views.count_visit, name="c"),
]
