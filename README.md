# IDOM Package Cookiecutter

![Test](https://github.com/idom-team/idom-package-cookiecutter/workflows/Test/badge.svg?branch=main)

A [`cookiecutter`](https://cookiecutter.readthedocs.io/en/1.7.2/README.html) template for packaging Javascript components with IDOM

# About IDOM

IDOM is a framework for creating highly interactive web pages purely in Python. However,
IDOM also provides a way to natively interface with the Javascript ecosystem. This
repository defines a basic template for creating packages wich distribute Javascript for
use in IDOM-based applications.

For more information about IDOM refer to its [documentation](https://idom-docs.herokuapp.com/docs/index.html).

# Usage

Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/1.7.2/README.html) with `pip`:

```bash
pip install cookiecutter
```

Then use this repostory template as a cookiecutter to initalize a repository:

```bash
cookiecutter https://github.com/idom-team/idom-react-component-cookiecutter.git
```

As the template is being constructed you will be prompted to fill out the following information:

| Field                       | Description                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------- |
| `author_name`               | your name or the name of your organization                                          |
| `author_email`              | your email of the email of your organization                                        |
| `repository_name`           | the name of your repository's root directory                                        |
| `repository_url`            | the URL your repository can be found at                                             |
| `python_package_name`       | the name of the "backend" Python package your Javascript components will be used in |
| `npm_package_name`          | the name of the "frontend" Javascript package used by your Python package           |
| `project_short_description` | a short summary used to describe both Python and Javascript packages                |

After this you should find a new directory named after the given `repository_name`.

# Template Manifest

The template generates the following files:

```
├── {python_package_name}
│   ├── __init__.py
│   └── example.py
├── js
│   ├── src
│   │   ├── index.js
│   ├── package.json
│   ├── README.md
│   └── rollup.config.js
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_example.py
├── .gitignore
├── MANIFEST.in
├── README.md
├── setup.cfg
└── setup.py
```

The key consituents of the generated repository are briefly described below:

| File/Directory           | Contents                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------- |
| `js/`                    | a bare-bones Javascript component that is bundled with [Rollup](https://rollupjs.org/)            |
| `{python_package_name}/` | minimial code required to load the Javascript component                                           |
| `tests/`                 | a basic [`selenium`](https://selenium-python.readthedocs.io/)-based test suite for your component |

# Run the Tests

To run the tests for this repository you'll need the
[ChromeDriver](https://chromedriver.chromium.org/downloads) in your `PATH`. Once that's
done, simply `pip` install the requirements:

```bash
pip install -r requirements.txt
```

And run the `test` session with [Nox](https://nox.thea.codes/en/stable/):

```bash
nox -s test
```

To run in headless mode:

```bash
nox -s test -- --headless
```
