from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

################################################################################
########## 1. Quan ly nguoi dung ###############################################


class CustomUser(AbstractUser):
    user_type_data = ((1, "AdminHOD"), (2, "CanBoNghiepVu"))
    user_type = models.CharField(
        default=1, choices=user_type_data, max_length=10
    )


class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Donvi(models.Model):
    id = models.AutoField(primary_key=True)
    ten_don_vi = models.TextField()
    vi_tri = models.TextField()
    objects = models.Manager()


class CanBoNghiepVu(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    don_vi = models.ForeignKey(Donvi, on_delete=models.CASCADE)
    chuc_vu = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    fcm_token = models.TextField(default="")
    objects = models.Manager()


########################################################################################## 2. Quan ly cay giong ################################################


class LoaiCayGiong(models.Model):
    id = models.AutoField(primary_key=True)
    ten_giong = models.TextField()
    Ngay_cap_phep = models.DateField()
    objects = models.Manager()


class CoSoSanXuatCayGiong(models.Model):
    id = models.AutoField(primary_key=True)
    ten_co_so = models.TextField()
    dia_diem = models.TextField()
    ngay_cap_phep = models.DateField()
    objects = models.Manager()


class CayGiong(models.Model):
    id = models.AutoField(primary_key=True)
    loai_cay_giong = models.ForeignKey(LoaiCayGiong, on_delete=models.CASCADE)
    co_so_san_xuat = models.ForeignKey(
        CoSoSanXuatCayGiong, on_delete=models.CASCADE
    )
    so_luong = models.IntegerField()
    Thoi_gian_cap_nhat = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


################################################################################
########## 3. Quan ly co so san xuat che bien go ###############################


class LoaiHinhSanXuat(models.Model):
    id = models.AutoField(primary_key=True)
    ten_loai_hinh_san_xuat = models.TextField()
    objects = models.Manager()


class HinhThucHoatDong(models.Model):
    id = models.AutoField(primary_key=True)
    ten_hinh_thuc_hoat_dong = models.TextField()
    objects = models.Manager()


class CoSoSanXuatCheBienGo(models.Model):
    id = models.AutoField(primary_key=True)
    ten_co_so  = models.TextField()
    loai_hinh_san_xuat = models.ForeignKey(
        LoaiHinhSanXuat, on_delete=models.CASCADE
    )
    loai_hinh_hoat_dong = models.ForeignKey(
        HinhThucHoatDong, on_delete=models.CASCADE
    )
    dia_diem = models.TextField()
    ngay_thanh_lap = models.DateField()
    objects = models.Manager()


################################################################################
########## 4. Quan ly tai nguyen quy hiem ######################################


class LoaiDongVatQuy(models.Model):
    id = models.AutoField(primary_key=True)
    ten_loai_dong_vat_quy = models.TextField()
    objects = models.Manager()


class CoSoLuuTruDongVat(models.Model):
    id = models.AutoField(primary_key=True)
    ten_co_so = models.TextField()
    dia_chi = models.TextField()
    objects = models.Manager()


class LoaiBienDong(models.Model):
    id = models.AutoField(primary_key=True)
    ten_loai_bien_doi = models.TextField()
    objects = models.Manager()


class DongVatQuy(models.Model):
    id = models.AutoField(primary_key=True)
    loai_dong_vat_quy = models.ForeignKey(
        LoaiDongVatQuy, on_delete=models.CASCADE
    )
    co_so_luu_tru = models.ForeignKey(
        CoSoLuuTruDongVat, on_delete=models.CASCADE
    )
    loai_bien_dong = models.ForeignKey(LoaiBienDong, on_delete=models.CASCADE)
    so_luong = models.IntegerField()
    ngay_cap_nhat = models.DateField(auto_now_add=True)
    objects = models.Manager()


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            CanBoNghiepVu.objects.create(
                admin=instance, chuc_vu="", don_vi=Donvi.objects.get(id=1)
            )


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.canbonghiepvu.save()
