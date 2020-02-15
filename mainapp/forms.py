from django import forms
from .models import Local, Irmao
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django.forms.widgets import Select


class LocalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LocalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Row(
                Column('cidade', css_class='form-group col-md-4 mb-0'),
                Column('uf', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
            Column('dataini', css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('irmaocontato', css_class='form-group col-md-4 mb-0'),
                Column('telefonecontato', css_class='form-group col-md-3 mb-0')
            )
        )

        for f in self.fields:
            #  self.fields[f].label = _(self.fields[f].label)
            if isinstance(self.fields[f].widget, Select):
                self.fields[f].widget.attrs['disabled'] = 'disabled'
            else:
                self.fields[f].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Local
        fields = ('statuslocal', 'cidade', 'uf', 'dataini', 'irmaocontato', 'telefonecontato')
        labels = {
            'statuslocal': 'Situação da Localidade: ',
            'dataini': 'Data de Início da Localidade: ',
            'irmaocontato': 'Irmão para Contato: ',
            'telefonecontato': 'Telefone de Contato: ',
            'uf': 'Estado: ',
            'cidade': 'Cidade: '
        }


class IrmaoForm(forms.ModelForm):

    class Meta:
        model = Irmao
        fields = ('imagefoto', 'local', 'contatolocal', 'cidade', 'uf', 'genero', 'datanasc', 'estadocivil',
                  'telefonecontato', 'emailcontato', 'status', 'parentes', 'observacoes')
