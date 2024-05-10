import json

import requests
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from App.models import (
    CanBoNghiepVu,
    CoSoLuuTruDongVat,
    CoSoSanXuatCayGiong,
    CustomUser,
    Donvi,
    HinhThucHoatDong,
    LoaiBienDong,
    LoaiCayGiong,
    LoaiDongVatQuy,
    LoaiHinhSanXuat,
)


def admin_home(request):
    CanBoNghiepVu_count = CanBoNghiepVu.objects.all().count()
    LoaiCayGiong_count = LoaiCayGiong.objects.all().count()
    LoaiDongVatQuyHiem_count = LoaiDongVatQuy.objects.all().count()
    CoSoSanXuatCayGiong_count = CoSoSanXuatCayGiong.objects.all().count()

    return render(
        request,
        "hod_template/home_content.html",
        {
            "CanBoNghiepVu_count": CanBoNghiepVu_count,
            "LoaiCayGiong_count": LoaiCayGiong_count,
            "LoaiDongVatQuyHiem_count": LoaiDongVatQuyHiem_count,
            "CoSoSanXuatCayGiong_count": CoSoSanXuatCayGiong_count,
        },
    )


def add_staff(request):
    don_vi_all = Donvi.objects.all()
    return render(
        request,
        "hod_template/add_staff_template.html",
        {"don_vi_all": don_vi_all},
    )


def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        
        try:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            chuc_vu = request.POST.get("chuc_vu")
            don_vi_id = request.POST.get("don_vi")
            don_vi_ = Donvi.objects.get(id=don_vi_id)
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                last_name=last_name,
                first_name=first_name,
                user_type=2,
            )
            user.canbonghiepvu.don_vi = don_vi_
            user.canbonghiepvu.chuc_vu = chuc_vu
            user.save()
            messages.success(request, "Successfully Added Staff")
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request, "Failed to Add Staff")
            return HttpResponseRedirect(reverse("add_staff"))


def manage_staff(request):
    staffs = CanBoNghiepVu.objects.all()
    return render(
        request, "hod_template/manage_staff_template.html", {"staffs": staffs}
    )


def edit_staff(request, staff_id):
    staff = CanBoNghiepVu.objects.get(admin=staff_id)
    don_vi_all = Donvi.objects.all()
    return render(
        request,
        "hod_template/edit_staff_template.html",
        {"staff": staff, "don_vi_all": don_vi_all},
    )


def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            staff_id = request.POST.get("staff_id")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            chuc_vu = request.POST.get("chuc_vu")
            don_vi_id = request.POST.get("don_vi")
            don_vi_ = Donvi.objects.get(id=don_vi_id)
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.password = password
            user.save()

            staff_model = CanBoNghiepVu.objects.get(admin=staff_id)
            staff_model.don_vi = don_vi_
            staff_model.chuc_vu = chuc_vu
            staff_model.save()

            messages.success(request, "Successfully update Staff")
            return HttpResponseRedirect(
                reverse("edit_staff", kwargs={"staff_id": staff_id})
            )
        except:
            messages.error(request, "Failed to update Staff")
            return HttpResponseRedirect(
                reverse("edit_staff", kwargs={"staff_id": staff_id})
            )


def Them_donvi(request):
    return render(request, "hod_template/add_donvi.html")


def Them_donvi_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        ten_don_vi = request.POST.get("don_vi")
        dia_chi = request.POST.get("dia_chi")
        try:
            donvi = Donvi(ten_don_vi=ten_don_vi, vi_tri=dia_chi)
            donvi.save()
            messages.success(request, "Successfully Added don vi")
            return HttpResponseRedirect(reverse("them_don_vi"))
        except:
            messages.error(request, "Failed to Add don vi")
            return HttpResponseRedirect(reverse("them_don_vi"))


def manage_don_vi(request):
    donvi_all = Donvi.objects.all()
    return render(
        request, "hod_template/manage_don_vi.html", {"donvi_all": donvi_all}
    )


def edit_don_vi(request, donvi_id):
    don_vi = Donvi.objects.get(id=donvi_id)
    return render(request, "hod_template/edit_donvi.html", {"don_vi": don_vi})


