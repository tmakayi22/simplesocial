from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
#this imports pre-determined form created by django

# class name must be diff from imported/inherited class
class UserCreateForm(UserCreationForm):

    class Meta:
        #create fields to be used to confirm password
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # create custom labels to display for each attribute,
        # not necessary, but makes it easier to recognize attributes
        self.fields['username'].label = 'Display Name'
        self.fields['email'].lable = 'Email Address'
