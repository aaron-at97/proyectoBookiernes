from django.contrib import admin
import eBook.models

admin.site.register(eBook.models.Book)
admin.site.register(eBook.models.Notification)
admin.site.register(eBook.models.Writer)
admin.site.register(eBook.models.Editor)
admin.site.register(eBook.models.EditorChief)
admin.site.register(eBook.models.ChiefDesigner)
admin.site.register(eBook.models.Designer)
admin.site.register(eBook.models.CTO)
admin.site.register(eBook.models.Developer)
admin.site.register(eBook.models.Clients)