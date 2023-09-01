from django.apps import AppConfig


class TestAppConfig(AppConfig):
    name = "myapp.tests.testapp"  # replace `myapp` with your app name
    verbose_name = "TestApp"
