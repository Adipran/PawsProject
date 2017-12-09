
from django.db import models


# codeGroup model
class codeGroup(models.Model):
    codeGroupID = models.IntegerField(primary_key=True)
    codeGroupName = models.CharField(max_length=255, null=False, unique=True)
    #createdBy = models.ForeignKey('users.user', related_name='codeGroup_createdBy', db_column='createdBy')
    createdOn = models.DateTimeField(auto_now_add=True)
    #modifiedBy = models.ForeignKey('users.user', related_name='codeGroup_modifiedBy', db_column='modifiedBy')
    modifiedOn = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'com_codeGroup'
        get_latest_by = 'codeGroupName'



# code model

class code(models.Model):
    codeID = models.IntegerField(primary_key=True)
    codeGroup = models.ForeignKey('codeGroup', db_column='codeGroupID', null=False, related_name="code_codeGroupID")
    codeName = models.CharField(max_length=255, null=False)
    displayOrder = models.IntegerField(null=True, blank=True)
    comment = models.CharField(max_length=255, null=True)
    #createdBy = models.ForeignKey('users.user', related_name='code_createdBy', db_column='createdBy')
    createdOn = models.DateTimeField(auto_now_add=True)
    #modifiedBy = models.ForeignKey('users.user', related_name='code_modifiedBy', db_column='modifiedBy')
    modifiedOn = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'com_code'


get_latest_by = 'codeNameEn'


#pet
class pet(models.Model):
    petID = models.AutoField(primary_key=True)
    petCategory = models.ForeignKey('code', db_column='petCategory')
    petName = models.CharField(max_length=255)
    petDescription = models.TextField()
   # createdBy = models.ForeignKey('users.user', related_name='code_createdBy', db_column='createdBy')
    createdOn = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'pet_pet'


class petDetails(models.Model):
    petDetailsID = models.AutoField(primary_key=True)
    petID = models.ForeignKey('pet', db_column='petID')
    petAge = models.FloatField()
    petType = models.ForeignKey('code', db_column='petType')
    petColor = models.CharField(max_length=255)
    petHeight = models.FloatField()
    petWeight = models.FloatField()
    # createdBy = models.ForeignKey('users.user', related_name='code_createdBy', db_column='createdBy')
    createdOn = models.DateTimeField(auto_now_add=True)
    # modifiedBy = models.ForeignKey('users.user', related_name='code_modifiedBy', db_column='modifiedBy')
    modifiedOn = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pet_petDetails'






