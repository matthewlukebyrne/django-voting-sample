from django.contrib import admin

# Register your models here.
# Shows up on admin page

from .models import Question, Choice
# admin.site.register(Question)
# admin.site.register(Choice)


# Change the main admin header
admin.site.site_header = 'Pollster Example'
admin.site.site_title = 'Pollster Admin Area'
admin.site.index_title = 'Welcome to the admin area dude!'


# Tabluar inline
class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

# Extend model Admin
# Python dictonary
class  QuestionAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields': ['question_text']}),
  ('Date Information', {'fields': ['pub_date'], 'classes': ['collapase']}), ] 

  inlines = [ChoiceInline]

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)