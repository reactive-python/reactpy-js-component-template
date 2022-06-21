# {{ cookiecutter.repository_name }}

{{ cookiecutter.project_short_description }}

# Installation

Use `pip` to install this package:

```bash
pip install {{ cookiecutter.python_package_name }}
```

For a developer installation from source be sure to install [NPM](https://www.npmjs.com/) before running:

```bash
git clone {{ cookiecutter.repository_url }}
cd {{ cookiecutter.repository_name }}
pip install -e . -r requirements.txt
```

# Running the Tests

To run the tests you'll need to install [Chrome](https://www.google.com/chrome/). Then you
can download the [ChromeDriver](https://chromedriver.chromium.org/downloads) and add it to
your `PATH`. Once that's done, simply `pip` install the requirements:

```bash
pip install -r requirements.txt
```

And run the tests with `pytest`:

```bash
pytest tests
```

You can run the tests in headless mode (i.e. without opening the browser):

```bash
pytest tests
```

You'll need to run in headless mode to execute the suite in continuous integration systems
like GitHub Actions.

# Releasing This Package

To release a new version of {{ cookiecutter.python_package_name }} on PyPI:

1. Install [`twine`](https://twine.readthedocs.io/en/latest/) with `pip install twine`
2. Update the `version = "x.y.z"` variable in `{{ cookiecutter.python_package_name }}/__init__.py`
3. `git` add the changes to `__init__.py` and create a `git tag -a x.y.z -m 'comment'`
4. Build the Python package with `python setup.py sdist bdist_wheel`
5. Check the build artifacts `twine check --strict dist/*`
6. Upload the build artifacts to [PyPI](https://pypi.org/) `twine upload dist/*`

To release a new version of `{{ cookiecutter.npm_package_name }}` on [NPM](https://www.npmjs.com/):

1. Update `js/package.json` with new npm package version
2. Clean out prior builds `git clean -fdx`
3. Install and publish `npm install && npm publish`