def edit_don_vi_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            don_vi_id = request.POST.get("donvi_id")
            ten_don_vi = request.POST.get("don_vi")
            dia_chi = request.POST.get("dia_chi")
            donvi = Donvi.objects.get(id=don_vi_id)
            donvi.ten_don_vi = ten_don_vi
            donvi.vi_tri = dia_chi
            donvi.save()
            messages.success(request, "Successfully Updated don vi")
            return HttpResponseRedirect(
                reverse("edit_don_vi", kwargs={"donvi_id": don_vi_id})
            )
        except:
            messages.error(request, "Failed to update don vi")
            return HttpResponseRedirect(
                reverse("manage_donvi", kwargs={"donvi_id": don_vi_id})
            )


def add_loai_cay_giong(request):
    return render(request, "hod_template/add_loai_cay_giong.html")


def add_loai_cay_giong_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            ten_loai_cay_giong = request.POST.get("loai_cay_giong")
            ngay_cap_phep = request.POST.get("ngay_cap_phep")
            loai_cay_giong = LoaiCayGiong(
                ten_giong=ten_loai_cay_giong, Ngay_cap_phep=ngay_cap_phep
            )
            loai_cay_giong.save()
            messages.success(request, "Successfully Create loai giong cay moi")
            return HttpResponseRedirect(reverse("add_loai_cay_giong"))
        except:
            messages.error(request, "Failed Create loai giong cay moi")
            return HttpResponseRedirect(reverse("add_loai_cay_giong"))


def manage_loai_cay_giong(request):
    loai_cay_giong_all = LoaiCayGiong.objects.all()
    return render(
        request,
        "hod_template/manage_loai_cay_giong.html",
        {"loai_cay_giong_all": loai_cay_giong_all},
    )


def edit_loai_cay_giong(request, id_giong_cay):
    giong_cay = LoaiCayGiong.objects.get(id=id_giong_cay)
    return render(
        request,
        "hod_template/edit_loai_cay_giong.html",
        {"giong_cay": giong_cay},
    )


def edit_loai_cay_giong_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            cay_giong_id = request.POST.get("giong_cay_id")
            ten_loai_cay_giong = request.POST.get("loai_cay_giong")
            ngay_cap_phep = request.POST.get("ngay_cap_phep")
            loai_cay_giong = LoaiCayGiong.objects.get(id=cay_giong_id)
            loai_cay_giong.ten_giong = ten_loai_cay_giong
            loai_cay_giong.Ngay_cap_phep = ngay_cap_phep
            loai_cay_giong.save()
            messages.success(request, "Successfully update loai giong cay moi")
            return HttpResponseRedirect(
                reverse(
                    "edit_loai_cay_giong", kwargs={"id_giong_cay": cay_giong_id}
                )
            )
        except:
            messages.error(request, "Failed Update loai giong cay moi")
            return HttpResponseRedirect(
                reverse(
                    "edit_loai_cay_giong", kwargs={"id_giong_cay": cay_giong_id}
                )
            )


def add_co_so_san_xuat_cay_giong(request):
    return render(request, "hod_template/add_co_so_san_xuat_cay_giong.html")


def add_co_so_san_xuat_cay_giong_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            ten_co_so = request.POST.get("ten_co_so")
            dia_chi = request.POST.get("dia_chi")
            ngay_cap_phep = request.POST.get("ngay_cap_phep")
            co_so_sx_cay_giong = CoSoSanXuatCayGiong(
                ten_co_so=ten_co_so,
                dia_diem=dia_chi,
                ngay_cap_phep=ngay_cap_phep,
            )
            co_so_sx_cay_giong.save()
            messages.success(
                request, "Successfully create co so san xuat giong cay moi"
            )
            return HttpResponseRedirect(reverse("add_co_so_san_xuat_cay_giong"))
        except:
            messages.error(
                request, "Failed create co so san xuat giong cay moi"
            )
            return HttpResponseRedirect(reverse("add_co_so_san_xuat_cay_giong"))


