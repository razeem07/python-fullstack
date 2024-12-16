from django import forms

class BmiForm(forms.Form):

    height=forms.IntegerField()

    weight=forms.IntegerField()

  


class VehicleForm(forms.Form):
    
     name=forms.CharField()

     running_km =forms.IntegerField()

     OWNER_CHOICES=(
     ("single owner","Single Owner"),
     ("second owner","Second Owner"),
     ("third owner","Third Owner"),
     )

     owner_type=forms.ChoiceField(choices=OWNER_CHOICES)

     price =forms.IntegerField()

     FUEL_CHOICES=(
          ("petrol","Petrol"),
          ("diesel","Diesel"),
          ("electric","EV"),
          ("cng","CNG"),
     )

     fuel_type=forms.ChoiceField(choices=FUEL_CHOICES)


class BmrForm(forms.Form):

    height=forms.IntegerField()

    weight=forms.IntegerField()

    age =forms.IntegerField()
    
    GENDER_CHOICES=(
          ("male","Male"),
          ("female","Female"),
     )
    
    gender_type=forms.ChoiceField(choices=GENDER_CHOICES)

     
    ACTIVITY_CHOICES=(
          ("active","active"),
          ("moderately active","moderately active"),
          ("very active","very active"),
          ("not active","not active")
     )
    
    activity_level =forms.ChoiceField(choices=ACTIVITY_CHOICES)


class MilegeForm(forms.Form):
    
     distance=forms.IntegerField()

     consumption=forms.IntegerField()


