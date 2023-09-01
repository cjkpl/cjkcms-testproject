#!/usr/bin/env python
import sys
from unittest import TestSuite
from boot_django import boot_django

boot_django()

default_labels = [
    "myapp.tests",
]


def get_suite(labels=default_labels):
    from django.test.runner import DiscoverRunner

    runner = DiscoverRunner(verbosity=1)
    if failures := runner.run_tests(labels):
        sys.exit(failures)
    return TestSuite()


if __name__ == "__main__":
    labels = sys.argv[1:] if len(sys.argv[1:]) > 0 else default_labels
    get_suite(labels)
