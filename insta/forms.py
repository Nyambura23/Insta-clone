from django import forms
from .models import Image,Profile,Comment

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['likes','user','posted_at','comments']
 
 
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        exclude=['user'] 
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment        
        fields=['comment']          