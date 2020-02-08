from django import forms
from .models import Local, Irmao


class LocalForm(forms.ModelForm):

    class Meta:
        model = Local
        fields = ('statuslocal', 'cidade', 'uf', 'dataini', 'irmaocontato', 'telefonecontato')


class IrmaoForm(forms.ModelForm):

    class Meta:
        model = Irmao
        fields = ('imagefoto', 'local', 'contatolocal', 'cidade', 'uf', 'genero', 'datanasc', 'estadocivil',
                  'telefonecontato', 'emailcontato', 'status', 'parentes', 'observacoes')