def manage_co_so_san_xuat_cay_giong(request):
    co_so_san_xuat_cay_giong_all = CoSoSanXuatCayGiong.objects.all()
    return render(
        request,
        "hod_template/manage_cs_sx_cay_giong.html",
        {"co_so_san_xuat_cay_giong_all": co_so_san_xuat_cay_giong_all},
    )


def edit_co_so_san_xuat_cay_gong(request, co_so_sx_cay_giong_id):
    co_so_sx_cay_giong = CoSoSanXuatCayGiong.objects.get(
        id=co_so_sx_cay_giong_id
    )
    return render(request, "hod_template/edit_cs_sx_cay_giong.html", {"co_so_sx_cay_giong": co_so_sx_cay_giong})

def edit_co_so_san_xuat_cay_gong_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            co_so_id = request.POST.get("co_so_id")
            ten_co_so = request.POST.get("ten_co_so")
            dia_chi = request.POST.get("dia_chi")
            ngay_cap_phep = request.POST.get("ngay_cap_phep")
            co_so_sx_cay_giong = CoSoSanXuatCayGiong.objects.get(id=co_so_id)
            co_so_sx_cay_giong.ten_co_so = ten_co_so
            co_so_sx_cay_giong.dia_diem = dia_chi
            co_so_sx_cay_giong.ngay_cap_phep = ngay_cap_phep
            co_so_sx_cay_giong.save()
            messages.success(request, "Successfully update co so sx cay giong")
            return HttpResponseRedirect(
                reverse(
                    "edit_co_so_san_xuat_cay_gong", kwargs={"co_so_sx_cay_giong_id": co_so_id}
                )
            )
        except:
            messages.error(request, "Failed Update loai giong cay moi")
            return HttpResponseRedirect(
                reverse(
                    "edit_co_so_san_xuat_cay_gong", kwargs={"co_so_sx_cay_giong_id": co_so_id}
                )
            )
        
def add_loai_hinh_san_xuat(request):
    return render(
        request,"hod_template/add_loai_hinh_san_xuat.html"
    )
def add_loai_hinh_san_xuat_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        try:
            ten_loai_hinh_san_xuat = request.POST.get("ten_loai_hinh_san_xuat")
            loai_hinh_san_xuat = LoaiHinhSanXuat(
                ten_loai_hinh_san_xuat=ten_loai_hinh_san_xuat
            )
            loai_hinh_san_xuat.save()
            messages.success(request, "Successfully Create loai hinh san xuat moi")
            return HttpResponseRedirect(reverse("add_loai_hinh_san_xuat"))
        except:
            messages.error(request, "Failed Create loai hinh san xuat moi")
            return HttpResponseRedirect(reverse("add_loai_hinh_san_xuat"))

def manage_loai_hinh_san_xuat(request):
    loai_hinh_san_xuat_all = LoaiHinhSanXuat.objects.all()
    return render(
        request,
        "hod_template/manage_loai_hinh_san_xuat.html",
        {"loai_hinh_san_xuat_all": loai_hinh_san_xuat_all},
    )

def edit_loai_hinh_san_xuat(request, id_san_xuat):
    loai_hinh_san_xuat = LoaiHinhSanXuat.objects.get(id=id_san_xuat)
    return render(
        request,
        "hod_template/edit_loai_hinh_san_xuat.html",
        {"loai_hinh_san_xuat": loai_hinh_san_xuat},
    )

def edit_loai_hinh_san_xuat_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            id_san_xuat = request.POST.get("id_san_xuat")
            ten_loai_hinh_san_xuat = request.POST.get("loai_hinh_san_xuat")
            loai_hinh_san_xuat = LoaiHinhSanXuat.objects.get(id=id_san_xuat)
            loai_hinh_san_xuat.ten_loai_hinh_san_xuat = ten_loai_hinh_san_xuat
            loai_hinh_san_xuat.save()
            messages.success(request, "Successfully update loai giong cay moi")
            return HttpResponseRedirect(
                reverse(
                    "edit_loai_hinh_san_xuat", kwargs={"id_san_xuat": id_san_xuat}
                )
            )
        except:
            messages.error(request, "Failed Update loai giong cay moi")
            return HttpResponseRedirect(
                reverse(
                    "edit_loai_hinh_san_xuat", kwargs={"id_san_xuat": id_san_xuat}
                )
            )

