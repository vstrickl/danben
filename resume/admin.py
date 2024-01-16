from django.contrib import admin

from .models import FontFamily, PageStyle, NavMenu, Summary, SocialMediaItem, Achievement, Experience, Company, Skill, SkillGroup

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

class AchievementAdmin(admin.ModelAdmin):

    search_fields = ['date','company']

    autocomplete_fields = ['company']
    list_display = ('date', 'company')

admin.site.register(Achievement, AchievementAdmin)

class SkillAdmin(admin.ModelAdmin):

    search_fields = ['type']

admin.site.register(Skill, SkillAdmin)

class SkillGroupAdmin(admin.ModelAdmin):

    autocomplete_fields = ['skills']

admin.site.register(SkillGroup, SkillGroupAdmin)