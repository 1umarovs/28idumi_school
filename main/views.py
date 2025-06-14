from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import News ,Comments,Images,Teachers,ACCEPTANCE,Achievements,Boss,Teachers_situation
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

def Home(request):
    # Fetching teachers and news
    teachers = Teachers.objects.all()
    news = News.objects.all().order_by('-id')
    direktor = Boss.objects.all()
    achive = Achievements.objects.all()[0:3]
    context = {
        'News': news,
        'teachers': teachers,
        'direktor': direktor,
        'achives': achive,
    }
    return render(request, 'index.html', context)

@login_required  # Agar foydalanuvchi tizimga kirmagan bo'lsa, login sahifasiga yo'naltiriladi
def News_detail(request, slug):
    detail = News.objects.get(slug=slug)
    comment = Comments.objects.filter(new=detail)
    other_new = News.objects.exclude(id=detail.id).order_by('-id')
    other_images = Images.objects.filter(new=detail)
    count = comment.count()

    if request.method == 'POST':  # Form POST bo'lsa
        message = request.POST.get('message')
        if message:
            # Sharhni foydalanuvchi bilan saqlaymiz
            Comments.objects.create(new=detail, name=request.user, message=message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context = {
        'object': detail,
        'comments': comment,
        'c_count': count,
        'other_post': other_new,
        'other_img': other_images,
    }

    return render(request, 'single-blog.html', context)


def Achivments(request):
    achive = Achievements.objects.all()
    paginator = Paginator(achive, 5)  # Show 3 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'achivments.html', {'achives': page_obj})

def AchivmentsDetail(request, slug):
    detail = Achievements.objects.get(slug=slug)
    return render(request, 'achivments-detail.html', {'object': detail})


def TeachersDetail(request, slug):
    detail = Teachers.objects.get(slug=slug)
    other_image = Teachers_situation.objects.filter(teacher=detail)
    return render(request, 'teachers.html', {'teacher': detail, 'other_img': other_image})


def NewsPage(request):
    new = News.objects.all().order_by('-id')
    paginator = Paginator(new, 5)  # Show 3 news items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog.html', {'news': page_obj})

def About(request):
    teachers = Teachers.objects.all()
    return render(request,'about.html',{'teachers':teachers})

def Elements(request):
    return render(request, 'elements.html')

# def searchbar(request):
#     q = request.GET.get('search')
#     if len(q) >= 2:
#         query = News.objects.filter(title__icontains = q)
#         context = {'other_post':query}
#     return render(request , 'blog.html' ,context)

def Courses(request):
    return render(request,'courses.html')

def Contact(request):
    if request.method == 'POST':
        student_name = request.POST.get('studentName')
        student_number = request.POST.get('studentNumber')
        student_image = request.FILES.get('studentImage')

        # Check if the student with the same name, phone number, and image already exists
        if ACCEPTANCE.objects.filter(name=student_name, phone_number=student_number, image=student_image).exists():
            messages.error(request, 'Bu foydalanuvchi allaqachon qabul qilingan')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        # Validate that all fields are present
        elif student_name and student_number and student_image:
            ACCEPTANCE.objects.create(
                name=student_name,
                phone_number=student_number,
                image=student_image,
            )
            messages.success(request, 'Siz qabul qilindingiz va biz sizga murojatga chiqamiz')
        else:
            messages.error(request, 'Xatolik yuz berdi')

        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    return render(request,'contact.html') 