from django import forms

class Student(forms.Form):
    name = forms.CharField(error_messages={'required':'ENter Your Name '})
    lname = forms.CharField(error_messages={'required':'Enter Your Last Name'})
    
    
    # def clean_name(self):

    #     valname = self.cleaned_data['name']
    #     if len(valname) < 4 :
    #         raise forms.ValidationError('Name should be equal to four or greater then four')
    #     return valname
    

    # def clean_lname(self):
    #     vallname = self.cleaned_data['lname']
    #     if len(vallname) > 4 :
    #         raise forms.ValidationError('Lname must be less then four')
    #     return vallname

    def clean(self):
        cleaned_data = super().clean()
        nm = self.cleaned_data['name']
        ln = self.cleaned_data['lname']
      
        if len(nm) < 5 :
            raise forms.ValidationError('ENter five  digit name' )
        
        elif len(ln) > 4 :
            raise forms.ValidationError('Enter last name must be less then four')
        return cleaned_data