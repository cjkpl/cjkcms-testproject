# A minimal Wagtail + CjkCMS project setup

Version 1.0 (2023-08-31)

A Wagtail project, with CjkCMS, useful for testing (as your testproject boilerplate) and temporary, throw-away setups.

## Usage

1. Clone the repo:
```git clone https://github.com/cjkpl/cjkcms-testproject.git```
2. Typically the testproject is called `testproject` so you may want to rename it:
```mv cjkcms-testproject testproject```
3. Add your app to `INSTALLED_APPS` in `settings.py`:


## Repository structure

```manage.py``` - Your regular Django manage.py file. Configures the settings to be read from 

```settings.py``` - Django settings

```urls.py``` - Django URLs configuration

```home/models.py``` - defines `ProjectArticlePage`, `ProjectArticleIndexPage`, and `ProjectWebPage`

This is not strictly necessary, but will make it easier for you to add your own blocks to test.

```home/migrations/*``` - a set of migrations that set CjkCMS-based page as the website homepage. 