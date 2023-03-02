from django.shortcuts import render, redirect
from project.models import Lecturer, Student, Lecture, Status,  Result
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.contrib import messages




# Create your views here.
def index(request):
    return render (request,'index.html')


def login(request):
    if request.method=='POST':
        studID=request.POST.get('login_id')
        studPass=request.POST.get('login_pass')
        
        try:
            # Check if the given ID and password are in the Student table
            student = Student.objects.get(studID=studID, studPass=studPass)
            # Redirect the student to the student_result page
            return HttpResponseRedirect(reverse('student_result') + f'?studID={student.studID}')
        except Student.DoesNotExist:
            pass
        
        try:
            # Check if the given ID and password are in the Lecturer table
            lecturer = Lecturer.objects.get(lectID=studID, lectPass=studPass)
           # Redirect the lecturer to the index page
            return HttpResponseRedirect('/finalpro')
        except Lecturer.DoesNotExist:
            pass
        
        # If neither the Student nor the Lecturer table contains the given ID and password,
        # return an error message to the user
        dict = {'error_message': 'Invalid ID or password'}
        return render(request, 'login.html', dict)
    else:
        # Get the studIC parameter from the query string, if it exists
        studIC = request.GET.get('studIC')
        # Add the studIC parameter to the template context
        context = {'data': {'studIC': studIC}}
        return render(request, 'login.html', context)


def save_signupStud(request):
    if request.method == "POST":
        studID = request.POST['studID']
        studName = request.POST['studName']
        studIC = request.POST['studIC']
        studPass = request.POST['studPass']
        current_class_name = request.POST['studClass']

        try:
            current_class = Lecture.objects.get(lecture=current_class_name)
        except Lecture.DoesNotExist:
            # Handle the case where the Lecture object with the given lecture name does not exist
            messages.error(request, f'Class {current_class_name} does not exist!')
            return redirect('login')

        if Student.objects.filter(studID=studID).exists():
            # Handle the case where the student ID already exists
            messages.error(request, 'Student ID already exists!')
        else:
            student = Student(studID=studID, studName=studName, studIC=studIC, studPass=studPass, current_class=current_class)
            student.save()
            messages.success(request, 'Successfully Registered!')

    return redirect('login')


def save_signupLect(request):
    allect=Lecturer.objects.all()
    if request.method == "POST":
        lectID = request.POST['lectID']
        lectName = request.POST['lectName']
        lectPass = request.POST['lectPass']

        lecturer = Lecturer(lectID=lectID, lectName=lectName, lectPass=lectPass)
        lecturer.save()

        dict={
            'allect': allect,
            'message': 'Registration Successful!'}

    return render(request, 'login.html', dict)


def keyin(request):
    allresult = Result.objects.all()
    if request.method == 'POST':
        k_id = request.POST['k_id'] #foreign
        k_program = request.POST['k_program']
        k_class = request.POST['k_class'] #foreign
        k_code = request.POST['k_code']
        k_desc = request.POST['k_desc']
        k_grade = request.POST['k_grade']
        k_credit = request.POST['k_credit']
        k_status = request.POST['k_status'] #foreign

        #get foreign key data from reference table
        f_id = get_object_or_404(Student, studID=k_id)
        f_class = get_object_or_404(Lecture, lecture=k_class)
        f_status = get_object_or_404(Status, result_status=k_status)

        #set default value
        k_program = "DIPLOMA IN COMPUTER SCIENCE"
        k_session = "SESSION 3 2022/2023"
        
        data = Result(r_id=f_id, r_prog=k_program, r_class=f_class, r_session=k_session, r_code=k_code, r_desc=k_desc, r_grade=k_grade, r_kredit=k_credit, r_status=f_status)
        data.save()
        
        dict = {'allresult': allresult,
               'message': "Data Saved"}

    else:
        allstudent = Student.objects.all()
        allecture = Lecture.objects.all()
        allstatus = Status.objects.all()
        dict = {'allresult': allresult, 'allstudent':allstudent, 'allecture': allecture, 'allstatus': allstatus}

    return render(request, 'keyin.html', dict)


def search_class(request):
    allecture = Lecture.objects.all()

    if request.method == 'GET':
        selected_class = request.GET.get('s_class')
        stud_id = request.GET.get('stud_id')  # get the studID from the URL parameter
        if stud_id:
            data = Result.objects.select_related('r_id').filter(r_class_id=selected_class, r_id=stud_id).values('r_class_id', 'r_id__studName', 'r_id_id').distinct()
        else:
            data = Result.objects.select_related('r_id').filter(r_class_id=selected_class).values('r_class_id', 'r_id__studName', 'r_id_id').distinct()
        numberResult = data.count()

        dict = {
            'data': data,
            'allecture': allecture,
            'lecture': selected_class,
            'num_result': numberResult
        }
    else:
        dict = {'allecture': allecture} 

    return render(request, "search_class.html", dict)


