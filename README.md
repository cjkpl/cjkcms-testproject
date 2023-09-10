# Portable, minimal testproject (3 variants)

## For Wagtail (optionally with CMS) app testing

Version 1.2 (2023-09-10)

When we create an installable application, it should be testable outside of the context of a specific Wagtail project. Therefore, we must provide a portable, minimal django project configuration & setup for such an application.

## Setup

Get a local copy of the repository: download or clone it:
```git clone https://github.com/cjkpl/cjkcms-testproject.git```


This repo contains three alternate setups for testing your app, each in separate subfolder of the repository. Choose one that suits your needs best - the "integrated-testproject" is most convinient, in my opinion.

You should not use all three - choose one, and use files from the selected folder only in your application development.

## I. Integrated `testproject` in `myapp/tests` folder

Copy the contents of `integrated-testproject` folder to your `myapp/tests` folder. If you only use pytest (rather than standard django test runner), you can skip the `manage.py` file.

If you use pytest, add the following to your `pyproject.toml` file, to let pytest know which settings file to use. Replace `myapp` with your app name:

```toml
[tool.pytest.ini_options]
DJANGO_SETTINGS_MODULE = "myapp.tests.settings"
# optional: if you want to use doctests, and get duration of each test
addopts = "--doctest-modules --durations=0"
# optional - if you want to ignore specific folders 
norecursedirs = "project_template"

```
Replace `myapp` with your app name in: 
- `settings.py` (INSTALED_APPS) - twice:

```python
INSTALLED_APPS = [
    "myapp",  # replace with your app name
    "myapp.tests.testapp.apps.TestAppConfig",  # replace `myapp`
    ...
    ]
```

Replace `myapp` with your app name in testapp/apps.py:

```python
class TestAppConfig(AppConfig):
    name = "myapp.tests.testapp"  # replace `myapp` with your app name
```

1. You can run your tests executing in your repo root folder:
```
pytest myapp
```

2. If you use standard django test runner, execute:
```
python myapp/tests/manage.py test
```
Replace `myapp` with your app name in the above shell command.

In this case you need to point django to the your `manage.py` file, which contains reference to the `settings.py` file in the same folder.

## II. Separate `testproject` folder, parallel to `myapp` folder

Use contents of `separate-testproject` folder for this setup. 

Replace `myapp` with your app name in `settings.py`:
```python
INSTALLED_APPS = [
    "myapp",  # replace with your app name
    "testapp",  # replace, or remove if you don't need it
    ...
    ]
```

If you use pytest, add the following to your pyproject.toml file, to let pytest know which settings file to use. Replace myapp with your app name:

1. With pytest, start in the `testproject` folder, and run:
```
pytest ../myapp --ds=settings
```

2. With standard django test runner, start in the `testproject` folder, and run:
```
python manage.py test myapp.tests
```
Assuming that the `myapp` ins installed (probably in editable mode with -e), it will be found by the test runner.

## III. `boot_django + load_tests` setup

Some repositories, and some tutorials use a setup where your `testproject` is not a part of the repository, but is created on the fly by the `load_tests.py`, which calls `boot_django.py`.

Put the three files: `boot_django.py`, `boot_urls.py`, and `load_tests.py` in your repository root folder. Replace `myapp` in `boot_django` and `load_tests` with your app name.

Execute your tests by running:
```
python load_tests.py
```

I haven't figured out how to use `pytest` with this setup.

---

## Repository structure - common for both `testproject` approaches

* ```manage.py``` - Your regular Django manage.py file. Configures the settings to be read from 

* ```settings.py``` - Django settings

* ```urls.py``` - Django URLs configuration

* ```testapp/models.py``` - defines `ProjectArticlePage`, `ProjectArticleIndexPage`, and `ProjectWebPage`

* This is not strictly necessary, but will make it easier for you to add your own blocks to test, if you need them.

* ```testapp/migrations/*``` - a set of migrations that set CjkCMS-based page as the website homepage. 

## Optional componets

### `testapp`
In many scenarios you will not need the `testapp` - you can then remove the folder, and remove it from `INSTALLED_APPS`. The only scenarios where the `testapp` is useful is when you want to add custom blocks to CMS page models, and test them - for example, when you are developing an app that provides a custom block to be used in several projects.

### `wagtail-cjkcms`
This repo is perfectly usable for testing plain Wagtail apps, without the `CjkCMS`. If you don't need the CMS, remove 'wagtail-cjkcms' and its dependencies from `INSTALLED_APPS` in `settings.py` file, and remove unnecessary URLs from `urls.py`

