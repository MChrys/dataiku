from django.db import models
class Task(models.Model):
    '''
    All task that could be apply to a specific account
    '''
    name = models.CharField(max_length=60, null=True, blank=True, primary_key=True)
    description = models.CharField(max_length=510, null=True, blank=True)


class Operation(models.Model):
    '''
    A running Task
    '''
    STATUS = (
        ('pending', 'pending'),
        ('running', 'running'),
        ('done', 'done')
    )
    account = models.ForeignKey(Dataiku_account, on_delete=models.CASCADE)
    date =
    statut = models.CharField(max_length=255, null=True, blank=True, choices = STATUS)

class Dataiku_account(models.Model):
    STATUS = (
        ('in operation', 'in operation')
        ('avaible', 'avaible')
    )
    email = models.CharField(max_length=60, null=True, blank=True, primary_key=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    task = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True, choices = STATUS)

    def __str__(self):
        return self.email

class QCM(models.Model):
    LearningPathUrl  = models.CharField(max_length=255, null=True, blank=True)
    LearningPathName = models.CharField(max_length=255, null=True, blank=True)
    CourseUrl = models.CharField(max_length=255, null=True, blank=True)
    CourseName = models.CharField(max_length=255, null=True, blank=True)
    QcmUrl = models.CharField(max_length=255, null=True, blank=True)
    QcmName =  models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return "{}_{}_{}".format(self.LearningPathName, self.CourseName,self.QcmName) 
    


# Create your models here.
class Question(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('check', 'check')
    )
    CHOICES_TYPE = (

        ('checkbox', 'checkbox'),
        ('radio', 'radio')
    )
    certification = models.ForeignKey(QCM)
    text = models.CharField(max_length=255, null=True, blank=True, primary_key=True)
    session = models.models.ForeignKey(session)
    status = models.CharField(max_length=255, null=True, blank=True, choices = STATUS)
    choice_type = models.CharField(max_length=255, null=True,, blank=True, default= "radio" ,choices = CHOICES_TYPE)
    cursor = models.IntegerField(default = 1)
    qcm = models.ForeignKey(QCM, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Posibility(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=True, blank=True)
    rank = models.models.ForeignKey(Answer)

    def __str__(self):
        return self.text
    

class Answer(models.Model):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )

    choice = models.IntegerField(max_length=10, null=True, default= 1, blank=True, choices = CHOICES)
    run = models.ForeignKey(Run)

class Run(models.Model):
    STATUS = (
        (True, 'True'),
        (False, 'False')
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    status = models.BooleanField(default = False)
    
class Session(models.Model):
    STATUS = (
        ('running','running'),
        ('finish','finish')
    )
    email = models.ForeignKey(Dataiku_account , on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    countdown = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    score = models.IntegerField(default=0)
    lenght = models.IntegerField(default=0)


