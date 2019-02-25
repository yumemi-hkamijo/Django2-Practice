from django.contrib import admin
from django import forms
from .models import Publisher, Author, Book

class BookAdminForm(forms.ModelForm):
    def clean_title(self):
        value = self.cleaned_data['title']
        if 'Django' not in value:
            raise forms.ValidationError("タイトルには「Django」を含めてください")
        return value


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'price')
    ordering = ('-price')
    fields = ('title', 'publisher', 'authors', 'price',)

# Register your models here.
admin.site.Register(Publisher)
admin.site.Register(Author)
admin.site.Register(Book)
