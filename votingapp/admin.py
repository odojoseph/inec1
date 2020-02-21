from django.contrib import admin
from .models import Voters, VotersAdmin,Vote,VoteAdmin

# Register your models here.
admin.site.register (Voters,VotersAdmin)
admin.site.register (Vote,VoteAdmin)