def update_result(request, r_id_id):
    if request.method == 'POST':
        k_id = request.POST.get('k_id')
        k_program = request.POST.get('k_program')
        k_class = request.POST.get('k_class')  # renamed from "k_status"
        k_session = request.POST.get('k_session')
        k_code = request.POST.get('k_code')
        k_desc = request.POST.get('k_desc')
        k_grade = request.POST.get('k_grade')
        k_credit = request.POST.get('k_credit')
        k_status = request.POST.get('k_status')  # renamed from "k_class"

        result = Result.objects.filter(r_id_id=r_id_id).first()
        result.r_id_id = k_id
        result.r_prog = k_program
        result.r_class_id = k_class
        result.r_session = k_session
        result.r_code = k_code
        result.r_desc = k_desc
        result.r_grade = k_grade
        result.r_kredit = k_credit
        
        # retrieve Status object corresponding to selected status
        status_obj = Status.objects.get(result_status=k_status)
        result.r_status = status_obj
        
        result.save()

        #get foreign key data from reference table
        f_class = Lecture.objects.get(lecture=k_class)
        f_status = status_obj

        dict = {'data': result, 'allecture': Lecture.objects.all(), 'allstatus': Status.objects.all(), 'message': message}
        return render(request, "update_result.html", dict)
    else:
        data = Result.objects.filter(r_id_id=r_id_id).first()
        allecture = Lecture.objects.all()
        allstatus = Status.objects.all()
        dict = {
            'data': data,
            'allecture': allecture,  # use existing variable
            'allstatus': allstatus,  # use existing variable
            'allcourse': Lecture.objects.all(),
            'f_class': data.r_class_id,
            'f_status': data.r_status,
            'message': "Result successfully updated."
        }
        return render(request, "update_result.html", dict)


def save_update_result(request, r_id_id):
    u_grade = request.POST['k_grade']
    u_credit = request.POST['k_credit']
    u_status = request.POST['k_status']
    u_id = request.POST['k_id']

    # retrieve Status object corresponding to selected status
    status_obj = Status.objects.get(result_status=u_status)

    data = Result.objects.filter(r_id_id=r_id_id).first()
    data.r_grade = u_grade
    data.r_kredit = u_credit
    data.r_status = status_obj # assign Status object to r_status field
    data.save()

    dict = {'data': data, 'allcourse': Lecture.objects.all(), 'message': "Result successfully updated."}

    return redirect('update_result', r_id_id=data.r_id_id)


def delete_result(request, r_id_id, r_code):
    result = Result.objects.filter(r_id_id=r_id_id, r_code=r_code).first()
    if result:
        studID = result.r_id.studID  # get the student ID before deleting the result
        result.delete()
    return HttpResponseRedirect(reverse('checking') + f'?studID={studID}')


def delete_student(request, r_id_id):
    student = Student.objects.get(studID=r_id_id)
    class_id = ""
    if student:
        try:
            result = Result.objects.get(r_id=student)
            class_id = result.r_class.lecture
            result.delete()
        except Result.DoesNotExist:
            pass
        student.delete()
    return HttpResponseRedirect(reverse("search_class") + f"?s_class={class_id}")


def checking(request):
    studID = request.GET.get('studID')

    try:
        student = Student.objects.get(studID=studID)
    except Student.DoesNotExist:
        # Handle the case where the student does not exist
        student = None

    results = Result.objects.filter(r_id=student)

    program = ''
    if results:
        program = results[0].r_prog

    dict={
        'results': results,
        'student': student,
        'program': program,
    }
    
    return render(request, 'checking.html', dict)


def student_result(request):
    studID = request.GET.get('studID')
    try:
        student = Student.objects.get(studID=studID)
    except Student.DoesNotExist:
        # Handle the case where the student does not exist
        student = None

    results = Result.objects.filter(r_id=student)

    program = ''
    
    if results:
        program = results[0].r_prog

    dict={
        'results': results,
        'student': student,
        'program': program,
    }

    return render(request, 'student_result.html', dict)


def add_class(request):
    allclass = Lecture.objects.all()
    dict = {'allclass': allclass}

    if request.method == 'POST':
        a_sem = request.POST.get('a_sem') # Use request.POST.get to avoid errors if the key doesn't exist
        a_class = request.POST.get('lecture') # Use the correct name of the input field
        if a_sem and a_class: # Check if both fields have values
            data = Lecture(lecture=a_class, semester=a_sem)
            data.save()
            dict['message'] = 'Data Saved'
        else:
            dict['message'] = 'Please fill in both fields'

    return render(request, 'add_class.html', dict)


def view_class(request):
    allclass = Lecture.objects.all()
    context = {'allclass': allclass}
    return render(request, 'view_class.html', context)


def delete_class(request, a_class):
    try:
        allclass = Lecture.objects.get(lecture=a_class)
        allclass.delete()
        return HttpResponseRedirect(reverse("view_class"))
    except Lecture.DoesNotExist:
        return HttpResponseRedirect(reverse("view_class") + "?error=invalid_request")


def update_class(request, lecture):
    lecture_obj = Lecture.objects.get(lecture=lecture)

    if request.method == 'POST':
        a_class = request.POST.get('lecture')
        a_sem = request.POST.get('a_sem')

        lecture_obj.lecture = a_class
        lecture_obj.semester = a_sem
        lecture_obj.save()

        message = "Class successfully updated."
        return redirect('save_update_class', lecture=lecture_obj.lecture)

    allsem = Lecture.objects.values('semester').distinct()
    data = {
        'allsem': allsem,
        'data': lecture_obj,
        'current_sem': lecture_obj.semester,
    }
    return render(request, "update_class.html", data)


def save_update_class(request, lecture):
    if request.method == 'POST':
        a_class = request.POST['lecture']
        a_sem = request.POST['a_sem']

        lecture_obj = Lecture.objects.get(lecture=lecture)
        lecture_obj.lecture = a_class
        lecture_obj.semester = a_sem
        lecture_obj.save()

        message = "Class successfully updated."

        dict = {
            'message': message,
            'data': lecture_obj,
        }

        return redirect('view_class')

    # retrieve the lecture object using the lecture parameter from the URL
    lecture_obj = Lecture.objects.get(lecture=lecture)

    dict = {
        'data': lecture_obj,
    }

    return render(request, "update_class.html", dict)


