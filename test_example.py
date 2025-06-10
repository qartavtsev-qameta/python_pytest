import allure
import pytest

@allure.tag("Tag 1", "Tag 2", "Tag 3")
@allure.title("Test case example for NBC Universal")
@allure.label("owner", "John Smith")
@allure.feature("Authentication")
def test_example():
    Allure::label("priority", "1 - High");
    Allure::label("service", "Authentication Service");
    with allure.step("Step 1"):
        pass
    with allure.step("Step 2"):
        with allure.step("Sub-step 2.1"):
            pass
        with allure.step("Sub-step 2.2"):
            pass
    with allure.step("Step 3"):
        pass
