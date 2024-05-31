Feature: behave qa demo

  Scenario Outline: Search country
    Given I login to the test page
    When I search for "<country>"
    Then i will see "<country>" selected


    Examples:
      | country              |
      | Mexico               |
      | United States        |
      | Argentina            |


  Scenario: Dropdown select
    Given I login to the test page
    When I select option 2 from the dropdown
    And I change the selection to Option 3
    Then i will see Option 3 selected



  Scenario Outline: new window handle
    Given I login to the test page
    When I open a new window
    Then I assert the "<text>" is present

        Examples:
      | text              |
      | 30 DAY MONEY BACK GUARANTEE|
      | SELF PACED ONLINE TRAINING|

  Scenario: new tab handle
    Given I login to the test page
    When I open a new tab
    Then I assert a button

  Scenario: Alerts
    Given I login to the test page
    When I type "QA Card"
    And I click the Alert button
    And I click the Confirm button
    Then I assert the alert is correct


  Scenario: table navigation
    Given I login to the test page
    When I search for $25, and $15 courses
    Then I print them
