from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
import re
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.profile.is_active)
        )
account_activation_token = TokenGenerator()