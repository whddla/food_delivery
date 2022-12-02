from django import forms
from food_delivery.models import User
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):                                  
    username = forms.CharField(                               
        error_messages={                                      
            'required': '아이디를 입력해주세요'
        },
        max_length=50, label="아이디")                     
    
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        },
        max_length=50,widget=forms.PasswordInput, label="비밀번호")           
    
    def clean(self):                                           
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password :
            try:
                user = User.objects.get(id=username,pw=password)
                if not check_password(password, user.pw):
                    self.add_error('password', '비밀번호를 틀렸습니다.')     (7)
                else:
                    self.user_no = user.no                                 (8)
            except Exception:
                self.add_error('username', '존재하지 않는 아이디 입니다.')

