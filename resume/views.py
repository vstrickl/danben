from django.shortcuts import render

from .models import PageStyle
from .models import NavMenu
from .models import SocialMediaItem
from .models import Summary
from .models import Experience
from .models import Achievement
from .models import SkillGroup

# Create your views here.
def resume(request):

    theme = PageStyle.objects.get(pk=1)
    summary = Summary.objects.get(pk=1)
    nav = NavMenu.objects.all()
    social = SocialMediaItem.objects.all()
    experience = Experience.objects.all()
    achievement = Achievement.objects.all()
    skills = SkillGroup.objects.all()

    context = {
        'f':theme, 
        'nav':nav,
        's':summary,
        'skills':skills,
        'social':social, 
        'experience':experience,
        'achievement':achievement,
        }
    
    return render(request, 'resume.html', context)