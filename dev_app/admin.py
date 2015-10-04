from django.contrib import admin
from .models import page, logo, pulled
#,logo,pulled

class logoInline(admin.TabularInline):
	model=	logo
	extra = 1
	
class pulledInline(admin.StackedInline):
	model = pulled
	extra = 0

class pageAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,	{'fields': ['page_title','page_domain','page_url']}),
	]
	inlines = [logoInline, pulledInline]

admin.site.register(page, pageAdmin)
#,logo,pulled)
# Register your models here.
