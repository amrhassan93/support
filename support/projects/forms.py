
from .models import Project,ProjectPicture
from django.utils import timezone
from django.forms import ModelForm
from django import forms




class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'target',
                  'start_date', 'end_date', 'category_id', 'tags']

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




