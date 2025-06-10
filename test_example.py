import allure
import pytest

@pytest.mark.parametrize("username", ["John", "Alice"])
@allure.tag("Tag 1", "Tag 2", "Tag 3")
@allure.title("Test case example for NBC Universal - {username}")
@allure.label("owner", "John Smith")
@allure.label("priority", "1 - High")
@allure.label("service", "Authentication Service")
@allure.feature("Authentication")
def test_example(username):
    with allure.step("Step 1"):
        pass
    with allure.step("Step 2"):
        with allure.step("Sub-step 2.1"):
            pass
        with allure.step("Sub-step 2.2"):
            pass
    with allure.step("Step 3"):
        pass

@allure.title("Test case example for NBC Universal - dynamic parameter"
def test_sum():
    x = 1
    y = 2
    ttl = 3
    allure.dynamic.parameter("x", x)
    allure.dynamic.parameter("y", y)
    allure.dynamic.parameter("sum", ttl)
