from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class FontFamily(models.Model):
    family_name = models.CharField(max_length=200, null=True, blank=True)
    serif_type = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"'{self.family_name}', {self.serif_type}"
    
class PageStyle(models.Model):
    template_name = models.CharField(max_length=200,null=True, blank=True)
    template_url = models.URLField(max_length=200, null=True, blank=True)
    header_font = models.ManyToManyField(FontFamily, blank=True, related_name='headers')  
    header_font_size = models.CharField(max_length=200, null=True, blank=True)
    header_font_weight = models.CharField(max_length=200, null=True, blank=True)
    font = models.ManyToManyField(FontFamily, blank=True, related_name='general')  

    def __str__(self):
        return self.template_name
    
class NavMenu(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
class Summary(models.Model):
    first_name = models.CharField(max_length=200,null=True, blank=True)
    last_name = models.CharField(max_length=200,null=True, blank=True)
    image = CloudinaryField('image', null=True, blank=True)
    desired_job = models.CharField(max_length=200, null=True, blank=True)
    objective = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.desired_job
    
class Company(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Achievement(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE, related_name='company_achievements') 
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.company:
            return f'{self.company.name} - {self.title}'
        else:
            return 'No Company'
    
class Experience(models.Model):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    present = models.BooleanField(null=True, blank=True)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE, related_name='hired_companies') 
    job_title = models.CharField(max_length=200, null=True, blank=True)
    achievements = models.ManyToManyField(Achievement, blank=True, related_name='accomplishments') 

    def __str__(self):
        if self.company:
            return self.company.name
        else:
            return 'No Company'
        
class Education(models.Model):
    year = models.DateField(null=True, blank=True)
    school = models.CharField(max_length=200,null=True, blank=True)
    major = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
            return self.school
    
class Membership(models.Model):
    membership_cert = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.membership_cert
    
class Skill(models.Model):
    type = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.type

class SkillGroup(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name='skills')

    def __str__(self):
        return self.name
    
class SocialMediaItem(models.Model):
    social = models.CharField(max_length=200, null=True, blank=True)
    font_awesome = models.CharField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.social