from django.shortcuts import render
from .models import Student
 
def student_list(request):
    students = Student.objects.all()
    return render(request,
                  "students/list.html",
                  {
                      "students": students,
                      },
                  )

# here's the logic 
# urls -> router
# views ->  logic, call api, redirect which html to display, data to html
def student_detail(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)

    enrollments = (Enrollment.objects
                   .filter(student=student)
                   .select_related("class_record")
                   )