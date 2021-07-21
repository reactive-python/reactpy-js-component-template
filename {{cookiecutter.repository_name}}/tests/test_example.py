import idom

from {{ cookiecutter.python_package_name }}.example import ExampleCounter


def test_example_counter(driver, driver_wait_until, display):
    count = idom.Ref(0)

    display(
        lambda: ExampleCounter(
            on_count_change=count.set_current,
            button_text="this is a test",
            button_id="test-button",
        )
    )

    client_side_button = driver.find_element_by_id("test-button")

    client_side_button.click()
    driver_wait_until(lambda: count.current == 1)

    client_side_button.click()
    driver_wait_until(lambda: count.current == 2)
