from selenium.webdriver.common.by import By


class UncategorizedLocators:
    """
    login page UI elements' selectors
    """
    login_username = (By.NAME, "username")
    login_password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    create_account_button = (By.XPATH, "//span[text()='Create an account']")

    """
    Search UI elements
    """
    search_button = (By.XPATH, "//span[text()='Search']")
    search_result_item = (By.XPATH, "//div[@class='ndt']")
    filter_icon = (By.ID, "tasks-advanced-search")
    see_all_search_results_data_button = (By.XPATH, "//span[text()='See All Data ']")
    type_filter_input = (By.XPATH, "//input[@placeholder='Type']")
    list_of_types_container = (By.XPATH, "//div[@aria-label='Items']")

    """
    Tab UI elements' selectors
    """
    object_creation_confirmation_message = (By.XPATH, "//*[contains(text(),'has been successfully created')]")
    table_first_row = (By.XPATH, "//table/tbody/tr")
    table_name_column_title = (By.XPATH, "//div[@role='presentation' and text()='Name']")
    search_result_summary_items_list_container = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding css-1ontqvh']")
    table_item_types = (By.XPATH, "//tbody/tr/td[8]")
    table_draggable_area = (By.XPATH, "//div[@class='dragWrapper']")

    """
    Side Menu UI elements' selectors
    """
    side_menu_table_icon = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding css-inu1m2']/li[2]")

    """
    Header
    """
    active_workspace = (By.XPATH, "//div[@aria-label='Active Workspace']/div")
    create_object_plus_icon = (By.ID, "tasks-create-menu")
    search_input_text = (By.XPATH, "//input[@placeholder='Search']")
    demo_dashboard_title = (By.XPATH, "//div[text()='Demo Dashboard']")
    new_workspace_button = (By.XPATH, "//div[text()='New Workspace']")

    """
    object creation window UI elements' selectors
    """
    item_name_input_box = (By.XPATH, "//p[text()='Name']/following::input")
    document_file_upload = (By.XPATH, "(//input[@type='file'])[2]")
    finish_creating_object_button = (By.XPATH, "//div[text()='CREATE']")
