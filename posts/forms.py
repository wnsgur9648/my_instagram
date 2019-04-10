from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    content = forms.CharField(label="content")
    
    class Meta:
        model = Post
        # input을 만들 column 값들을 만들어 넣어준다.
        fields = ['content',]
        widget = {
            'content': forms.Textarea(attrs={
                'class': '',
                'rows': 5,
                'cols': 50,
                'placeholder': "지금 뭘하고 계신가요?",
            })
        }