import allure
import random
import pytest


@allure.epic("Authentication and Access Management")
@allure.feature("Authentication")
@allure.story("Create new issue")
@allure.tag("Tag")
@allure.label("severity", "1 - High")
@allure.label("service", "Monitoring Service")
@allure.label("owner", "John Smith")
@pytest.mark.parametrize("random_fail", [random.choice([True, False])])
def test_example(random_fail):
    allure.step("Step 1")
    
    with allure.step("Step 2"):
        allure.step("Sub-step 2.1")
        with allure.step("Sub-step 2.2"):
            allure.step("Sub-step 2.2.1")
                if random_fail:
                    pytest.fail("Step failed!")
