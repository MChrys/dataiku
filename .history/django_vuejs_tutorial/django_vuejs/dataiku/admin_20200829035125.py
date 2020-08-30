from django.contrib import admin

# Register your models here.
from .models import QCM, Answer, Task, Dataiku_account, Operation, Session, Question, Run, Posibility

admin.site.register(Task)
admin.site.register(Dataiku_account)
admin.site.register(Operation)
admin.site.register(Session)
admin.site.register(Question)
admin.site.register(Run)
admin.site.register(Posibility)
admin.site.register(QCM)
admin.site.register(Answer)
