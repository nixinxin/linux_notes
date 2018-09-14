import time
import json
import requests
from pyquery import PyQuery
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

username = 'nixingguo'
password = 'mwteckmwteck'
quchu = "导入-"


class TitidaAdmin(object):
    main_url = "http://admin.maintenance.ettda.com/#/login"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 30)
        self.basic_page_open = False
        self.control = False
        self.market_manage = False
        self.token = ''

    def login(self, username, password):
        self.driver.get(self.main_url)
        self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#login > div.main > div.login-title")))

        username_input = self.driver.find_element_by_css_selector(
            "#login > div.main > div.content > form > div:nth-child(1) > div > div > input")
        username_input.clear()
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_css_selector(
            "#login > div.main > div.content > form > div:nth-child(2) > div > div > input")
        password_input.clear()
        password_input.send_keys(password)

        self.driver.find_element_by_css_selector("#login > div.main > div.content > form > button > span").click()
        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                    "#homePage > div.sidebar > div.main-nav > aside > div > div > ul > div > li:nth-child(1) > div > span")))

        self.token = self.driver.execute_script('return window.sessionStorage["userToken"]')

    def access_projects_page(self):
        if self.basic_page_open is False:
            self.driver.find_element_by_css_selector(
                "#homePage > div.sidebar > div.main-nav > aside > div > div > ul > div > li:nth-child(1) > div > span").click()
            self.basic_page_open = True

        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                    "#homePage > div.sidebar > div.main-nav > aside > div > div > ul > div > li.el-submenu.is-opened > ul > a:nth-child(2)")))
        self.driver.find_element_by_css_selector(
            "#homePage > div.sidebar > div.main-nav > aside > div > div > ul > div > li.el-submenu.is-opened > ul > a:nth-child(2) > li > span").click()

        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                    "#projectFile > div:nth-child(2) > div.panel-body > div.body-box > div > div:nth-child(3) > div.el-col.el-col-8 > div > div > button")))

    def query_project_by_browser(self, project):
        self.input_text("#projectFile > div:nth-child(2) > div.panel-body > div.body-box > div > div:nth-child(3) > div.el-col.el-col-8 > div > input", project)
        time.sleep(0.5)
        self.driver.find_element_by_css_selector(
            "#projectFile > div:nth-child(2) > div.panel-body > div.body-box > div > div:nth-child(3) > div.el-col.el-col-8 > div > div > button").click()
        self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                        '#projectFile > div:nth-child(3) > div.panel-body > div.page-box > div > div > span.el-pagination__total')))

        self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR,
                                                        '.el-table__row')))

        time.sleep(0.5)

    def query_project_by_moni(self, project):

        url = "http://v3m2.api.2012iot.com/api-admin/project/toList"

        querystring = {"client_type": "web", "pageSize": "10", "page": "1",
                       "projectName": project, "province": "", "city": "", "country": ""}

        headers = {
            'tokenStr': self.token,
        }

        response = requests.request("GET", url, headers=headers, params=querystring).text
        response = json.loads(response)['obj']
        if response['totalCount'] == 1:
            for item in response['result']:
                projectName = item['projectName']
                areaName = item['areaName']
                return projectName, areaName
        return None

    def modify_projects(self, project):
        self.query_project_by_browser(project)
        page_html = self.driver.page_source
        all_items = PyQuery(page_html).find(".el-table__row").length
        if all_items == 1:
            num = 1
            try:
                project_names = self.driver.find_element_by_css_selector("tr.el-table__row:nth-child({}) > td.el-table_1_column_3.is-center > div".format(num)).text
                if "导入-" in project_names:
                    project_name = project_names.replace("导入-", '')
                    self.driver.find_element_by_css_selector(
                        "tr.el-table__row:nth-child({}) > td.el-table_1_column_6.is-center > div > button.el-button.el-button--primary.el-button--small".format(
                            num)).click()
                    time.sleep(0.5)
                    self.wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#projectFile > div:nth-child(6) > div > div.el-dialog__footer > div > button.el-button.el-button--default")))
                    self.input_text("#projectFile > div:nth-child(6) > div > div.el-dialog__body > form > div:nth-child(1) > div > div > div > div > input", project_name)
                    time.sleep(0.5)
                    self.driver.find_element_by_css_selector("#projectFile > div:nth-child(6) > div > div.el-dialog__footer > div > button.el-button.el-button--success").click()
                    time.sleep(0.5)
                    print(project_names, project_name)
            except Exception as e:
                print(e)
                assert input()

    def input_text(self, locator, text):
        option = self.driver.find_element_by_css_selector(locator)
        option.clear()
        option.send_keys(text)

    def access_elevator_page(self):
        if self.basic_page_open is False:
            self.driver.find_element_by_css_selector(
                "#homePage > div.sidebar > div.main-nav > aside > div > div > ul > div > li:nth-child(1) > div > span").click()
            self.basic_page_open = True
        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                    "#homePage > div.sidebar > div.main-nav > aside > div > div > ul > div > li.el-submenu.is-opened > ul > a:nth-child(1)")))

        self.driver.find_element_by_css_selector(
            "#homePage > div.sidebar > div.main-nav > aside > div > div > ul > div > li.el-submenu.is-opened > ul > a:nth-child(1) > li > span").click()

        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                    "#elevatorFile > div.btnGroup > div > button:nth-child(1) > span")))
        return self.driver

    def add_elevator_info(self):
        self.driver_elevator = self.access_elevator_page()
        self.driver_elevator.find_element_by_css_selector("#elevatorFile > div.btnGroup > div > button:nth-child(1) > span").click()
        time.sleep(3)

        # 插入电梯详细信息

        self.driver_elevator.find_element_by_css_selector("#elevatorFile > div:nth-child(7) > div > div.el-dialog__footer > div > button.el-button.el-button--default").click()

    def query_elevator_by_moni(self):
        pass

    def read_json(self):
        with open('projects.json', 'r', encoding='utf-8') as f:
            datas = json.loads(f.read())
            return datas

    def close(self):
        self.driver.close()


zhixing = TitidaAdmin()
zhixing.login(username, password)
result = zhixing.query_project_by_moni('紫檀二期')
print(result)
zhixing.close()



