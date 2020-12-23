# {{ cookiecutter.npm_package_name }}

{{ cookiecutter.project_short_description }}

# Package Installation

Requires [Node](https://nodejs.org/en/) to be installed:

```bash
npm install --save {{ cookiecutter.npm_package_name }}
```

For a developer installation, `cd` into this directory and run:

```bash
npm install
npm run build
```

This will install required dependencies and generate a Javascript bundle that is saved
to `{{ cookiecutter.python_package_name }}/bundle.js`` and is distributed with the
associated Python package.
