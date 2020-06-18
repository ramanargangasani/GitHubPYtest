'''
def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )
'''

import pytest


from selenium import webdriver

# driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup_initialization(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path='C:\\ChromeDriver\\chromedriver.exe')

    elif browser_name == "firefox":
        # driver = webdriver.Chrome(executable_path='C:\\ChromeDriver\\firefoxdriver.exe')
        print("Download FireFox driver")
    else:
        # driver = webdriver.Chrome(executable_path='C:\\ChromeDriver\\IEdriver.exe')
        print("Download I.E driver")

    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver   # driver declaring local i.e environment variable
    yield
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
        '''
           Extends the PyTest plugin to take and embed screenshot in html report, whenever test fails.
          '''
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == 'setup':
            xfail = hasattr(report, 'wasxfail')
            if(report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_")+".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt ="screenshot" style="width:304px;height:228px;" ' \
                         ' onclick="window.open(this.src)" align ="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)



