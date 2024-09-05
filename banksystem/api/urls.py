from django.urls import path

from .views import BanksAPIView, AccountDetailAPIView, WithdrawListAPIView, DepositeListAPIView, AccountListAPIView, BranchsAPIView, BranchDetailAPIView, BankDetailAPIView, CreateAccountAPIView

urlpatterns = [
    path(r'branchs/', BranchsAPIView.as_view(), name="branchs"),
    path(r'branch/<pk>', BranchDetailAPIView.as_view(), name="branch"),
    path(r'banks/', BanksAPIView.as_view(), name='banks'),
    path(r'bank/<pk>', BankDetailAPIView.as_view(), name="bank"),
    path(r'create_account/', CreateAccountAPIView.as_view(), name="createAccount"),
    path(r'accounts/', AccountListAPIView.as_view(), name="accounts"),
    path(r'account/<pk>', AccountDetailAPIView.as_view(), name="account"),
    path(r'deposite/', DepositeListAPIView.as_view(), name="deposite"),
    path(r'withdraw/', WithdrawListAPIView.as_view, name="withddraw")
]
