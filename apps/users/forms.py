from django import forms


class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label='Nome da loja',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Digite o login da Loja"
        })
    )

    senha_login = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': "Digite sua senha"
        })
    )


class RegisterForm(forms.Form):
    nome_registro = forms.CharField(
        label='Nome da loja para registro',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Digite o login para a loja"
            })
        )

    email = forms.EmailField(
        label='E-mail',
        required=True,
        max_length=70,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "Digite o e-mail da sua loja"
            })
        )

    senha_registro = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': "Digite sua senha"
            })
        )

    senha_registro_confirm = forms.CharField(
        label='Confirmação de senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': "Digite sua senha novamente"
            })
        )

    def clean_nome_registro(self):
        nome = self.cleaned_data.get('nome_registro')
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possivel inserir espaços dentro do campo usuário")
            else:
                return nome

    def clean_senha_registro_confirm(self):
        senha1 = self.cleaned_data['senha_registro']
        senha2 = self.cleaned_data['senha_registro_confirm']
        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError("Senhas diferentes uma da outra")
            else:
                return senha2
