from django.shortcuts import render

from .models import PageStyle
from .models import NavMenu
from .models import SocialMediaItem
from .models import Summary
from .models import Experience
from .models import Membership
from .models import Education
from .models import Achievement
from .models import SkillGroup
from .models import Skill

from .forms import CsvUploadForm

from .csv_upload import handle_csv_upload

# Create your views here.
def resume(request):

    theme = PageStyle.objects.get(pk=1)
    summary = Summary.objects.get(pk=1)
    nav = NavMenu.objects.all()
    social = SocialMediaItem.objects.all()
    experience = Experience.objects.all()
    memberships = Membership.objects.all()
    education = Education.objects.all()
    skills = SkillGroup.objects.all()

    combined_achievements = []
    for ach in Achievement.objects.all():
        experiences = Experience.objects.filter(achievements=ach)
        combined_achievements.append({
            'achievement': ach,
            'experiences': experiences
        })

    context = {
        'f':theme, 
        'nav':nav,
        's':summary,
        'skills':skills,
        'social':social, 
        'experience':experience,
        'memberships':memberships,
        'education':education,
        'combined_achievements': combined_achievements,
        }
    
    return render(request, 'resume.html', context)

def upload_skills(request):
    header = "CSV Upload"
    sub_header = 'Use this form to upload a batch of Skills via CSV.'

    context = {
        'header':header,
        'sub_header':sub_header,
    }

    field_mapping = {'type': 0}

    return handle_csv_upload(
        request=request,
        model_class=Skill,
        success_url='resume',
        form_class=CsvUploadForm,
        field_mapping=field_mapping,
        template_name='upload.html',
        context=context
    )

def resume_export(request):

    theme = PageStyle.objects.get(pk=1)
    summary = Summary.objects.get(pk=1)
    nav = NavMenu.objects.all()
    social = SocialMediaItem.objects.all()
    experience = Experience.objects.all()
    memberships = Membership.objects.all()
    education = Education.objects.all()
    skills = SkillGroup.objects.all()

    combined_achievements = []
    for ach in Achievement.objects.all():
        experiences = Experience.objects.filter(achievements=ach)
        combined_achievements.append({
            'achievement': ach,
            'experiences': experiences
        })

    context = {
        'f':theme, 
        'nav':nav,
        's':summary,
        'skills':skills,
        'social':social, 
        'experience':experience,
        'memberships':memberships,
        'education':education,
        'combined_achievements': combined_achievements,
        }
    
    return render(request, 'resume_export.html', context)
