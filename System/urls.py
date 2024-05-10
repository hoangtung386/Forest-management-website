""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from App import HodViews, StaffViews, views
from System import settings

urlpatterns = (
    [
        path("demo", views.showDemoPage),
        #     path("signup_admin", views.signup_admin, name="signup_admin"),
        #     path("signup_student", views.signup_student, name="signup_student"),
        #     path("signup_staff", views.signup_staff, name="signup_staff"),
        #     path("do_admin_signup", views.do_admin_signup, name="do_admin_signup"),
        #     path("do_staff_signup", views.do_staff_signup, name="do_staff_signup"),
        #     path(
        #         "do_signup_student",
        #         views.do_signup_student,
        #         name="do_signup_student",
        #     ),
        #     path("admin/", admin.site.urls),
        #     path("accounts/", include("django.contrib.auth.urls")),
        path("", views.ShowLoginPage, name="show_login"),
        #     path("get_user_details", views.GetUserDetails),
        path("logout_user", views.logout_user, name="logout"),
        path(
            "check_email_exist",
            HodViews.check_email_exist,
            name="check_email_exist",
        ),
        path(
            "check_username_exist",
            HodViews.check_username_exist,
            name="check_username_exist",
        ),
        path("doLogin", views.doLogin, name="do_login"),
        path("admin_home", HodViews.admin_home, name="admin_home"),
        path("them_don_vi", HodViews.Them_donvi, name="them_don_vi"),
        path(
            "them_don_vi_save",
            HodViews.Them_donvi_save,
            name="them_don_vi_save",
        ),
        path("manage_don_vi", HodViews.manage_don_vi, name="manage_donvi"),
        path(
            "edit_don_vi/<str:donvi_id>",
            HodViews.edit_don_vi,
            name="edit_don_vi",
        ),
        path(
            "edit_donvi_save", HodViews.edit_don_vi_save, name="edit_donvi_save"
        ),
        path("add_staff", HodViews.add_staff, name="add_staff"),
        path("add_staff_save", HodViews.add_staff_save, name="add_staff_save"),
        path("manage_staff", HodViews.manage_staff, name="manage_staff"),
        path(
            "edit_staff/<str:staff_id>", HodViews.edit_staff, name="edit_staff"
        ),
        path(
            "edit_staff_save", HodViews.edit_staff_save, name="edit_staff_save"
        ),
        path(
            "add_loai_cay_giong",
            HodViews.add_loai_cay_giong,
            name="add_loai_cay_giong",
        ),
        path(
            "add_loai_cay_giong_save",
            HodViews.add_loai_cay_giong_save,
            name="add_loai_cay_giong_save",
        ),
        path(
            "manage_loai_cay_giong",
            HodViews.manage_loai_cay_giong,
            name="manage_loai_cay_giong",
        ),
        path(
            "edit_loai_cay_giong/<str:id_giong_cay>",
            HodViews.edit_loai_cay_giong,
            name="edit_loai_cay_giong",
        ),
        path(
            "edit_loai_cay_giong_save",
            HodViews.edit_loai_cay_giong_save,
            name="edit_loai_cay_giong_save",
        ),
        path(
            "add_co_so_san_xuat_cay_giong",
            HodViews.add_co_so_san_xuat_cay_giong,
            name="add_co_so_san_xuat_cay_giong",
        ),
        path(
            "add_co_so_san_xuat_cay_giong_save",
            HodViews.add_co_so_san_xuat_cay_giong_save,
            name="add_co_so_san_xuat_cay_giong_save",
        ),
        path(
            "manage_co_so_san_xuat_cay_giong",
            HodViews.manage_co_so_san_xuat_cay_giong,
            name="manage_co_so_san_xuat_cay_giong",
        ),
        path(
            "edit_co_so_san_xuat_cay_gong/<str:co_so_sx_cay_giong_id>",
            HodViews.edit_co_so_san_xuat_cay_gong,
            name="edit_co_so_san_xuat_cay_gong",
        ),
        path(
            "edit_co_so_san_xuat_cay_gong",
            HodViews.edit_co_so_san_xuat_cay_gong,
            name="edit_co_so_san_xuat_cay_gong",
        ),

        path(
            "add_loai_hinh_san_xuat",
            HodViews.add_loai_hinh_san_xuat,
            name="add_loai_hinh_san_xuat",
        ),
        path(
            "add_loai_hinh_san_xuat_save",
            HodViews.add_loai_hinh_san_xuat_save,
            name="add_loai_hinh_san_xuat_save",
        ),
        path(
            "manage_loai_hinh_san_xuat",
            HodViews.manage_loai_hinh_san_xuat,
            name="manage_loai_hinh_san_xuat",
        ),
        path(
            "edit_loai_hinh_san_xuat/<str:id_san_xuat>",
            HodViews.edit_loai_hinh_san_xuat,
            name="edit_loai_hinh_san_xuat",
        ),
        path(
            "edit_loai_hinh_san_xuat_save",
            HodViews.edit_loai_hinh_san_xuat_save,
            name="edit_loai_hinh_san_xuat_save",
        ),
        path(
            "add_co_so_luu_tru_dong_vat",
            HodViews.add_co_so_luu_tru_dong_vat,
            name="add_co_so_luu_tru_dong_vat",
        ),
        path(
            "add_co_so_luu_tru_dong_vat_save",
            HodViews.add_co_so_luu_tru_dong_vat_save,
            name="add_co_so_luu_tru_dong_vat_save",
        ),
        path(
            "manage_co_so_luu_tru_dong_vat",
            HodViews.manage_co_so_luu_tru_dong_vat,
            name="manage_co_so_luu_tru_dong_vat",
        ),
        path(
            "edit_co_so_luu_tru_dong_vat/<str:id_co_so>",
            HodViews.edit_co_so_luu_tru_dong_vat,
            name="edit_co_so_luu_tru_dong_vat",
        ),
        path(
            "edit_co_so_luu_tru_dong_vat_save",
            HodViews.edit_co_so_luu_tru_dong_vat_save,
            name="edit_co_so_luu_tru_dong_vat_save",
        ),
        path(
            "add_hinh_thuc_hoat_dong",
            HodViews.add_hinh_thuc_hoat_dong,
            name="add_hinh_thuc_hoat_dong",
        ),
        path(
            "add_hinh_thuc_hoat_dong_save",
            HodViews.add_hinh_thuc_hoat_dong_save,
            name="add_hinh_thuc_hoat_dong_save",
        ),
        path(
            "manage_hinh_thuc_hoat_dong",
            HodViews.manage_hinh_thuc_hoat_dong,
            name="manage_hinh_thuc_hoat_dong",
        ),
        path(
            "edit_hinh_thuc_hoat_dong/<str:id_hinh_thuc_hoat_dong>",
            HodViews.edit_hinh_thuc_hoat_dong,
            name="edit_hinh_thuc_hoat_dong",
        ),
        path(
            "edit_hinh_thuc_hoat_dong_save",
            HodViews.edit_hinh_thuc_hoat_dong_save,
            name="edit_hinh_thuc_hoat_dong_save",
        ),
        path(
            "add_loai_bien_dong",
            HodViews.add_loai_bien_dong,
            name="add_loai_bien_dong",
        ),
        path(
            "add_loai_bien_dong_save",
            HodViews.add_loai_bien_dong_save,
            name="add_loai_bien_dong_save",
        ),
        path(
            "manage_loai_bien_dong",
            HodViews.manage_loai_bien_dong,
            name="manage_loai_bien_dong",
        ),
        path(
            "edit_loai_bien_dong/<str:id_loai_bien_dong>",
            HodViews.edit_loai_bien_dong,
            name="edit_loai_bien_dong",
        ),
        path(
            "edit_loai_bien_dong_save",
            HodViews.edit_loai_bien_dong_save,
            name="edit_loai_bien_dong_save",
        ),

        path(
            "add_loai_dong_vat_quy",
            HodViews.add_loai_dong_vat_quy,
            name="add_loai_dong_vat_quy",
        ),
        path(
            "add_loai_dong_vat_quy_save",
            HodViews.add_loai_dong_vat_quy_save,
            name="add_loai_dong_vat_quy_save",
        ),
        path(
            "manage_loai_dong_vat_quy",
            HodViews.manage_loai_dong_vat_quy,
            name="manage_loai_dong_vat_quy",
        ),
        path(
            "edit_loai_dong_vat_quy/<str:id_dong_vat>",
            HodViews.edit_loai_dong_vat_quy,
            name="edit_loai_dong_vat_quy",
        ),
        path(
            "edit_loai_dong_vat_quy_save",
            HodViews.edit_loai_dong_vat_quy_save,
            name="edit_loai_dong_vat_quy_save",
        ),
        path("admin_profile", HodViews.admin_profile, name="admin_profile"),
        path("admin_profile_save", HodViews.admin_profile_save, name="admin_profile_save"),
        # Staff
        path("staff_home", StaffViews.staff_home, name="staff_home"),
        path("staff_profile", StaffViews.staff_profile, name="staff_profile"),
        path(
            "staff_profile_save",
            StaffViews.staff_profile_save,
            name="staff_profile_save",
        ),
        path("add_cay_giong", StaffViews.add_cay_giong, name="add_cay_giong"),
        path(
            "add_cay_giong_save",
            StaffViews.add_cay_giong_save,
            name="add_cay_giong_save",
        ),
        path(
            "manage_cay_giong",
            StaffViews.manage_cay_giong,
            name="manage_cay_giong",
        ),
        path(
            "edit_cay_giong/<str:cay_giong_id>",
            StaffViews.edit_cay_giong,
            name="edit_cay_giong",
        ),
        path(
            "edit_cay_giong_save",
            StaffViews.edit_cay_giong_save,
            name="edit_cay_giong_save",
        ),
        path("add_cssx_che_bien_go", StaffViews.add_cssx_che_bien_go, name="add_cssx_che_bien_go"),
        path("add_cssx_che_bien_go_save", StaffViews.add_cssx_che_bien_go_save, name="add_cssx_che_bien_go_save"),
        path("manage_cssx_che_bien_go", StaffViews.manage_cssx_che_bien_go, name="manage_cssx_che_bien_go"),
        path("edit_cssx_che_bien_go/<str:cssx_che_bien_go_id>", StaffViews.edit_cssx_che_bien_go, name="edit_cssx_che_bien_go"),
        path("edit_cssx_che_bien_go_save", StaffViews.edit_cssx_che_bien_go_save, name="edit_cssx_che_bien_go_save"),
        path("add_dong_vat_quy", StaffViews.add_dong_vat_quy, name="add_dong_vat_quy"),
        path("add_dong_vat_quy_save", StaffViews.add_dong_vat_quy_save, name="add_dong_vat_quy_save"),
        path("manage_dong_vat_quy", StaffViews.manage_dong_vat_quy, name="manage_dong_vat_quy"),
        path("edit_dong_vat_quy/<str:dong_vat_quy_id>",StaffViews.edit_dong_vat_quy, name="edit_dong_vat_quy"),
        path("edit_dong_vat_quy_save", StaffViews.edit_dong_vat_quy_save, name="edit_dong_vat_quy_save"),

        
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
