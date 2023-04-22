from django.db import models


class phonebook(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    contact = models.CharField(max_length=15, null=True)

    class Meta:
        managed = False
        db_table = "mstphonebook"

    def number():
        no = phonebook.objects.order_by('phonebook_id').last().phonebook_id + 1
        if no == None:
            return 1
        else:
            return no
    phonebook_id = models.IntegerField(default=number)
