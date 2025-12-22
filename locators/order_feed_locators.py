from selenium.webdriver.common.by import By

class OrderFeedLOcators: 

    LIST_ORDERS = [By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]"]
    NUMBER_ORDER = [By.XPATH, "//*[contains(text(), '#')]"]
    ORDER_NUMBER_WITH_OPENED_WINDOW = [By.XPATH, "//*[contains(@class, 'Modal_orderBox')]/p[1]"]
    ORDERS_NUMBER_LIST = [By.XPATH, "//*[contains(text(), '#')]"]
    COUNTER_ALL_TIME = [By.XPATH, "//*[text()='Выполнено за все время:']/parent::div/p[2]"]
    COUNTER_TODAY = [By.XPATH, "//*[text()='Выполнено за сегодня:']/parent::div/p[2]"]
    ORDERS_NUMBER_LIST_IN_WORK = [By.XPATH, "//*[contains(@class, '_orderListReady')]/li[contains(@class, 'digits')]"]
