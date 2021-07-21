from pathlib import Path

from idom.web.module import export, module_from_file


_js_module = module_from_file(
    "{{ cookiecutter.npm_package_name }}",
    file=Path(__file__).parent / "bundle.js",
    fallback="⏳",
)

_ExampleCounter = export(_js_module, "ExampleCounter")


def ExampleCounter(on_count_change, button_text, button_id):
    return _ExampleCounter(
        {
            "onCountChange": on_count_change,
            "buttonText": button_text,
            "buttonId": button_id,
        }
    )
