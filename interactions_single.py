import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

from locators_object_type_icon import ObjectTypeIconLocators
from locators_registration import RegistrationLocators
from locators_uncategorized import UncategorizedLocators
from locators_widget import WidgetLocators


class SingleInteractions:
    """
    Login

    """

    @staticmethod
    def insert_login_username(driver, username):
        driver.find_element(*UncategorizedLocators.login_username).send_keys(username)

    @staticmethod
    def insert_login_password(driver, password):
        driver.find_element(*UncategorizedLocators.login_password).send_keys(password)

    @staticmethod
    def click_login(driver):
        driver.find_element(*UncategorizedLocators.login_button).click()

    """
    Header
    
    """

    @staticmethod
    def is_search_input_text_displayed(driver):
        return driver.find_element(*UncategorizedLocators.search_input_text).is_displayed()

    @staticmethod
    def is_demo_dashboard_title_displayed(driver):
        return driver.find_element(*UncategorizedLocators.demo_dashboard_title).is_displayed()

    @staticmethod
    def wait_for_active_workspace_name_to_be_displayed(driver):
        WebDriverWait(driver, 60).until(
            expected_conditions.visibility_of_element_located(UncategorizedLocators.active_workspace))

    """
    Registration Page
    
    """

    @staticmethod
    def click_create_new_account_button(driver):
        driver.find_element(*UncategorizedLocators.create_account_button).click()

    @staticmethod
    def insert_unregistered_email_address(driver, email_address):
        driver.find_element(*RegistrationLocators.email_input_text).send_keys(email_address)

    @staticmethod
    def insert_new_account_password(driver, password):
        driver.find_element(*RegistrationLocators.new_account_password).send_keys(password)

    @staticmethod
    def click_register_button(driver):
        driver.find_element(*RegistrationLocators.register_button).click()

    @staticmethod
    def insert_otp(driver, otp):
        driver.find_element(*RegistrationLocators.otp_input_text).send_keys(otp)

    @staticmethod
    def click_verify_button(driver):
        driver.find_element(*RegistrationLocators.verify_button).click()

    @staticmethod
    def insert_first_name(driver, first_name):
        driver.find_element(*RegistrationLocators.first_name_input_text).send_keys(first_name)

    @staticmethod
    def insert_last_name(driver, last_name):
        driver.find_element(*RegistrationLocators.last_name_input_text).send_keys(last_name)

    @staticmethod
    def insert_domain(driver, domain):
        driver.find_element(*RegistrationLocators.domain_input_text).send_keys(domain)

    @staticmethod
    def find_domain_confirmation_icon(driver):
        driver.find_element(*RegistrationLocators.domain_confirmation_icon)

    @staticmethod
    def click_create_tenant(driver):
        driver.find_element(*RegistrationLocators.create_tenant_button).click()

    """
    Side Menu
    
    """

    @staticmethod
    def click_side_menu_table_icon(driver):
        time.sleep(5)
        driver.find_element(*UncategorizedLocators.side_menu_table_icon).click()

    """
    Search
    """

    @staticmethod
    def insert_search_query(driver, search_query):
        time.sleep(3)
        driver.find_element(*UncategorizedLocators.search_input_text).send_keys(search_query)

    @staticmethod
    def drag_drop_search_result_first_item(driver):
        time.sleep(5)
        source = driver.find_element(*UncategorizedLocators.search_result_item)
        target = driver.find_element(*UncategorizedLocators.table_draggable_area)
        drag_and_drop(driver, source, target)
        time.sleep(5)

    @staticmethod
    def get_text_of_first_item(driver):
        return driver.find_element(*UncategorizedLocators.search_result_item).get_attribute("textContent")

    @staticmethod
    def find_search_result_summary_container(driver):
        driver.find_element(*UncategorizedLocators.search_result_summary_items_list_container)

    @staticmethod
    def click_see_all_data_button(driver):
        driver.find_element(*UncategorizedLocators.see_all_search_results_data_button).click()

    @staticmethod
    def click_filter_icon(driver):
        driver.find_element(*UncategorizedLocators.filter_icon).click()

    @staticmethod
    def click_type_filter_input_box(driver):
        driver.find_element(*UncategorizedLocators.type_filter_input).click()

    @staticmethod
    def find_typs_list_container(driver):
        driver.find_element(*UncategorizedLocators.list_of_types_container)

    @staticmethod
    def insert_value_into_type_filter_box(driver, type_value):
        driver.find_element(*UncategorizedLocators.type_filter_input).send_keys(type_value)
        time.sleep(3)

    @staticmethod
    def click_enter_on_type_filter_box(driver):
        driver.find_element(*UncategorizedLocators.type_filter_input).send_keys(Keys.ENTER)
        time.sleep(3)

    @staticmethod
    def click_search_button(driver):
        driver.find_element(*UncategorizedLocators.search_button).click()
        time.sleep(8)  # wait for list to be filtered

    """
    Table
    """

    @staticmethod
    def is_table_first_raw_displayed(driver):
        return driver.find_element(*UncategorizedLocators.table_first_row).is_displayed()

    @staticmethod
    def is_table_column_name_title_displayed(driver):
        return driver.find_element(*UncategorizedLocators.table_name_column_title).is_displayed()

    @staticmethod
    def get_list_of_table_items_types(driver):
        return driver.find_elements(*UncategorizedLocators.table_item_types)

    """
    Create Menu
    """

    @staticmethod
    def click_create_object(driver):
        driver.find_element(*UncategorizedLocators.create_object_plus_icon).click()

    @staticmethod
    def insert_text_into_create_menu_search_box(driver, text):
        driver.find_element(*ObjectTypeIconLocators.create_menu_search_input_box).send_keys(text)

    @staticmethod
    def click_item_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_item_icon).click()

    @staticmethod
    def click_task_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_task_icon).click()

    @staticmethod
    def click_category_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_category_icon).click()

    @staticmethod
    def click_document_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_document_icon).click()

    @staticmethod
    def click_idea_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_idea_icon).click()

    @staticmethod
    def click_cost_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_cost_icon).click()

    @staticmethod
    def click_issue_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_issue_icon).click()

    @staticmethod
    def click_node_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_node_icon).click()

    @staticmethod
    def click_company_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_company_icon).click()

    @staticmethod
    def click_impact_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_impact_icon).click()

    @staticmethod
    def click_deviation_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_deviation_icon).click()

    @staticmethod
    def click_change_order_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_change_order_icon).click()

    @staticmethod
    def click_change_request_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_change_request_icon).click()

    @staticmethod
    def click_change_task_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_change_task_icon).click()

    @staticmethod
    def click_implementation_plan_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_implementation_plan_icon).click()

    @staticmethod
    def click_material_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_material_icon).click()

    @staticmethod
    def click_milestone_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_milestone_icon).click()

    @staticmethod
    def click_node_template_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_node_template_icon).click()

    @staticmethod
    def click_organization_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_organization_icon).click()

    @staticmethod
    def click_phase_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_phase_icon).click()

    @staticmethod
    def click_problem_report_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_problem_report).click()

    @staticmethod
    def click_product_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_product_icon).click()

    @staticmethod
    def click_program_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_program_icon).click()

    @staticmethod
    def click_project_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_project_icon).click()

    @staticmethod
    def click_requirement_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_requirement_icon).click()

    @staticmethod
    def click_risk_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_risk_icon).click()

    @staticmethod
    def click_workflow_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_workflow_icon).click()

    @staticmethod
    def click_workflow_template_icon(driver):
        driver.find_element(*ObjectTypeIconLocators.create_workflow_template_icon).click()

    """
    Object Creation Window
    """

    @staticmethod
    def insert_object_name(driver, text):
        e = driver.find_element(*UncategorizedLocators.item_name_input_box)
        e.send_keys(text)

    @staticmethod
    def click_finish_creating_object(driver):
        time.sleep(3)
        driver.find_element(*UncategorizedLocators.finish_creating_object_button).click()

    @staticmethod
    def upload_document_file(driver, file_path):
        driver.find_element(*UncategorizedLocators.document_file_upload).send_keys(file_path)

    """
    Footer
    """

    @staticmethod
    def wait_for_object_creation_confirmation_to_be_displayed(driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                UncategorizedLocators.object_creation_confirmation_message))

    @staticmethod
    def wait_for_check_box_of_first_row_in_table_widget_to_be_displayed(driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(WidgetLocators.first_row_check_box))

    @staticmethod
    def click_on_check_box_of_first_row_in_table_widget(driver):
        driver.find_element(*WidgetLocators.first_row_check_box).click()

    @staticmethod
    def click_open_commands_group(driver):
        driver.find_element(*WidgetLocators.open_commands_group).click()
        time.sleep(2)

    @staticmethod
    def click_revise_command(driver):
        driver.find_element(*WidgetLocators.revise_command).click()

    @staticmethod
    def click_relations_icon(driver):
        driver.find_element(*WidgetLocators.relations_icon).click()

    @staticmethod
    def get_full_name_of_revision_b_object(driver):
        return driver.find_element(*WidgetLocators.version_B_object_in_revision_tab_of_relations_pane).get_attribute(
            "textContent")

    @staticmethod
    def wait_for_version_b_object_to_be_displayed(driver):
        WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(
                WidgetLocators.version_B_object_in_revision_tab_of_relations_pane))

    @staticmethod
    def wait_for_revise_confirmation_message(driver):
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(WidgetLocators.revise_command_confirmation_message))

    @staticmethod
    def click_open_in_table(driver):
        driver.find_element(*WidgetLocators.open_in_table_command).click()

    @staticmethod
    def click_open_in_details(driver):
        driver.find_element(*WidgetLocators.open_in_details_command).click()

    @staticmethod
    def click_open_in_structure(driver):
        driver.find_element(*WidgetLocators.open_in_structure_command).click()

    @staticmethod
    def click_open_in_navigator(driver):
        driver.find_element(*WidgetLocators.open_in_navigator_command).click()

    @staticmethod
    def click_open_in_kanban(driver):
        driver.find_element(*WidgetLocators.open_in_kanban_command).click()

    @staticmethod
    def click_open_in_timeline(driver):
        driver.find_element(*WidgetLocators.open_in_timeline_command).click()

    @staticmethod
    def click_open_in_history(driver):
        driver.find_element(*WidgetLocators.open_in_history_command).click()

    @staticmethod
    def click_open_in_chart(driver):
        driver.find_element(*WidgetLocators.open_in_chart_command).click()

    @staticmethod
    def click_open_in_viewer(driver):
        driver.find_element(*WidgetLocators.open_in_viewer_command).click()

    @staticmethod
    def click_open_in_comparison(driver):
        driver.find_element(*WidgetLocators.open_in_comparison_command).click()

    @staticmethod
    def find_all_rows_of_second_widget(driver):
        return driver.find_elements(*WidgetLocators.second_widget_row)

    @staticmethod
    def get_second_widget_first_row_text_content(driver):
        return driver.find_element(*WidgetLocators.second_widget_first_object_name).get_attribute("textContent")

    @staticmethod
    def wait_for_text_in_second_opened_widget_title_a(driver, text):
        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(
                WidgetLocators.second_opened_widget_title_A, text))

    @staticmethod
    def wait_for_text_in_second_opened_widget_title_b(driver, text):
        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(
                WidgetLocators.second_opened_widget_title_B, text))
