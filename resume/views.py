import os
import base64
import cloudinary.uploader

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

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

def download_resume_pdf(request):
    # Set up Seleniu with headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")

    # Ensure the path to chromedriver is set in your system's PATH
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Replace with the URL of your resume page
        driver.get(request.build_absolute_uri(reverse('preview')))

        # Using Chrome's built-in PDF printing feature
        pdf_data = driver.execute_cdp_cmd("Page.printToPDF", {"printBackground": True})
        pdf_content = base64.b64decode(pdf_data['data'])

        # Save screenshot to a temporary file
        temp_pdf_path = '/tmp/resume.pdf'
        with open(temp_pdf_path, 'wb') as f:
            f.write(pdf_content)

        # Check if PDF is correctly generated
        if os.path.exists(temp_pdf_path) and os.path.getsize(temp_pdf_path) > 0:
            # Error handling for Cloudinary upload
            try:
                # Upload to Cloudinary
                upload_response = cloudinary.uploader.upload(temp_pdf_path, resource_type='auto', public_id='daniel_brunker_resume')
                pdf_url = upload_response.get('url')
                # Redirect user to the Cloudinary URL to download the PDF
                return redirect(pdf_url)
            except Exception as e:
                return HttpResponse(f"Error uploading to Cloudinary: {e}", status=500)
        else:
            return HttpResponse("Failed to generate PDF file.", status=500)
    except Exception as e:
        return HttpResponse(f"Error generating PDF: {e}", status=500)
    finally:
        driver.quit()