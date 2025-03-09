from selenium.webdriver.common.by import By


class ProductsPageLocators:
    PRODUCT_SEARCH = (By.CSS_SELECTOR, 'div.col-sm-4:nth-of-type(4) div.productinfo p')
    VIEW_PRODUCT_BUTTON = (By.CSS_SELECTOR, '[href="/product_details/3"]')
    WRITE_YOUR_REVIEW = (By.CSS_SELECTOR, '[data-toggle="tab"]')
    NAME_FIELD = (By.CSS_SELECTOR, '#name')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#email')
    REVIEW_FIELD = (By.CSS_SELECTOR, '#review')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#button-review')
    SUCCESS_REVIEW_ALERT = (By.CSS_SELECTOR, '.alert-success span')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[data-product-id="3"]')
    SUCCESS_ADDED_ALERT = (By.CSS_SELECTOR, '.modal-body :first-child.text-center')
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, '[href="/view_cart"] u')
