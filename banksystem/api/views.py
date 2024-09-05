from django.shortcuts import render
from django.http import Http404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bank, Branch, Client, ClientManager, Account, Transfer, Withdraw, Deposit
from .serializers import BankSerializer, AccountDetailSerializer, BranchSerializer, ClientSerializer, ClientManagerSerializer, AccountSerializer, TransferSerializer, WithdrawSerializer, DepositSerializer


class BranchsAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BanksAPIView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BankSerializer


class CreateAccountAPIView(APIView):

    def post(self, request):
        client = Client.objects.create(
            name = request.data['name'],
            address = request.data['address']
        )
        branch = Branch.objects.get(pk=request.data['branch'])
        account = Account.objects.create(
            client = client,
            open_date = request.data['open_date'],
            account_type = request.data['account_type'],
            branch = branch
        )

        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class DepositeListAPIView(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


class WithdrawListAPIView(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer


class AccountDetailAPIView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer