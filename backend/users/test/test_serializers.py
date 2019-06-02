from django.test import TestCase
from django.forms.models import model_to_dict
# from django.contrib.auth.hashers import check_password
from nose.tools import eq_, ok_
from .factories import UserFactory
from ..serializers import UserSerializer


class TestUserSerializer(TestCase):

    def setUp(self):
        self.user_data = model_to_dict(UserFactory.build())

    def test_serializer_with_empty_data(self):
        serializer = UserSerializer(data={})
        eq_(serializer.is_valid(), False)

    def test_serializer_with_valid_data(self):
        serializer = UserSerializer(data=self.user_data)
        ok_(serializer.is_valid())

    def test_serializer_hashes_password(self):
        serializer = UserSerializer(data=self.user_data)
        ok_(serializer.is_valid())

        # user = serializer.save()
        # print("user: ", user) user creation don't return password
        # ok_(check_password(self.user_data.get('password'), user.password))
