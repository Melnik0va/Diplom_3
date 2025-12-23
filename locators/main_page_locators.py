from selenium.webdriver.common.by import By

class MainPageLocators(): 
    ACCOUNT_BUTTON = [By.XPATH, "//header/nav/a"]

    LOADING_ANIMATION = [By.XPATH, "//*[@alt='loading animation']/parent::div"]
    CONSTRUCTOR_BUTTON = [By.XPATH, "//*[text()='Конструктор']/parent::a"]
    ORDER_FEED_BUTTON = [By.XPATH, "//*[text()='Лента Заказов']/parent::a"]
    LIST_BUN_INGREDIENTS = [By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]"]
    INGREDIENT_NAME_WITH_OPEN_WINDOW = [By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]/div/div/p"]
    CLOSE_OPENED_WINDOW_INGREDIENT_DETAILS = [By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button"]
    TITTLE_INGREDIENT_DETAILS = [By.XPATH, "//div[contains(@class,'Modal_modal__contentBox')]"]

    COUNTER_INGREDIENT = [By.XPATH, "//*[contains(@class, 'counter_counter__num')]"]
    CART_WITN_INGREDIENTS = [By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]"]
    ORDER_BUTTON = [By.XPATH, "//button[contains(text(), 'Оформить заказ')]"]
    ORDER_STATUS = [By.XPATH, "//*[contains(@class, 'Modal_modal__text')]/p[1]"]

    TITTLE_ORDER_NUMBER_IN_OPENED_WINDOW = [By.XPATH, "//h2[contains(@class,'title_shadow')]"]