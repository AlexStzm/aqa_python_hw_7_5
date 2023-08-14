import os
from selene import browser, have


def test_practice_form():
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')

    browser.element('#firstName').type('FirstName')
    browser.element('#lastName').type('LastName')
    browser.element('#userEmail').type('test@test.com')
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('9999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select>[value="1991"]').click()
    browser.element('.react-datepicker__month-select>[value="10"]').click()
    browser.element('.react-datepicker__day--015').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter().type('Maths').press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/test_picture.JPG'))
    browser.element('#currentAddress').type('User test address')
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text(
        'Thanks for submitting the form'))
    browser.element('.table').should(have.text('FirstName LastName')
        .and_(have.text('test@test.com'))
        .and_(have.text('Male'))
        .and_(have.text('9999999999'))
        .and_(have.text('15 November,1991'))
        .and_(have.text('Computer Science, Maths'))
        .and_(have.text('Sports, Reading'))
        .and_(have.text('test_picture.JPG'))
        .and_(have.text('User test address'))
        .and_(have.text('NCR Delhi')))