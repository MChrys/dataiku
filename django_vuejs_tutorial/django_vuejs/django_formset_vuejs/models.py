from django.db import models


class AuthorContainer(models.Model):
    created_on = models.DateField(auto_now=True, null=True)


class Author(models.Model):
    author_container = models.ForeignKey(AuthorContainer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    isbn = models.CharField(max_length=255, null=True, blank=True)

class QQM(models.Model):
    LearningPathUrl  = models.CharField(max_length=255, null=True, blank=True)
    LearningPathName = models.CharField(max_length=255, null=True, blank=True)
    CourseUrl = models.CharField(max_length=255, null=True, blank=True)
    CourseName = models.CharField(max_length=255, null=True, blank=True)
    QcmUrl = models.CharField(max_length=255, null=True, blank=True)
    QcmName =  models.CharField(max_length=255, null=True, blank=True)
    Lenght  = models.IntegerField(default =0)
    Verif = models.IntegerField(default =0)
    def __str__(self):
        return "{}_{}_{}".format(self.LearningPathName, self.CourseName,self.QcmName) 