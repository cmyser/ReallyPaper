from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return '/later/list/'
    def get_logout_redirect_url(self, request):
        return '/later/list/'
    def get_email_confirmation_redirect_url(self, request):
        return '/later/list/'
    def get_signup_redirect_url(self, request):
        return '/later/list/'