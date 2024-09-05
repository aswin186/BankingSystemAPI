from rest_framework import serializers
from .models import Branch, Bank, Client, ClientManager, Account, Withdraw, Transfer, Deposit


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    class Meta:
        model = Branch
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'


class ClientManagerSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()
    class Meta:
        model = ClientManager
        fields = '__all__'



class AccountSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    branch = BranchSerializer()
    class Meta:
        model = Account
        fields = ('__all__')


class AccountDetailSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(decimal_places=2 ,max_digits=100)
    client = ClientSerializer()
    branch = BranchSerializer()
    
    class Meta:
        model = Account
        fields = ['client', 'account_type', 'branch', 'balance']


class TransferSerializer(serializers.ModelSerializer):
    account = AccountSerializer
    class Meta:
        model = Transfer
        fields = ('__all__')


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('__all__')


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('__all__')