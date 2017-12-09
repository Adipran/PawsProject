from django.contrib import admin
from .models import petDetails
from .models import code
from .models import codeGroup
from .models import pet

admin.site.register(petDetails)
admin.site.register(code)
admin.site.register(codeGroup)
admin.site.register(pet)