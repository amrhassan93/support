
from .models import *
from django.utils import timezone
from django.forms import ModelForm
from django import forms




class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'target',
                  'start_date', 'end_date', 'category_id', 'tags','user_id']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date <= start_date:
            msg = u"End date should be greater than start date."
            self._errors["end_date"] = self.error_class([msg])

class ImageForm(forms.ModelForm):
    #image = forms.ImageField(label='Image')
    class Meta:
        model = ProjectPicture
        fields = ['img_url', ]

   


# class reviewform(forms.ModelForm):
    
#     class Meta:
#         model=Comments
#         fields=['content',]
       
# class rateform(forms.ModelForm):

#     class Meta:
#         model=Rating
#         fields=['value',]




