from pathlib import Path

import idom


_js_module = idom.Module(
    "{{ cookiecutter.npm_package_name }}",
    source_file=Path(__file__).parent / "bundle.js",
    has_mount=True,
)


def ExampleCounter(on_count_change, button_text, button_id):
    return _js_module.ExampleCounter(
        {
            "onCountChange": on_count_change,
            "buttonText": button_text,
            "buttonId": button_id
        }
    )
