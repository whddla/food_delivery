from django import forms
from food_delivery.models import User

class LoginForm(forms.Form):                                  
    id = forms.CharField(                               
        error_messages={                                      
            'required': '아이디를 입력해주세요'
        },
        max_length=50, label="아이디")                     
    
    pw = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        max_length=50,widget=forms.PasswordInput, label="비밀번호")           
    
    def clean(self):                                           
        cleaned_data = super().clean()
        id = cleaned_data.get('id')
        pw = cleaned_data.get('pw')

        if id and pw :
            try:
                user = User.objects.get(id=id)
            except Exception:
                self.add_error('id', '존재하지 않는 아이디 입니다.')
                return
            if user.pw != pw:
                self.add_error('pw', '비밀번호를 틀렸습니다.') 

            else:
                self.user_id = user.id 