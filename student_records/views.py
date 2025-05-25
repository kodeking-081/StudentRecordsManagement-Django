from django.http import HttpResponseRedirect
from django.shortcuts import render

from student_records.models import Student

# Create your views here.

def student_list(request):
    students= Student.objects.all()
    return render(
        request,
        "student_list.html",
        {"students":students},
    )

def delete_record(request,id):
    record=Student.objects.get(id=id)
    record.delete()
    return HttpResponseRedirect("/")

def add_record(request):
    if request.method == "GET":
        return render(request,"add_record.html")
    else:
        Student.objects.create(
            student_id=request.POST["student_id"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            date_of_Birth=request.POST["date_of_Birth"],
            address=request.POST["address"],
            phone=request.POST["phone"]
            )
        return HttpResponseRedirect("/")
    
def update_details(request,id):
    if request.method == "GET":
        student=Student.objects.get(id=id)
        return render(
            request,
            "update_details.html",
            {"student":student}
        )
    else:
        student=Student.objects.get(id=id)
        student.student_id=request.POST["student_id"]
        student.first_name=request.POST["first_name"]
        student.last_name=request.POST["last_name"]
        student.email=request.POST["email"]
        dob = request.POST.get("date_of_Birth")
        if dob:
            student.date_of_Birth = dob  # only update if a new date is given
        student.address=request.POST["address"]
        student.phone=request.POST["phone"]
        student.save()
        return HttpResponseRedirect("/")


    
def show_record(request,id):
    student=Student.objects.get(id=id)
    return render(request,"view_details.html",{"Student":student})
