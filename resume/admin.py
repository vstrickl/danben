from django.contrib import admin

from .models import FontFamily
from .models import PageStyle
from .models import NavMenu
from .models import Summary
from .models import SocialMediaItem
from .models import Achievement
from .models import Experience
from .models import Membership
from .models import Education
from .models import Company
from .models import Skill
from .models import SkillGroup

# Register your models here.
admin.site.register(Summary)
admin.site.register(SocialMediaItem)

class CompanyAdmin(admin.ModelAdmin):

    search_fields = ['name']

admin.site.register(Company, CompanyAdmin)

class FontFamilyAdmin(admin.ModelAdmin):

    list_display = ("family_name", "serif_type")
    search_fields = ['family_name']

admin.site.register(FontFamily, FontFamilyAdmin)

class PageStyleAdmin(admin.ModelAdmin):

    autocomplete_fields = ['header_font', 'font']

admin.site.register(PageStyle, PageStyleAdmin)

class NavMenuAdmin(admin.ModelAdmin):
    list_display = ("title", "url")

admin.site.register(NavMenu, NavMenuAdmin)

class ExperienceAdmin(admin.ModelAdmin):

    autocomplete_fields = ['company','achievements']
    list_display = ('company', 'job_title', 'start_date', 'present','end_date')

admin.site.register(Experience, ExperienceAdmin)

admin.site.register(Membership)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'major', 'year')

admin.site.register(Education, EducationAdmin)

class AchievementAdmin(admin.ModelAdmin):

    search_fields = ['company', 'title']

    autocomplete_fields = ['company']
    list_display = ('company', 'title')

admin.site.register(Achievement, AchievementAdmin)

class SkillAdmin(admin.ModelAdmin):

    search_fields = ['type']

admin.site.register(Skill, SkillAdmin)

class SkillGroupAdmin(admin.ModelAdmin):

    autocomplete_fields = ['skills']

admin.site.register(SkillGroup, SkillGroupAdmin)