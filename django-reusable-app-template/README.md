# Django reusable app template

A simple template of a reusable Django app with tests.
This sample app tracks user model changes and deletions and register them in a separate model.

Directions:
- `src/reusable_app` is the reusable app being tested
- `tests/settings.py` is the settings file for the sample project
- `tests/myapp` is an app included in the sample project (required when your reusable app works with external models)
- `pyproject.toml` is containing pytest configuration

Featuring:
- `pytest` as test tooling
- `tox` as test runner
- `pytest-django` integrating Django and pytest
- `factory_boy` providing fixtures for tests
- `pytest-factoryboy` integrating factory_boy and pytest
- `pdbpp` replacing pdb for debugging with lots of features

To run the tests:
1. clone the repo
2. install the deps with `poetry install`
3. run the tests with `poetry run tox`

References:
- https://github.com/torchbox/django-pattern-library/