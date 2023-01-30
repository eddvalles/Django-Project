from django.contrib.admin.apps import AdminConfig

class BookrAdminConfig(AdminConfig):
    default_site = 'admin.BookrAdminSite'