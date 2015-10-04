from django.contrib import admin
from .models import page, logo, pull
#,logo,pulled

class logoInline(admin.TabularInline):
	model=	logo
	extra = 1
	
class pullInline(admin.StackedInline):
	model = pull
	extra = 0

class pageAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,	{'fields': ['page_title','page_domain','page_url']}),
	]
	inlines =	[logoInline, pullInline]
	list_display=	('page_title','page_domain',)

admin.site.register(page, pageAdmin)
#,logo,pulled)
# Register your models here.
