from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)


class DefaultAccountAdapterCustom(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = settings.URL_FRONT + \
            'verify-email/' + context['key']
        msg = self.render_mail(template_prefix, email, context)
        try:
            msg.send()
        except Exception:
            logger.error('Error in send_mail (after successful user creation)')
            pass
