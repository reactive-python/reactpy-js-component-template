import reactpy
from reactpy.testing import poll

from {{ cookiecutter.python_package_name }}.example import ExampleCounter


async def test_example_counter(display):
    count = reactpy.Ref(0)

    await display.show(
        lambda: ExampleCounter(
            on_count_change=count.set_current,
            button_text="this is a test",
            button_id="test-button",
        )
    )

    client_side_button = await display.page.wait_for_selector("#test-button")
    poll_count = poll(lambda: count.current)

    await client_side_button.click()
    await poll_count.until_equals(1)

    await client_side_button.click()
    await poll_count.until_equals(2)
