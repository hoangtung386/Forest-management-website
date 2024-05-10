import json

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from App.models import (
    CanBoNghiepVu,
    CayGiong,
    CoSoSanXuatCayGiong,
    CoSoSanXuatCheBienGo,
    CustomUser,
    HinhThucHoatDong,
    LoaiCayGiong,
    LoaiHinhSanXuat,
    LoaiDongVatQuy,
    CoSoLuuTruDongVat,
    LoaiBienDong,
    DongVatQuy
)


def staff_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    staff = CanBoNghiepVu.objects.get(admin=user)
    return render(
        request,
        "staff_template/staff_profile.html",
        {"user": user, "staff": staff},
    )


def staff_profile_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("staff_profile"))
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("staff_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("staff_profile"))


def add_cay_giong(request):
    loai_cay_giong_all = LoaiCayGiong.objects.all()
    cs_sx_cay_giong_all = CoSoSanXuatCayGiong.objects.all()
    return render(
        request,
        "staff_template/add_cay_giong.html",
        {
            "loai_cay_giong_all": loai_cay_giong_all,
            "cs_sx_cay_giong_all": cs_sx_cay_giong_all,
        },
    )


def add_cay_giong_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        loai_cay_giong_id = request.POST.get("loai_cay_giong")
        cssx_id = request.POST.get("cssx")
        soluong = int(request.POST.get("soluong"))
        try:
            loai_cay_giong = LoaiCayGiong.objects.get(id=loai_cay_giong_id)
            cssx = CoSoSanXuatCayGiong.objects.get(id=cssx_id)
            cay_giong = CayGiong(so_luong=soluong)
            cay_giong.loai_cay_giong = loai_cay_giong
            cay_giong.co_so_san_xuat = cssx
            cay_giong.save()
            messages.success(request, "Successfully create cay giong")
            return HttpResponseRedirect(reverse("add_cay_giong"))
        except:
            messages.error(request, "Failed to create cay giong")
            return HttpResponseRedirect(reverse("add_cay_giong"))


def manage_cay_giong(request):
    cay_giong_all = CayGiong.objects.all()
    return render(
        request,
        "staff_template/manage_cay_giong.html",
        {"cay_giong_all": cay_giong_all},
    )


def edit_cay_giong(request, cay_giong_id):
    cay_giong = CayGiong.objects.get(id=cay_giong_id)
    loai_cay_giong_all = LoaiCayGiong.objects.all()
    cs_sx_cay_giong_all = CoSoSanXuatCayGiong.objects.all()
    return render(
        request,
        "staff_template/edit_cay_giong.html",
        {
            "cay_giong": cay_giong,
            "loai_cay_giong_all": loai_cay_giong_all,
            "cs_sx_cay_giong_all": cs_sx_cay_giong_all,
        },
    )


def edit_cay_giong_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        loai_cay_giong_id = request.POST.get("loai_cay_giong")
        cssx_id = request.POST.get("cssx")
        soluong = int(request.POST.get("soluong"))
        cay_giong_id = request.POST.get("cay_giong_id")
        try:
            loai_cay_giong = LoaiCayGiong.objects.get(id=loai_cay_giong_id)
            cssx = CoSoSanXuatCayGiong.objects.get(id=cssx_id)
            cay_giong = CayGiong.objects.get(id=cay_giong_id)
            cay_giong.so_luong = soluong
            cay_giong.loai_cay_giong = loai_cay_giong
            cay_giong.co_so_san_xuat = cssx
            cay_giong.Thoi_gian_cap_nhat = timezone.now()
            cay_giong.save()
            messages.success(request, "Successfully update cay giong")
            return HttpResponseRedirect(
                reverse("edit_cay_giong", kwargs={"cay_giong_id": cay_giong_id})
            )
        except:
            messages.error(request, "Failed to update cay giong")
            return HttpResponseRedirect(
                reverse("edit_cay_giong", kwargs={"cay_giong_id": cay_giong_id})
            )

def add_cssx_che_bien_go(request):
    loai_hinh_sx_all = LoaiHinhSanXuat.objects.all()
    hinh_thuc_hd_all = HinhThucHoatDong.objects.all()
    return render(request, "staff_template/add_cssx_che_bien_go.html", {
        "loai_hinh_sx_all": loai_hinh_sx_all,
        "hinh_thuc_hd_all": hinh_thuc_hd_all
    })

def add_cssx_che_bien_go_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        
        try:
            ten_co_so = request.POST.get("ten_co_so")
            loai_hinh_sx_id = request.POST.get("loai_hinh_sx")
            hinh_thuc_hoat_dong_id = request.POST.get("hinh_thuc_hoat_dong")
            hinh_thuc_hoat_dong = HinhThucHoatDong.objects.get(id=hinh_thuc_hoat_dong_id)
            dia_diem = request.POST.get("diadiem")
            loai_hinh_sx_ = LoaiHinhSanXuat.objects.get(id=loai_hinh_sx_id)
            hinh_thuc_hoat_dong = HinhThucHoatDong.objects.get(id=hinh_thuc_hoat_dong_id)
            ngaythanhlap = request.POST.get("ngaythanhlap")
            cssx_che_bien_go = CoSoSanXuatCheBienGo()
            cssx_che_bien_go.ten_co_so = ten_co_so
            cssx_che_bien_go.loai_hinh_san_xuat = loai_hinh_sx_
            cssx_che_bien_go.loai_hinh_hoat_dong = hinh_thuc_hoat_dong
            cssx_che_bien_go.dia_diem = dia_diem
            cssx_che_bien_go.ngay_thanh_lap = ngaythanhlap
            cssx_che_bien_go.save()
            messages.success(request, "Successfully create CSSX che bien go")
            return HttpResponseRedirect(reverse("add_cssx_che_bien_go"))
        except:
            messages.error(request, "Failed to create  CSSX che bien go")
            return HttpResponseRedirect(reverse("add_cssx_che_bien_go"))
        
def manage_cssx_che_bien_go(request):
    cssx_che_bien_go_all = CoSoSanXuatCheBienGo.objects.all()
    return render(request, "staff_template/manage_cssx_che_bien_go.html", {
        "cssx_che_bien_go_all": cssx_che_bien_go_all
    })

def edit_cssx_che_bien_go(request, cssx_che_bien_go_id):
    cssx_che_bien_go = CoSoSanXuatCheBienGo.objects.get(id=cssx_che_bien_go_id)
    loai_hinh_sx_all = LoaiHinhSanXuat.objects.all()
    hinh_thuc_hd_all = HinhThucHoatDong.objects.all()
    return render(request, "staff_template/edit_cssx_che_bien_go.html", {
        "cssx_che_bien_go": cssx_che_bien_go,
        "loai_hinh_sx_all": loai_hinh_sx_all,
        "hinh_thuc_hd_all": hinh_thuc_hd_all
    })

def edit_cssx_che_bien_go_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        
        try:
            cssx_che_bien_go_id = request.POST.get("cssx_che_bien_go_id")
            ten_co_so = request.POST.get("ten_co_so")
            loai_hinh_sx_id = request.POST.get("loai_hinh_sx")
            hinh_thuc_hoat_dong_id = request.POST.get("hinh_thuc_hoat_dong")
            hinh_thuc_hoat_dong = HinhThucHoatDong.objects.get(id=hinh_thuc_hoat_dong_id)
            dia_diem = request.POST.get("diadiem")
            loai_hinh_sx_ = LoaiHinhSanXuat.objects.get(id=loai_hinh_sx_id)
            hinh_thuc_hoat_dong = HinhThucHoatDong.objects.get(id=hinh_thuc_hoat_dong_id)
            ngaythanhlap = request.POST.get("ngaythanhlap")
            cssx_che_bien_go = CoSoSanXuatCheBienGo.objects.get(id=cssx_che_bien_go_id)
            cssx_che_bien_go.ten_co_so = ten_co_so
            cssx_che_bien_go.loai_hinh_san_xuat = loai_hinh_sx_
            cssx_che_bien_go.loai_hinh_hoat_dong = hinh_thuc_hoat_dong
            cssx_che_bien_go.dia_diem = dia_diem
            cssx_che_bien_go.ngay_thanh_lap = ngaythanhlap
            cssx_che_bien_go.save()
            messages.success(request, "Successfully update CSSX che bien go")
            return HttpResponseRedirect(reverse("edit_cssx_che_bien_go", kwargs={"cssx_che_bien_go_id": cssx_che_bien_go_id}))
        except:
            messages.error(request, "Failed to update  CSSX che bien go")
            return HttpResponseRedirect(reverse("edit_cssx_che_bien_go", kwargs={"cssx_che_bien_go_id": cssx_che_bien_go_id}))

def add_dong_vat_quy(request):
    loai_dong_vat_quy_all = LoaiDongVatQuy.objects.all()
    co_so_luu_tru_dv_all = CoSoLuuTruDongVat.objects.all()
    loai_bien_dong_all = LoaiBienDong.objects.all()
    return render(request, "staff_template/add_dong_vat_quy.html", {
        "loai_dong_vat_quy_all": loai_dong_vat_quy_all,
        "co_so_luu_tru_dv_all": co_so_luu_tru_dv_all,
        "loai_bien_dong_all": loai_bien_dong_all
    })

def add_dong_vat_quy_save(request):
    if request.method != "POST":
            return HttpResponse("Method Not Allowed")
    else:
        try:
            loai_dong_vat_id = request.POST.get("loai_dong_vat")
            cs_luu_tru_id = request.POST.get("cs_luu_tru")
            loai_bien_dong_id = request.POST.get("loai_bien_dong_id")

            loai_dong_vat = LoaiDongVatQuy.objects.get(id=loai_dong_vat_id)

            cs_luu_tru = CoSoLuuTruDongVat.objects.get(id=cs_luu_tru_id)
            loai_bien_dong_ = LoaiBienDong.objects.get(id=loai_bien_dong_id)
            soluong = int(request.POST.get("soluong"))
            dong_vat_quy = DongVatQuy(so_luong=soluong)
            dong_vat_quy.loai_dong_vat_quy = loai_dong_vat
            dong_vat_quy.co_so_luu_tru = cs_luu_tru
            dong_vat_quy.loai_bien_dong = loai_bien_dong_
            dong_vat_quy.save()
            messages.success(request, "Successfully create dong vat quy")
            return HttpResponseRedirect(reverse("add_dong_vat_quy"))
        except:
            messages.error(request, "Failed to create  dong vat quy")
            return HttpResponseRedirect(reverse("add_dong_vat_quy"))

def manage_dong_vat_quy(request):
    dong_vat_quy_all = DongVatQuy.objects.all()
    return render(request, "staff_template/manage_dong_vat_quy.html", {
        "dong_vat_quy_all": dong_vat_quy_all
    })

def edit_dong_vat_quy(request, dong_vat_quy_id):
    dong_vat_quy = DongVatQuy.objects.get(id = dong_vat_quy_id)
    loai_dong_vat_quy_all = LoaiDongVatQuy.objects.all()
    co_so_luu_tru_dv_all = CoSoLuuTruDongVat.objects.all()
    loai_bien_dong_all = LoaiBienDong.objects.all()

    return render(request, "staff_template/edit_dong_vat_quy.html", {
        "dong_vat_quy": dong_vat_quy,
        "loai_dong_vat_quy_all": loai_dong_vat_quy_all,
        "co_so_luu_tru_dv_all": co_so_luu_tru_dv_all,
        "loai_bien_dong_all": loai_bien_dong_all
    })

def edit_dong_vat_quy_save(request):
    if request.method != "POST":
            return HttpResponse("Method Not Allowed")
    else:
        try:
            dong_vat_quy_ = request.POST.get("dong_vat_quy_id")
            loai_dong_vat_id = request.POST.get("loai_dong_vat")
            cs_luu_tru_id = request.POST.get("cs_luu_tru")
            loai_bien_dong_id = request.POST.get("loai_bien_dong")


            loai_dong_vat = LoaiDongVatQuy.objects.get(id=loai_dong_vat_id)
            cs_luu_tru = CoSoLuuTruDongVat.objects.get(id=cs_luu_tru_id)
            loai_bien_dong_ = LoaiBienDong.objects.get(id=loai_bien_dong_id)
            soluong = int(request.POST.get("soluong"))
            dong_vat_quy = DongVatQuy.objects.get(id = dong_vat_quy_ )
            
            dong_vat_quy.loai_dong_vat_quy = loai_dong_vat
            dong_vat_quy.co_so_luu_tru = cs_luu_tru
            dong_vat_quy.loai_bien_dong = loai_bien_dong_
            dong_vat_quy.so_luong = soluong
            dong_vat_quy.ngay_cap_nhat = timezone.now()
            dong_vat_quy.save()
            messages.success(request, "Successfully update dong vat quy")
            return HttpResponseRedirect(reverse("edit_dong_vat_quy", kwargs={"dong_vat_quy_id": dong_vat_quy_}))
        except:
            messages.error(request, "Failed to update  dong vat quy")
            return HttpResponseRedirect(reverse("edit_dong_vat_quy", kwargs={"dong_vat_quy_id": dong_vat_quy_}))



def staff_home(request):
    return render(
        request,
        "staff_template/staff_home_template.html",
    )
    # For Fetch All Student Under Staff


#     subjects = Subjects.objects.filter(staff_id=request.user.id)
#     course_id_list = []
#     for subject in subjects:
#         course = Class.objects.get(id=subject.course_id.id)
#         course_id_list.append(course.id)

#     final_course = []
#     # removing Duplicate Course ID
#     for course_id in course_id_list:
#         if course_id not in final_course:
#             final_course.append(course_id)

#     students_count = Students.objects.filter(course_id__in=final_course).count()

#     # Fetch All Attendance Count
#     attendance_count = Attendance.objects.filter(
#         subject_id__in=subjects
#     ).count()

#     # Fetch All Approve Leave
#     staff = Staffs.objects.get(admin=request.user.id)
#     leave_count = LeaveReportStaff.objects.filter(
#         staff_id=staff.id, leave_status=1
#     ).count()
#     subject_count = subjects.count()

#     # Fetch Attendance Data by Subject
#     subject_list = []
#     attendance_list = []
#     for subject in subjects:
#         attendance_count1 = Attendance.objects.filter(
#             subject_id=subject.id
#         ).count()
#         subject_list.append(subject.subject_name)
#         attendance_list.append(attendance_count1)

#     students_attendance = Students.objects.filter(course_id__in=final_course)
#     student_list = []
#     student_list_attendance_present = []
#     student_list_attendance_absent = []
#     for student in students_attendance:
#         attendance_present_count = AttendanceReport.objects.filter(
#             status=True, student_id=student.id
#         ).count()
#         attendance_absent_count = AttendanceReport.objects.filter(
#             status=False, student_id=student.id
#         ).count()
#         student_list.append(student.admin.username)
#         student_list_attendance_present.append(attendance_present_count)
#         student_list_attendance_absent.append(attendance_absent_count)

#     return render(
#         request,
#         "staff_template/staff_home_template.html",
#         {
#             "students_count": students_count,
#             "attendance_count": attendance_count,
#             "leave_count": leave_count,
#             "subject_count": subject_count,
#             "subject_list": subject_list,
#             "attendance_list": attendance_list,
#             "student_list": student_list,
#             "present_list": student_list_attendance_present,
#             "absent_list": student_list_attendance_absent,
#         },
#     )


# def staff_take_attendance(request):
#     subjects = Subjects.objects.filter(staff_id=request.user.id)
#     session_years = SessionYearModel.object.all()
#     return render(
#         request,
#         "staff_template/staff_take_attendance.html",
#         {"subjects": subjects, "session_years": session_years},
#     )


# @csrf_exempt
# def get_students(request):
#     subject_id = request.POST.get("subject")
#     session_year = request.POST.get("session_year")

#     subject = Subjects.objects.get(id=subject_id)
#     session_model = SessionYearModel.object.get(id=session_year)
#     students = Students.objects.filter(
#         course_id=subject.course_id, session_year_id=session_model
#     )
#     list_data = []

#     for student in students:
#         data_small = {
#             "id": student.admin.id,
#             "name": student.admin.first_name + " " + student.admin.last_name,
#         }
#         list_data.append(data_small)
#     return JsonResponse(
#         json.dumps(list_data), content_type="application/json", safe=False
#     )


# @csrf_exempt
# def save_attendance_data(request):
#     student_ids = request.POST.get("student_ids")
#     subject_id = request.POST.get("subject_id")
#     attendance_date = request.POST.get("attendance_date")
#     session_year_id = request.POST.get("session_year_id")

#     subject_model = Subjects.objects.get(id=subject_id)
#     session_model = SessionYearModel.object.get(id=session_year_id)
#     json_sstudent = json.loads(student_ids)
#     # print(data[0]['id'])

#     try:
#         attendance = Attendance(
#             subject_id=subject_model,
#             attendance_date=attendance_date,
#             session_year_id=session_model,
#         )
#         attendance.save()

#         for stud in json_sstudent:
#             student = Students.objects.get(admin=stud["id"])
#             attendance_report = AttendanceReport(
#                 student_id=student,
#                 attendance_id=attendance,
#                 status=stud["status"],
#             )
#             attendance_report.save()
#         return HttpResponse("OK")
#     except:
#         return HttpResponse("ERR")


# def staff_update_attendance(request):
#     subjects = Subjects.objects.filter(staff_id=request.user.id)
#     session_year_id = SessionYearModel.object.all()
#     return render(
#         request,
#         "staff_template/staff_update_attendance.html",
#         {"subjects": subjects, "session_year_id": session_year_id},
#     )


# @csrf_exempt
# def get_attendance_dates(request):
#     subject = request.POST.get("subject")
#     session_year_id = request.POST.get("session_year_id")
#     subject_obj = Subjects.objects.get(id=subject)
#     session_year_obj = SessionYearModel.object.get(id=session_year_id)
#     attendance = Attendance.objects.filter(
#         subject_id=subject_obj, session_year_id=session_year_obj
#     )
#     attendance_obj = []
#     for attendance_single in attendance:
#         data = {
#             "id": attendance_single.id,
#             "attendance_date": str(attendance_single.attendance_date),
#             "session_year_id": attendance_single.session_year_id.id,
#         }
#         attendance_obj.append(data)

#     return JsonResponse(json.dumps(attendance_obj), safe=False)


# @csrf_exempt
# def get_attendance_student(request):
#     attendance_date = request.POST.get("attendance_date")
#     attendance = Attendance.objects.get(id=attendance_date)

#     attendance_data = AttendanceReport.objects.filter(attendance_id=attendance)
#     list_data = []

#     for student in attendance_data:
#         data_small = {
#             "id": student.student_id.admin.id,
#             "name": student.student_id.admin.first_name
#             + " "
#             + student.student_id.admin.last_name,
#             "status": student.status,
#         }
#         list_data.append(data_small)
#     return JsonResponse(
#         json.dumps(list_data), content_type="application/json", safe=False
#     )


# @csrf_exempt
# def save_updateattendance_data(request):
#     student_ids = request.POST.get("student_ids")
#     attendance_date = request.POST.get("attendance_date")
#     attendance = Attendance.objects.get(id=attendance_date)

#     json_sstudent = json.loads(student_ids)

#     try:
#         for stud in json_sstudent:
#             student = Students.objects.get(admin=stud["id"])
#             attendance_report = AttendanceReport.objects.get(
#                 student_id=student, attendance_id=attendance
#             )
#             attendance_report.status = stud["status"]
#             attendance_report.save()
#         return HttpResponse("OK")
#     except:
#         return HttpResponse("ERR")


# def staff_apply_leave(request):
#     staff_obj = Staffs.objects.get(admin=request.user.id)
#     leave_data = LeaveReportStaff.objects.filter(staff_id=staff_obj)
#     return render(
#         request,
#         "staff_template/staff_apply_leave.html",
#         {"leave_data": leave_data},
#     )


# def staff_apply_leave_save(request):
#     if request.method != "POST":
#         return HttpResponseRedirect(reverse("staff_apply_leave"))
#     else:
#         leave_date = request.POST.get("leave_date")
#         leave_msg = request.POST.get("leave_msg")

#         staff_obj = Staffs.objects.get(admin=request.user.id)
#         try:
#             leave_report = LeaveReportStaff(
#                 staff_id=staff_obj,
#                 leave_date=leave_date,
#                 leave_message=leave_msg,
#                 leave_status=0,
#             )
#             leave_report.save()
#             messages.success(request, "Successfully Applied for Leave")
#             return HttpResponseRedirect(reverse("staff_apply_leave"))
#         except:
#             messages.error(request, "Failed To Apply for Leave")
#             return HttpResponseRedirect(reverse("staff_apply_leave"))


# def staff_feedback(request):
#     staff_id = Staffs.objects.get(admin=request.user.id)
#     feedback_data = FeedBackStaffs.objects.filter(staff_id=staff_id)
#     return render(
#         request,
#         "staff_template/staff_feedback.html",
#         {"feedback_data": feedback_data},
#     )


# def staff_feedback_save(request):
#     if request.method != "POST":
#         return HttpResponseRedirect(reverse("staff_feedback_save"))
#     else:
#         feedback_msg = request.POST.get("feedback_msg")

#         staff_obj = Staffs.objects.get(admin=request.user.id)
#         try:
#             feedback = FeedBackStaffs(
#                 staff_id=staff_obj, feedback=feedback_msg, feedback_reply=""
#             )
#             feedback.save()
#             messages.success(request, "Successfully Sent Feedback")
#             return HttpResponseRedirect(reverse("staff_feedback"))
#         except:
#             messages.error(request, "Failed To Send Feedback")
#             return HttpResponseRedirect(reverse("staff_feedback"))


# def staff_profile(request):
#     user = CustomUser.objects.get(id=request.user.id)
#     staff = Staffs.objects.get(admin=user)
#     return render(
#         request,
#         "staff_template/staff_profile.html",
#         {"user": user, "staff": staff},
#     )


# def staff_profile_save(request):
#     if request.method != "POST":
#         return HttpResponseRedirect(reverse("staff_profile"))
#     else:
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         address = request.POST.get("address")
#         password = request.POST.get("password")
#         try:
#             customuser = CustomUser.objects.get(id=request.user.id)
#             customuser.first_name = first_name
#             customuser.last_name = last_name
#             if password != None and password != "":
#                 customuser.set_password(password)
#             customuser.save()

#             staff = Staffs.objects.get(admin=customuser.id)
#             staff.address = address
#             staff.save()
#             messages.success(request, "Successfully Updated Profile")
#             return HttpResponseRedirect(reverse("staff_profile"))
#         except:
#             messages.error(request, "Failed to Update Profile")
#             return HttpResponseRedirect(reverse("staff_profile"))


# @csrf_exempt
# def staff_fcmtoken_save(request):
#     token = request.POST.get("token")
#     try:
#         staff = Staffs.objects.get(admin=request.user.id)
#         staff.fcm_token = token
#         staff.save()
#         return HttpResponse("True")
#     except:
#         return HttpResponse("False")


# def staff_all_notification(request):
#     staff = Staffs.objects.get(admin=request.user.id)
#     notifications = NotificationStaffs.objects.filter(staff_id=staff.id)
#     return render(
#         request,
#         "staff_template/all_notification.html",
#         {"notifications": notifications},
#     )


# def staff_add_result(request):
#     subjects = Subjects.objects.filter(staff_id=request.user.id)
#     session_years = SessionYearModel.object.all()
#     return render(
#         request,
#         "staff_template/staff_add_result.html",
#         {"subjects": subjects, "session_years": session_years},
#     )


# def save_student_result(request):
#     if request.method != "POST":
#         return HttpResponseRedirect("staff_add_result")
#     student_admin_id = request.POST.get("student_list")
#     assignment_marks = float(request.POST.get("assignment_marks"))
#     exam_marks = float(request.POST.get("exam_marks"))
#     subject_id = request.POST.get("subject")

#     student_obj = Students.objects.get(admin=student_admin_id)
#     subject_obj = Subjects.objects.get(id=subject_id)

#     try:
#         check_exist = StudentResult.objects.filter(
#             subject_id=subject_obj, student_id=student_obj
#         ).exists()
#         if check_exist is False:
#             result = StudentResult.objects.get(
#                 subject_id=subject_obj, student_id=student_obj
#             )
#             result.subject_assignment_marks = assignment_marks
#             result.subject_exam_marks = exam_marks
#             result.save()
#             messages.success(request, "Successfully Added Result")
#             return HttpResponseRedirect(reverse("staff_add_result"))
#         else:
#             messages.error(request, "Failed to Add Result")
#             return HttpResponseRedirect(reverse("staff_add_result"))
#     except:
#         messages.error(request, "Failed to Add Result")
#         return HttpResponseRedirect(reverse("staff_add_result"))


# def save_student_edit_result(request):
#     if request.method != "POST":
#         return HttpResponseRedirect("staff_add_result")
#     student_admin_id = request.POST.get("student_list")
#     assignment_marks = float(request.POST.get("assignment_marks"))
#     exam_marks = float(request.POST.get("exam_marks"))
#     subject_id = request.POST.get("subject")

#     student_obj = Students.objects.get(admin=student_admin_id)
#     subject_obj = Subjects.objects.get(id=subject_id)

#     try:
#         check_exist = StudentResult.objects.filter(
#             subject_id=subject_obj, student_id=student_obj
#         ).exists()
#         if check_exist:
#             result = StudentResult.objects.get(
#                 subject_id=subject_obj, student_id=student_obj
#             )
#             result.subject_assignment_marks = assignment_marks
#             result.subject_exam_marks = exam_marks
#             result.save()
#             messages.success(request, "Successfully Updated Result")
#             return HttpResponseRedirect(reverse("edit_student_result"))
#         else:
#             messages.error(request, "Failed to Updated Result")
#             return HttpResponseRedirect(reverse("edit_student_result"))
#     except:
#         messages.error(request, "Failed to Updated Result")
#         return HttpResponseRedirect(reverse("edit_student_result"))


# def staff_edit_result(request):
#     subjects = Subjects.objects.filter(staff_id=request.user.id)
#     session_years = SessionYearModel.object.all()
#     return render(
#         request,
#         "staff_template/edit_student_result.html",
#         {"subjects": subjects, "session_years": session_years},
#     )


# @csrf_exempt
# def fetch_result_student(request):
#     subject_id = request.POST.get("subject_id")
#     student_id = request.POST.get("student_id")
#     student_obj = Students.objects.get(admin=student_id)
#     result = StudentResult.objects.filter(
#         student_id=student_obj.id, subject_id=subject_id
#     ).exists()
#     if result:
#         result = StudentResult.objects.get(
#             student_id=student_obj.id, subject_id=subject_id
#         )
#         result_data = {
#             "exam_marks": result.subject_exam_marks,
#             "assign_marks": result.subject_assignment_marks,
#         }
#         return HttpResponse(json.dumps(result_data))
#     else:
#         return HttpResponse("False")


# def returnHtmlWidget(request):
#     return render(request, "widget.html")
