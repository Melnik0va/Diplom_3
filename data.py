class URLS: 
    BASE_URL ='https://stellarburgers.education-services.ru/'
    CREATE_USER = BASE_URL + 'api/auth/register'
    DELETE_USER = BASE_URL + 'api/auth/user'
    LOGIN_USER = BASE_URL + 'api/auth/login'

    LOGIN_URL = BASE_URL + 'login'
    PROFILE_URL = BASE_URL + 'account/profile'
    ORDERS_HISTORY = BASE_URL + 'account/order-history'
    FORGOT_PASSWORD = BASE_URL + 'forgot-password'
    RESET_URL = BASE_URL + 'reset-password'
    ORDER_FEED_URL = BASE_URL + 'feed'

    ACCOUNT_URL = BASE_URL + 'account'

class Browser: 
    Firefox = 'Firefox'
    Chrome = 'Chrome'



TIMEOUT = 10
