Authentication: The process of validating user is called authentication.

Authorization: The process of validating access permissions of user is called authorization.

Generally our web pages can be accessed by any person without having any restrictions.
But some times our business requirement is to access a web page compulsory we have to register and login.Then only end user can able to access our page. To fulfill such of requirements we should go for Django authentication and authorization module. (auth application).


steps for user authentication and authorization:
---------------------------------------------

1) create a app inside project container and register it

	python manage.py startapp app1[appName]

2) create template or media or static based on requirement and build connection

3) create forms.py file in app and create a model form

4) create a modelform class and mention model as User from 

from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password']  or '__all__

5) create a register view


6) first check request.method is post or not if it is post then create a object for formclass by passing request.POST as arguement

7) then check form is valid or not. if it is valid  then check whether the user exist not if exist then message need to created .

8) if we save passowrd will not be hashed to hash the password we need to override save() in form class.


