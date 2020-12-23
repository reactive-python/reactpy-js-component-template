from pathlib import Path

import idom

_js_module = idom.Module(
    "{{ cookiecutter.npm_package_name }}",
    source_file=Path(__file__).parent / "bundle.js"
)
_ExampleComponent = _js_module.define("ExampleCounter", has_children=False)


def ExampleCounter(on_count_change, button_text, button_id):
    return _ExampleComponent(
        {
            "onCountChange": on_count_change,
            "buttonText": button_text,
            "buttonId": button_id
        }
    )