def add_hinh_thuc_hoat_dong(request):
    return render(
        request,"hod_template/add_hinh_thuc_hoat_dong.html"
    )
def add_hinh_thuc_hoat_dong_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            ten_hinh_thuc_hoat_dong = request.POST.get("hinh_thuc_hoat_dong")
            hinh_thuc_hoat_dong = HinhThucHoatDong(
                ten_hinh_thuc_hoat_dong=ten_hinh_thuc_hoat_dong
            )
            hinh_thuc_hoat_dong.save()
            messages.success(request, "Successfully Create hinh thuc hoat dong")
            return HttpResponseRedirect(reverse("add_hinh_thuc_hoat_dong"))
        except:
            messages.error(request, "Failed Create hinh thuc hoat dong")
            return HttpResponseRedirect(reverse("add_hinh_thuc_hoat_dong"))

def manage_hinh_thuc_hoat_dong(request):
    hinh_thuc_hoat_dong_all = HinhThucHoatDong.objects.all()
    return render(
        request,
        "hod_template/manage_hinh_thuc_hoat_dong.html",
        {"hinh_thuc_hoat_dong_all": hinh_thuc_hoat_dong_all},
    )

def edit_hinh_thuc_hoat_dong(request, id_hinh_thuc_hoat_dong):
    hinh_thuc_hoat_dong = HinhThucHoatDong.objects.get(id=id_hinh_thuc_hoat_dong)
    return render(
        request,
        "hod_template/edit_hinh_thuc_hoat_dong.html",
        {"hinh_thuc_hoat_dong": hinh_thuc_hoat_dong},
    )

def edit_hinh_thuc_hoat_dong_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            id_hinh_thuc_hoat_dong = request.POST.get("id_hinh_thuc_hoat_dong")
            ten_hinh_thuc_hoat_dong = request.POST.get("hinh_thuc_hoat_dong")
            hinh_thuc_hoat_dong = HinhThucHoatDong.objects.get(id=id_hinh_thuc_hoat_dong)
            hinh_thuc_hoat_dong.ten_hinh_thuc_hoat_dong = ten_hinh_thuc_hoat_dong
            hinh_thuc_hoat_dong.save()
            messages.success(request, "Successfully update hinh thuc hoat dong")
            return HttpResponseRedirect(
                reverse(
                    "edit_hinh_thuc_hoat_dong", kwargs={"id_hinh_thuc_hoat_dong": id_hinh_thuc_hoat_dong}
                )
            )
        except:
            messages.error(request, "Failed Update hinh thuc hoat dong")
            return HttpResponseRedirect(
                reverse(
                    "edit_hinh_thuc_hoat_dong", kwargs={"id_hinh_thuc_hoat_dong": id_hinh_thuc_hoat_dong}
                )
            )

# Stop
def add_loai_dong_vat_quy(request):
    return render(
        request,"hod_template/add_loai_dong_vat_quy.html"
    )
def add_loai_dong_vat_quy_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            ten_loai_dong_vat_quy = request.POST.get("loai_dong_vat_quy")
            loai_dong_vat_quy = LoaiDongVatQuy(
                ten_loai_dong_vat_quy=ten_loai_dong_vat_quy
            )
            loai_dong_vat_quy.save()
            messages.success(request, "Successfully Create loai dong vat quy")
            return HttpResponseRedirect(reverse("add_loai_dong_vat_quy"))
        except:
            messages.error(request, "Failed Create loai dong vat quy")
            return HttpResponseRedirect(reverse("add_loai_dong_vat_quy"))

def manage_loai_dong_vat_quy(request):
    loai_dong_vat_quy_all = LoaiDongVatQuy.objects.all()
    return render(
        request,
        "hod_template/manage_loai_dong_vat_quy.html",
        {"loai_dong_vat_quy_all": loai_dong_vat_quy_all},
    )

