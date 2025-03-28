import allure
import random
import pytest


@allure.epic("Authentication and Access Management")
@allure.feature("Authentication")
@allure.story("Create new issue")
@allure.tag("Тег")
@allure.label("priority", "1 - High")
@allure.label("service", "Monitoring Service")
@allure.label("owner", "qartavtsev_admin")  # Используем label вместо owner
@pytest.mark.parametrize("random_fail", [random.choice([True, False])])
def test_example(random_fail):
    allure.step("Обычный шаг 1")
    
    with allure.step("Обычный шаг 2"):
        allure.step("Обычный подшаг 2.1")
        with allure.step("Обычный подшаг 2.2"):
            allure.step("Обычный подподшаг 2.2.1")
            allure.step("Обычный подподшаг 2.2.2")

    with allure.step("Шаг с ожидаемым результатом 1"):
        with allure.step("Ожидаемый результат"):
            allure.step("Ожидаемый результат 1.1")
            allure.step("Ожидаемый результат 1.2")

    with allure.step("Шаг с ожидаемым результатом 2"):
        allure.step("Обычный подшаг в шаге с ожидаемым результатом 2.1")
        allure.step("Обычный подшаг в шаге с ожидаемым результатом 2.2")
        with allure.step("Ожидаемый результат"):
            with allure.step("Ожидаемый результат 2.1"):
                if random_fail:
                    pytest.fail("Шаг 'Ожидаемый результат 2.1' упал!")

    with allure.step("Шаг с ожидаемым результатом 3"):
        with allure.step("Подшаг с ожидаемым результатом в шаге с ожидаемым результатом 3.1"):
            with allure.step("Ожидаемый результат"):
                allure.step("Ожидаемый результат 3.1.1")
