from selenium.webdriver.common.by import By


class ObjectTypeIconLocators:

    """
    create menu UI elements' selectors
    """
    create_menu_search_input_box = (By.XPATH, "(//input[@placeholder='Search'])[2]")
    create_item_icon = (By.ID, "tasks-create-menu-create-item")
    create_task_icon = (By.ID, "tasks-create-menu-create-task")
    create_category_icon = (By.ID, "tasks-create-menu-create-category")
    create_document_icon = (By.ID, "tasks-create-menu-create-document")
    create_idea_icon = (By.ID, "tasks-create-menu-create-idea")
    create_cost_icon = (By.ID, "tasks-create-menu-create-cost")
    create_issue_icon = (By.ID, "tasks-create-menu-create-Issue")
    create_node_icon = (By.ID, "tasks-create-menu-create-node")
    create_company_icon = (By.ID, "tasks-create-menu-create-company")
    create_impact_icon = (By.ID, "tasks-create-menu-create-impact")
    create_deviation_icon = (By.ID, "tasks-create-menu-create-deviation")
    create_change_order_icon = (By.ID, "tasks-create-menu-create-change_order")
    create_change_request_icon = (By.ID, "tasks-create-menu-create-change_request")
    create_change_task_icon = (By.ID, "tasks-create-menu-create-change_task")
    create_implementation_plan_icon = (By.ID, "tasks-create-menu-create-implementation_plan")
    create_material_icon = (By.ID, "tasks-create-menu-create-material")
    create_milestone_icon = (By.ID, "tasks-create-menu-create-milestone")
    create_node_template_icon = (By.ID, "tasks-create-menu-create-node_template")
    create_organization_icon = (By.ID, "tasks-create-menu-create-organization")
    create_phase_icon = (By.ID, "tasks-create-menu-create-phase")
    create_problem_report = (By.ID, "tasks-create-menu-create-problem_report")
    create_product_icon = (By.ID, "tasks-create-menu-create-product")
    create_program_icon = (By.ID, "tasks-create-menu-create-program")
    create_project_icon = (By.ID, "tasks-create-menu-create-project")
    create_requirement_icon = (By.ID, "tasks-create-menu-create-requirement")
    create_risk_icon = (By.ID, "tasks-create-menu-create-risk")
    create_workflow_icon = (By.ID, "tasks-create-menu-create-workflow")
    create_workflow_template_icon = (By.ID, "tasks-create-menu-create-workflow_template")