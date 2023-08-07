from selene import browser, have
from selenium.webdriver import Keys


def test_practice_form():
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')
    browser.element('#firstName').type('FirstName')
    browser.element('#lastName').type('LastName')
    browser.element('#userEmail').type('test@test.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('9999999999')
    browser.element('#dateOfBirthInput').type(Keys.CONTROL + 'A' + Keys.NULL + '15.nov.1991').press_enter()
    browser.element('#subjectsInput').type('test')
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys('C:/test.txt')
    browser.element('#currentAddress').type('User test address')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text(
        'Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text(
        'FirstName LastName' and
        'test@test.com' and 'Male' and
        '9999999999' and '15 November,1991' and
        'Sports, Reading' and 'test.txt' and
        'User test address' and 'NCR Delhi'))