from django.utils.translation import gettext as _
from django.conf import settings
from rest_framework import serializers
from rest_auth.serializers import PasswordResetSerializer
from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.models import EmailAddress
from allauth.account.utils import setup_user_email
from .models import User


class UserSerializer(serializers.ModelSerializer):
    account_verified = serializers.SerializerMethodField()
    extra_kwargs = {
        'email': {'allow_null': False, 'required': True}
    }

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'about', 'account_verified')
        # read_only_fields = ('username', )

    def get_account_verified(self, object):  # dynamic field
        result = EmailAddress.objects.filter(email=object.email)
        if len(result):
            return result[0].verified
        return False


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user


class CustomPasswordResetSerializer(PasswordResetSerializer):

    def get_email_options(self):
        return {
            'domain_override': settings.URL_FRONT,
            'html_email_template_name': 'registration/password_reset_email.html',
        }
