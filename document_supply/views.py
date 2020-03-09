from django.shortcuts import render, redirect, get_object_or_404
from .models import Apply_user
# Create your views here.
def propose_before (request) :
    return render(request, "document_supply/apply.html")

def propose_data(request) :
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    grade_num = request.POST.get('grade_num')

    motivation = request.POST.get('motivation')
    solution = request.POST.get('solution')
    webservice = request.POST.get('webservice')
    getting = request.POST.get("getting")

    userdata = Apply_user (
        name = name,
        phone = phone,
        major = major,
        grade = grade,
        grade_num = grade_num,
        motivation = motivation,
        solution = solution,
        webservice = webservice,
        getting = getting
    )

    userdata.save()

    request.session["submit_apply"] = "apply"

    return redirect("home")

def support(request) :
    return render(request, 'document_supply/support.html')

def apply_check_all(request) :
    if request.session.get('manager') :
        applies = Apply_user.objects.all()
        context = {'applies' : applies}

        return render(request, "document_supply/apply_check.html", context)
    else :
        return redirect("home")

def apply_check_one(request, pk) :
    apply = get_object_or_404(Apply_user, pk=pk)
    context = {"apply" : apply}
    return render(request, "document_supply/apply_check_more.html", context)