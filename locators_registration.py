from selenium.webdriver.common.by import By


class RegistrationLocators:
    """
    Registration UI elements' selectors
    """
    email_input_text = (By.XPATH, "//input[@type='email']")
    new_account_password = (By.XPATH, "//input[@type='password']")
    register_button = (By.XPATH, "//button[text()='Register']")
    otp_input_text = (By.XPATH, "//input[@placeholder='Verification code']")
    verify_button = (By.XPATH, "//button[text()='Verify']")
    first_name_input_text = (By.XPATH, "//input[@placeholder='First name']")
    last_name_input_text = (By.XPATH, "//input[@placeholder='Last name']")
    domain_input_text = (By.XPATH, "//input[@placeholder='Domain name']")
    domain_confirmation_icon = (By.CSS_SELECTOR, "[aria-label='This domain name is available']")
    create_tenant_button = (By.XPATH, "//button[text()='Create Tenant']")
