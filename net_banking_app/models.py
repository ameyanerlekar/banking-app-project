from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
	username = models.CharField(max_length = 30, primary_key = True)
	first_name = models.CharField(max_length = 15)
	last_name = models.CharField(max_length = 15)
	address = models.TextField()
	
	def __str__(self):
		return self.first_name + " " + self.last_name + " (" + self.username + ")"
	
class Account(models.Model):
	owner = models.ForeignKey(Customer, on_delete = models.CASCADE)
	account_number = models.IntegerField(primary_key = True)
	account_balance = models.FloatField()
	created_date = models.DateTimeField()
	frozen = models.BooleanField(default = False)
	
	def open(self):
		self.created_date = timezone.now()
		self.save()
		return "Account Created Successfully."
		
	def close(self):
		self.delete()
		return "Account: " + self.account_number + " has been closed successfully."	#also write code to transfer balance funds to another account
		
	def get_balance(self):
		if not self.frozen:
			return self.account_balance()
		else:
			return "Sorry, your account: " + self.account_number + " has been frozen temporarily due to security reasons. Please visit your nearest branch to resolve this issue."
		
	def credit(self, credit_amount):
		if not self.frozen:
			self.account_balance = self.account_balance + credit_amount
			self.save()
		else:
			return "Sorry, your account: " + self.account_number + " has been frozen temporarily due to security reasons. Please visit your nearest branch to resolve this issue."

	def debit(self, debit_amount):
		if not self.frozen:
			self.account_balance = self.account_balance + debit_amount
			self.save()
		else:
			return "Sorry, your account: " + self.account_number + " has been frozen temporarily due to security reasons. Please visit your nearest branch to resolve this issue."
		
	def freeze(self):
		self.frozen = True
		self.save()
		return "The account: " + self.account_number + "has been frozen successfully."
		
	def unfreeze(self):
		self.frozen = False
		self.save()
		return "The account: " + self.account_number + "has been returned to a fully functional state successfully."
		