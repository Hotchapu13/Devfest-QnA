from django.contrib import admin
from .models import User, Session, Question, Answer, SpeakerSession

admin.site.register([User, Session, Question, Answer, SpeakerSession])

