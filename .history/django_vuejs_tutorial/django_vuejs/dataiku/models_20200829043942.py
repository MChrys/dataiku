from django.db import models
from django.utils import timezone
class Task(models.Model):
    '''
    All task that could be apply to a specific account
    '''
    name = models.CharField(max_length=60,  primary_key=True)
    description = models.CharField(max_length=510, null=True, blank=True)
    supertask = models.ForeignKey('self',null=True, blank=True, on_delete=models.SET_NULL)

class Dataiku_account(models.Model):
    STATUS = (
        ('in operation', 'in operation'),
        ('avaible', 'avaible')
    )
    email = models.CharField(max_length=60, primary_key=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    #task = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True, choices = STATUS)

    def __str__(self):
        return self.email

class Operation(models.Model):
    '''
    A running Task like : validate this course or take this QCM
    '''
    creation = models.DateTimeField( editable = False)
    STATUS = (
        ('pending', 'pending'),
        ('running', 'running'),
        ('done', 'done')
    )
    task = models.OneToOneField(Task, null=True, blank=True,on_delete=models.SET_NULL)
    account = models.ForeignKey(Dataiku_account,  on_delete=models.CASCADE)

    statut = models.CharField(max_length=255, null=True, blank=True, choices = STATUS)

    def save(self, *args, **kwargs):
        if not self.id:
            self.creation = timezone.now()

        return super(User, self).save(*args, **kwargs)



class QCM(models.Model):
    LearningPathUrl  = models.CharField(max_length=255, null=True, blank=True)
    LearningPathName = models.CharField(max_length=255, null=True, blank=True)
    CourseUrl = models.CharField(max_length=255, null=True, blank=True)
    CourseName = models.CharField(max_length=255, null=True, blank=True)
    QcmUrl = models.CharField(max_length=255, null=True, blank=True)
    QcmName =  models.CharField(max_length=255, null=True, blank=True)
    Lenght  = models.IntegerField(default =0)
    Verif = models.IntegerField(default =0)
    status = models.BooleanField(default = False)
    def __str__(self):
        return "{}_{}_{}".format(self.LearningPathName, self.CourseName,self.QcmName) 
    
class Session(models.Model):
    STATUS = (
        ('running','running'),
        ('finish','finish')
    )
    email = models.ForeignKey(Dataiku_account , on_delete=models.CASCADE)
    start = models.DateTimeField(editable =False)
    countdown =  models.CharField(max_length=10, blank=True, null=True, default= '59:59')
    score = models.IntegerField(default=0)
    lenght = models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.start = timezone.now()
        return super(User, self).save(*args, **kwargs)


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
    text = models.CharField(max_length=255, primary_key=True)
    #session = models.ForeignKey(Session, null=True, blank=True,on_delete = models.SET_NULL)
    status = models.CharField(max_length=255, null=True, blank=True, choices = STATUS)
    choice_type = models.CharField(max_length=255, null=True, blank=True, default= "radio" ,choices = CHOICES_TYPE)
    max_choices = models.IntegerField(default = 0)
    cursor = models.IntegerField(default = 1)
    # cursor  is the number of answer currently explored
    qcm = models.ForeignKey(QCM, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Run(models.Model):
    '''
    A Run is a try
    '''
    STATUS = (
        (True, 'True'),
        (False, 'False')
    )

    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    status = models.BooleanField(default = False)
    #creation = models.DateTimeField(editable =False)


    '''def save(self, *args, **kwargs):
        if not self.id:
            self.creation = timezone.now()

        return super(User, self).save(*args, **kwargs)'''



class Posibility(models.Model):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )
    rank = models.IntegerField( null=True, default= 1, blank=True, choices = CHOICES)
    question = models.ForeignKey(Question, null=True, blank=True,on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=True, blank=True)
    #rank = models.ForeignKey(Answer, null=True, blank=True,on_delete= models.SET_NULL)

    def __str__(self):
        return self.text

class Answer(models.Model):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )

    #choice = models.IntegerField( null=True, default= 1, blank=True, choices = CHOICES)
    posibility  = models.ForeignKey(Posibility,blank=True,null=True,on_delete= models.SET_NULL)
    run = models.ForeignKey(Run,unique = False,blank=True,null=True,on_delete= models.SET_NULL)


    


    


