import allure
import pytest

@allure.tag("Tag 1", "Tag 2", "Tag 3")
@allure.title("Test case example for NBC Universal")
@allure.label("owner", "John Smith")
@allure.label("priority", "1 - High")
@allure.label("service", "Authentication Service")
@allure.feature("Authentication")
def test_example():
    with allure.step("Step 1"):
        pass
    with allure.step("Step 2"):
        with allure.step("Sub-step 2.1"):
            pass
        with allure.step("Sub-step 2.2"):
            pass
    with allure.step("Step 3"):
        pass