def edit_loai_dong_vat_quy(request, id_dong_vat):
    loai_dong_vat_quy = LoaiDongVatQuy.objects.get(id=id_dong_vat)
    return render(
        request,
        "hod_template/edit_loai_dong_vat_quy.html",
        {"loai_dong_vat_quy": loai_dong_vat_quy},
    )

def edit_loai_dong_vat_quy_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            id_dong_vat = request.POST.get("id_dong_vat")
            ten_loai_dong_vat_quy = request.POST.get("ten_loai_dong_vat_quy")
            loai_dong_vat_quy = LoaiDongVatQuy.objects.get(id=id_dong_vat)
            loai_dong_vat_quy.ten_loai_dong_vat_quy = ten_loai_dong_vat_quy
            loai_dong_vat_quy.save()
            messages.success(request, "Successfully update ten_loai_dong_vat_quy")
            return HttpResponseRedirect(
                reverse(
                    "edit_loai_dong_vat_quy", kwargs={"id_dong_vat": id_dong_vat}
                )
            )
        except:
            messages.error(request, "Failed Update loai_dong_vat_quy")
            return HttpResponseRedirect(
                reverse(
                    "edit_loai_dong_vat_quy", kwargs={"id_dong_vat": id_dong_vat}
                )
            )

# Stop
def add_co_so_luu_tru_dong_vat(request):
    return render(
        request,"hod_template/add_co_so_luu_tru_dong_vat.html"
    )
def add_co_so_luu_tru_dong_vat_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            ten_co_so = request.POST.get("ten_co_so")
            dia_chi = request.POST.get("ten_dia_chi")
            co_so_luu_tru = CoSoLuuTruDongVat(
                ten_co_so=ten_co_so,dia_chi = dia_chi
            )
            co_so_luu_tru.save()
            messages.success(request, "Successfully Create co so luu tru dong vat")
            return HttpResponseRedirect(reverse("add_co_so_luu_tru_dong_vat"))
        except:
            messages.error(request, "Failed Create co so luu tru dong vat")
            return HttpResponseRedirect(reverse("add_co_so_luu_tru_dong_vat"))

def manage_co_so_luu_tru_dong_vat(request):
    co_so_luu_tru_dong_vat_all = CoSoLuuTruDongVat.objects.all()
    return render(
        request,
        "hod_template/manage_co_so_luu_tru_dong_vat.html",
        {"co_so_luu_tru_dong_vat_all": co_so_luu_tru_dong_vat_all},
    )

def edit_co_so_luu_tru_dong_vat(request, id_co_so):
    co_so_luu_tru_dong_vat = CoSoLuuTruDongVat.objects.get(id=id_co_so)
    return render(
        request,
        "hod_template/edit_co_so_luu_tru_dong_vat.html",
        {"co_so_luu_tru_dong_vat": co_so_luu_tru_dong_vat},
    )

def edit_co_so_luu_tru_dong_vat_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            id_co_so = request.POST.get("id_co_so")
            ten_co_so = request.POST.get("ten_co_so")
            dia_chi = request.POST.get("dia_chi")
            co_so_luu_tru_dong_vat = CoSoLuuTruDongVat.objects.get(id=id_co_so)
            co_so_luu_tru_dong_vat.ten_co_so = ten_co_so
            co_so_luu_tru_dong_vat.dia_chi = dia_chi
            co_so_luu_tru_dong_vat.save()
            messages.success(request, "Successfully update co so luu tru dong vat")
            return HttpResponseRedirect(
                reverse(
                    "edit_co_so_luu_tru_dong_vat", kwargs={"id_co_so": id_co_so}
                )
            )
        except:
            messages.error(request, "Failed Update cco so luu tru dong vat")
            return HttpResponseRedirect(
                reverse(
                    "edit_co_so_luu_tru_dong_vat", kwargs={"id_co_so": id_co_so}
                )
            )

# Stop
        
def add_loai_bien_dong(request):
    return render(
        request,"hod_template/add_loai_bien_dong.html"
    )
