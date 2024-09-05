from __future__ import unicode_literals

from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250, null=True)

    def json_object(self):
        return {
            "name": self.name,
            "location": self.location
        }

    def __str__(self):
        return self.name 


class Branch(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    branch_code = models.CharField(max_length=250)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Branches"

    def json_object(self):
        return {
            "name":self.name,
            "location":self.location,
            "branch_code":self.branch_code,
            "home":self.home
        }
    
    def __str__(self):
        return self.name


class ClientManager(models.Model):
    name = models.CharField(max_length=250)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def json_object(self):
        return {
            "name":self.name,
            "address":self.address
        }

    def __str__(self):
        return self.name


class Account(models.Model):
    """Represents Bank Account"""
    client = models.ForeignKey(Client,on_delete=models.CASCADE, null=True)
    open_date = models.CharField(max_length=250)
    account_type = models.CharField(max_length=250)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE, null=True)
    
    @property
    def balance(self):
        deposits = sum([deposite.amount for deposite in Deposit.objects.filter(account=self.id)])
        Withdrawals = sum([withdraw.amount for withdraw in Withdraw.objects.filter(account=self.id)])

        total = deposits + Withdrawals
        return total

    def json_object(self):
        return {
            "client":self.client,
            "open_date":self.open_date,
            "account_type":self.account_type,
            "branch":self.branch

        }

    def __str__(self):
        return self.client.name


class Transfer(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)

    def json_object(self):
        return {
            "account":self.account,
            "branch":self.branch
        }

    def __str__(self):
        return "Account Transfered to {} Branch".format(self.branch.name)


class Withdraw(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)


class Deposit(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)