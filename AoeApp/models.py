from django.db import models

# Create your models here.

class Sign_up(models.Model):
    LastName = models.CharField(max_length = 50, verbose_name = 'LastName' )
    FirstName = models.CharField(max_length = 50, verbose_name = 'FirstName' )
    MiddleName = models.CharField(max_length = 50, verbose_name = 'MiddleName' )
    UserName = models.CharField(max_length = 50, verbose_name = 'UserName')
    Password = models.CharField(max_length = 50, verbose_name = 'Password')

    def __str__(self):
        return self.LastName

class Free_Quotation(models.Model):
    status = [
 				('Done', 'Done'),
				('Pending', 'Pending'),
 			]
    Name = models.CharField(max_length = 50, verbose_name = 'Name' )
    Address = models.CharField(max_length = 50, verbose_name = 'Address' )
    Email =  models.EmailField(max_length = 254, verbose_name = 'Email')
    Contact = models.DecimalField(max_digits= 11, decimal_places=0, )
    Date = models.DateField(default='')
    Details = models.TextField()
    Quantity =  models.IntegerField()
    File = models.FileField(upload_to = None, max_length = 100)
    status = models.TextField(max_length =20, choices=status, verbose_name='status', default="pending", null=True )
   
    def __str__(self):
        return self.Name