def add_loai_bien_dong_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            ten_loai_bien_dong = request.POST.get("loai_bien_dong")
            loai_bien_dong = LoaiBienDong(
                ten_loai_bien_doi = ten_loai_bien_dong
            )
            loai_bien_dong.save()
            messages.success(request, "Successfully Create loai bien dong")
            return HttpResponseRedirect(reverse("add_loai_bien_dong"))
        except:
            messages.error(request, "Failed Create loai bien dong")
            return HttpResponseRedirect(reverse("add_loai_bien_dong"))
def manage_loai_bien_dong(request):
    loai_bien_dong_all = LoaiBienDong.objects.all()
    return render(
        request,
        "hod_template/manage_loai_bien_dong.html",
        {"loai_bien_dong_all": loai_bien_dong_all},
    )

def edit_loai_bien_dong(request, id_loai_bien_dong):
    loai_bien_dong = LoaiBienDong.objects.get(id=id_loai_bien_dong)
    return render(
        request,
        "hod_template/edit_loai_bien_dong.html",
        {"loai_bien_dong": loai_bien_dong},
    )

def edit_loai_bien_dong_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        
        try:
            id_loai_bien_dong = request.POST.get("id_loai_bien_dong")
            ten_loai_bien_doi = request.POST.get("ten_loai_bien_doi")
            loai_bien_dong = LoaiBienDong.objects.get(id=id_loai_bien_dong)
            loai_bien_dong.ten_loai_bien_doi = ten_loai_bien_doi
            loai_bien_dong.save()
            messages.success(request, "Successfully update loai_bien_dong")
            return HttpResponseRedirect(
                reverse(
                    "edit_loai_bien_dong", kwargs={"id_loai_bien_dong": id_loai_bien_dong}
                )
            )
        except:
            messages.error(request, "Failed Update loai_bien_dong")
            return HttpResponseRedirect(
                reverse(
                    "edit_loai_bien_dong", kwargs={"id_loai_bien_dong": id_loai_bien_dong}
                )
            )

@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


# def staff_feedback_message(request):
#     feedbacks=FeedBackStaffs.objects.all()
#     return render(request,"hod_template/staff_feedback_template.html",{"feedbacks":feedbacks})

# def student_feedback_message(request):
#     feedbacks=FeedBackStudent.objects.all()
#     return render(request,"hod_template/student_feedback_template.html",{"feedbacks":feedbacks})

# @csrf_exempt
# def student_feedback_message_replied(request):
#     feedback_id=request.POST.get("id")
#     feedback_message=request.POST.get("message")

#     try:
#         feedback=FeedBackStudent.objects.get(id=feedback_id)
#         feedback.feedback_reply=feedback_message
#         feedback.save()
#         return HttpResponse("True")
#     except:
#         return HttpResponse("False")

# @csrf_exempt
# def staff_feedback_message_replied(request):
#     feedback_id=request.POST.get("id")
#     feedback_message=request.POST.get("message")

#     try:
#         feedback=FeedBackStaffs.objects.get(id=feedback_id)
#         feedback.feedback_reply=feedback_message
#         feedback.save()
#         return HttpResponse("True")
#     except:
#         return HttpResponse("False")

# def staff_leave_view(request):
#     leaves=LeaveReportStaff.objects.all()
#     return render(request,"hod_template/staff_leave_view.html",{"leaves":leaves})

# def student_leave_view(request):
#     leaves=LeaveReportStudent.objects.all()
#     return render(request,"hod_template/student_leave_view.html",{"leaves":leaves})

# def student_approve_leave(request,leave_id):
#     leave=LeaveReportStudent.objects.get(id=leave_id)
#     leave.leave_status=1
#     leave.save()
#     return HttpResponseRedirect(reverse("student_leave_view"))

# def student_disapprove_leave(request,leave_id):
#     leave=LeaveReportStudent.objects.get(id=leave_id)
#     leave.leave_status=2
#     leave.save()
#     return HttpResponseRedirect(reverse("student_leave_view"))


# def staff_approve_leave(request,leave_id):
#     leave=LeaveReportStaff.objects.get(id=leave_id)
#     leave.leave_status=1
#     leave.save()
#     return HttpResponseRedirect(reverse("staff_leave_view"))

