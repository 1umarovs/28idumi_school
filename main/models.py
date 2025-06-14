from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='images/News/')
    description = models.TextField()
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField()


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Comments(models.Model):
    new = models.ForeignKey(to=News, on_delete=models.CASCADE)
    name = models.ForeignKey(to=User, on_delete=models.CASCADE)  # Foydalanuvchi bilan bog'lash
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name.username
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Images(models.Model):
    new = models.ForeignKey(to=News,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/News/')

    def __str__(self) -> str:
        return self.new.title

    class Meta:
        verbose_name = 'news_Image'
        verbose_name_plural = 'news_Images'

class subjects(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'


class Teachers(models.Model):
    fullname = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/teahcers')
    bio = models.TextField()
    subjects = models.ManyToManyField(to=subjects)
    lessons = models.ImageField(upload_to='images/teacher_lesson' , blank=True, null=True)

    def __str__(self):
        return self.fullname
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Boss(models.Model):
    fullname = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/boss')
    bio = models.TextField()
    subjects = models.ManyToManyField(to=subjects)

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = 'Boss'
        verbose_name_plural = 'Bosses'

class Teachers_situation(models.Model):
    teacher = models.ForeignKey(to=Teachers, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/teachers_situation')

    def __str__(self) -> str:
        return self.teacher.fullname
    
    class Meta:
        verbose_name = 'Teacher_situation'
        verbose_name_plural = 'Teachers_situations'

class Achievements(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/achievement/certificate/')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    

class ACCEPTANCE(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/acceptance/')
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Acceptance'
        verbose_name_plural = 'Acceptances'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self.name
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("main:home", kwargs={"pk": self.pk})
    