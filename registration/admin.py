from django.contrib import admin
from .models import JobSeeker, JobProvider, JobDetails, JobApplication, UserDetails , JobsCompleted , Genre


admin.site.register(JobSeeker)
admin.site.register(JobProvider)
admin.site.register(JobDetails)
admin.site.register(JobApplication)
admin.site.register(UserDetails)
admin.site.register(JobsCompleted)
admin.site.register(Genre)


