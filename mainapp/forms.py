from django import forms
from .models import Local, Irmao
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
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
                Column('dataini', css_class='form-group col-md-4 mb-0')
            ),
            Row(
                Column('irmaocontato', css_class='form-group col-md-4 mb-0'),
                Column('telefonecontato', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('statuslocal', css_class='form-group col-md-4 mb-0')
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
        fields = ('statuslocal', 'cidade', 'uf', 'dataini', 'irmaocontato', 'telefonecontato', 'usuario')
        labels = {
            'statuslocal': 'Situação da Localidade: ',
            'dataini': 'Data de Início da Localidade: ',
            'irmaocontato': 'Irmão para Contato: ',
            'telefonecontato': 'Telefone de Contato: ',
            'uf': 'Estado: ',
            'cidade': 'Cidade: '
        }


class LocalFormEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LocalFormEdit, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Row(
                Column('nomelocal', css_class='form-group col-md-4 mb-0')
            ),
            Row(
                Column('cidade', css_class='form-group col-md-4 mb-0'),
                Column('uf', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('dataini', css_class='form-group col-md-4 mb-0')
            ),
            Row(
                Column('irmaocontato', css_class='form-group col-md-4 mb-0'),
                Column('telefonecontato', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('statuslocal', css_class='form-group col-md-4 mb-0')
            ),
            Submit('submit', 'Criar')
        )

    class Meta:
        model = Local
        fields = ('nomelocal', 'statuslocal', 'cidade', 'uf', 'dataini', 'irmaocontato', 'telefonecontato')
        labels = {
            'nomelocal': 'Nome da Localidade: ',
            'statuslocal': 'Situação da Localidade: ',
            'dataini': 'Data de Início da Localidade: ',
            'irmaocontato': 'Irmão para Contato: ',
            'telefonecontato': 'Telefone de Contato: ',
            'uf': 'Estado: ',
            'cidade': 'Cidade: '
        }


class IrmaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IrmaoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout = Layout(
            Row(
                Column('local', css_class='form-group col-md-3 mb-0'),
                Column('cidade', css_class='form-group col-md-3 mb-0'),
                Column('uf', css_class='form-group col-md-2 mb-0')
            ),
            Row(
                Column('telefonecontato', css_class='form-group col-md-2 mb-0'),
                Column('emailcontato', css_class='form-group col-md-4 mb-0')
            ),
            Row(
                Column('genero', css_class='form-group col-md-2 mb-0'),
                Column('estadocivil', css_class='form-group col-md-2 mb-0'),
                Column('datanasc', css_class='form-group col-md-2 mb-0')
            ),
            Row(
                Column('status', css_class='form-group col-md-3 mb-0')
            )
        )

        for f in self.fields:
            #  self.fields[f].label = _(self.fields[f].label)
            if isinstance(self.fields[f].widget, Select):
                self.fields[f].widget.attrs['disabled'] = 'disabled'
            else:
                self.fields[f].widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Irmao
        fields = ('local', 'cidade', 'uf', 'genero', 'datanasc', 'estadocivil',
                  'telefonecontato', 'emailcontato', 'status')
        labels = {
            'local': 'Localidade: ',
            'cidade': 'Cidade: ',
            'uf': 'UF: ',
            'genero': 'Gênero: ',
            'datanasc': 'Data Nascimento: ',
            'estadocivik': 'Estado Civil: ',
            'telefonecontato': 'Contato: ',
            'emailcontato': 'Email: ',
            'status': 'Situação: '
        }
