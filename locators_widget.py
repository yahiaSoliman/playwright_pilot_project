from selenium.webdriver.common.by import By


class WidgetLocators:
    first_row_check_box = (By.XPATH, "//*[@aria-label='Select row']")
    open_commands_group = (By.XPATH, "//button[@aria-label='Open']")
    open_in_table_command = (By.ID, "open_in_table")
    open_in_details_command = (By.ID, "open_in_details")
    open_in_structure_command = (By.ID, "open_in_structure")
    open_in_navigator_command = (By.ID, "show_navigator")
    open_in_kanban_command = (By.ID, "open_type_with_kanban_view")
    open_in_timeline_command = (By.ID, "open_in_timeline")
    open_in_history_command = (By.ID, "open-in-history")
    open_in_chart_command = (By.XPATH, "//span[text()='Open In Chart']")
    open_in_viewer_command = (By.XPATH, "//span[text()='Open In Viewer']")
    open_in_comparison_command = (By.XPATH, "//span[text()='Open In Comparison']")

    revise_command = (By.XPATH, "//span[@aria-label='Revise']")
    relations_icon = (By.XPATH, "//p[text()='Relations']/preceding-sibling::li")
    version_B_object_in_revision_tab_of_relations_pane = (By.XPATH, "//td[contains(normalize-space(),'(B)')]")
    revise_command_confirmation_message = (By.XPATH, "//*[contains(text(),'has been successfully revised')]")

    second_opened_widget_title_A = (By.XPATH, "(//div[@class='card-header'])[2]/descendant::span")
    second_opened_widget_title_B = (By.XPATH, "(//div[@class='card-header'])[2]/descendant::div")
    second_widget_row = (By.XPATH, "(//div[@class='card-header'])[2]/following::tbody[3]/tr")
    second_widget_first_object_name = (By.XPATH, "(//div[@class='card-header'])[2]/following::tbody[3]/tr/td[3]/div/div")


