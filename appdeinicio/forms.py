from django import forms
  
class CrearProfesorForm(forms.Form):
  nombre = forms.CharField(max_length=100)
  apellido = forms.CharField(label='Apellido', max_length=100)
  
class CrearAlumnoForm(forms.Form):
  nombre = forms.CharField(max_length=100)
  apellido = forms.CharField(label='Apellido', max_length=100)
  nota = forms.IntegerField(label='Nota')

class CrearPruebaForm(forms.Form):
  materia = forms.CharField(max_length=100)
  dificultad = forms.CharField(label='Dificultad', max_length=100)

  