# def staff_disapprove_leave(request,leave_id):
#     leave=LeaveReportStaff.objects.get(id=leave_id)
#     leave.leave_status=2
#     leave.save()
#     return HttpResponseRedirect(reverse("staff_leave_view"))

# def admin_view_attendance(request):
#     subjects=Subjects.objects.all()
#     session_year_id=SessionYearModel.object.all()
#     return render(request,"hod_template/admin_view_attendance.html",{"subjects":subjects,"session_year_id":session_year_id})

# @csrf_exempt
# def admin_get_attendance_dates(request):
#     subject=request.POST.get("subject")
#     session_year_id=request.POST.get("session_year_id")
#     subject_obj=Subjects.objects.get(id=subject)
#     session_year_obj=SessionYearModel.object.get(id=session_year_id)
#     attendance=Attendance.objects.filter(subject_id=subject_obj,session_year_id=session_year_obj)
#     attendance_obj=[]
#     for attendance_single in attendance:
#         data={"id":attendance_single.id,"attendance_date":str(attendance_single.attendance_date),"session_year_id":attendance_single.session_year_id.id}
#         attendance_obj.append(data)

#     return JsonResponse(json.dumps(attendance_obj),safe=False)


# @csrf_exempt
# def admin_get_attendance_student(request):
#     attendance_date=request.POST.get("attendance_date")
#     attendance=Attendance.objects.get(id=attendance_date)

#     attendance_data=AttendanceReport.objects.filter(attendance_id=attendance)
#     list_data=[]

#     for student in attendance_data:
#         data_small={"id":student.student_id.admin.id,"name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name,"status":student.status}
#         list_data.append(data_small)
#     return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)


def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, "hod_template/admin_profile.html", {"user": user})


def admin_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("admin_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            # if password!=None and password!="":
            #     customuser.set_password(password)
            customuser.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("admin_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("admin_profile"))

# def admin_send_notification_student(request):
#     students=Students.objects.all()
#     return render(request,"hod_template/student_notification.html",{"students":students})

# def admin_send_notification_staff(request):
#     staffs=Staffs.objects.all()
#     return render(request,"hod_template/staff_notification.html",{"staffs":staffs})

# @csrf_exempt
# def send_student_notification(request):
#     id=request.POST.get("id")
#     message=request.POST.get("message")
#     student=Students.objects.get(admin=id)
#     token=student.fcm_token
#     url="https://fcm.googleapis.com/fcm/send"
#     body={
#         "notification":{
#             "title":"Student Management System",
#             "body":message,
#             "click_action": "https://studentmanagementsystem22.herokuapp.com/student_all_notification",
#             "icon": "http://studentmanagementsystem22.herokuapp.com/static/dist/img/user2-160x160.jpg"
#         },
#         "to":token
#     }
#     headers={"Content-Type":"application/json","Authorization":"key=SERVER_KEY_HERE"}
#     data=requests.post(url,data=json.dumps(body),headers=headers)
#     notification=NotificationStudent(student_id=student,message=message)
#     notification.save()
#     print(data.text)
#     return HttpResponse("True")

# @csrf_exempt
# def send_staff_notification(request):
#     id=request.POST.get("id")
#     message=request.POST.get("message")
#     staff=Staffs.objects.get(admin=id)
#     token=staff.fcm_token
#     url="https://fcm.googleapis.com/fcm/send"
#     body={
#         "notification":{
#             "title":"Student Management System",
#             "body":message,
#             "click_action":"https://studentmanagementsystem22.herokuapp.com/staff_all_notification",
#             "icon":"http://studentmanagementsystem22.herokuapp.com/static/dist/img/user2-160x160.jpg"
#         },
#         "to":token
#     }
#     headers={"Content-Type":"application/json","Authorization":"key=SERVER_KEY_HERE"}
#     data=requests.post(url,data=json.dumps(body),headers=headers)
#     notification=NotificationStaffs(staff_id=staff,message=message)
#     notification.save()
#     print(data.text)
#     return HttpResponse("True")
