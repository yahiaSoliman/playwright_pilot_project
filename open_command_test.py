from baseClass import BaseClass
from data import Data
from endpoints import EndPoints
from interactions_compound import CompoundInteractions
from interactions_single import SingleInteractions


class TableWidget(BaseClass):
    """
    ITEMS TO BE DROPPED TO THE TABLE
    CLEAN DASHBOARD
    AT LEAST ONE TAB IS OPENED
    Tab is empty from any widgets
    default toolbar mode is comfortable
    """

    def setUp(self):
        super().setUp()
        # close all tabs of the active dashboard
        token = EndPoints.login(Data.url_staging_qa_api, Data.staging_qa_user_01).json()['data']['token']
        layout = EndPoints.get_layout(token, Data.url_staging_qa_api)
        app_id = layout['app_id']
        active_dashboard_id = None

        for x in layout['layout']:
            if x['isActive']:
                active_dashboard_id = x['id']
                break
        if active_dashboard_id is None:
            print("no active dashboard")
        EndPoints.close_all_tabs(token, app_id, active_dashboard_id, Data.url_staging_qa_api)

        # open commands group of open menu
        CompoundInteractions.login(self.driver, Data.url_staging_qa_ui, Data.username, Data.password)
        SingleInteractions.click_side_menu_table_icon(self.driver)
        SingleInteractions.insert_search_query(self.driver, "banana06")

        SingleInteractions.drag_drop_search_result_first_item(self.driver)
        self.assertTrue(SingleInteractions.is_table_first_raw_displayed(self.driver))
        SingleInteractions.wait_for_check_box_of_first_row_in_table_widget_to_be_displayed(self.driver)
        SingleInteractions.click_on_check_box_of_first_row_in_table_widget(self.driver)
        SingleInteractions.click_open_commands_group(self.driver)

    def test_01_open_in_details(self):
        SingleInteractions.click_open_in_details(self.driver)
        SingleInteractions.wait_for_text_in_second_opened_widget_title_a(self.driver, "Details")