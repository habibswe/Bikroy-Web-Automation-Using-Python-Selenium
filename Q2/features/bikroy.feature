Feature: bikroy website navigation

#senario number 1
  Scenario: navigate to bikroy home page
    Given launch chrome browser
    Then verify that the logo is present on the page

#senario number 2
  Scenario: search item in homepage
    Given launch chrome browser
    When search box write cycle
    Then click on search

#senario number 3

  Scenario: navigate to bikroy login and database
    Given launch chrome browser
    Then Click on login
    When click on continue with email
    Then enter email
    When type password
    Then Click login button

#senario number 4
# Browse items by category(mobiles)
  Scenario: Browse items by category
    Given launch chrome browser
    When click on mobiles
    Then search mobile model
    When click on search icon

# Browse items by category(electronics)
    Given launch chrome browser
    When click on electronics
    Then search electronics model
    When click on search icon

# Browse items by category(vehicles)
    Given launch chrome browser
    When click on vehicles
    Then search vehicles model
    When click on search icon

    # Browse items by category(Property)
    Given launch chrome browser
    When click on Property
    Then search Property details
    When click on search icon

    # Browse items by category(home & living)
    Given launch chrome browser
    When click on home_and_living
    Then search home_and_living
    When click on search icon

    # Browse items by category(pets_and_animals)
    Given launch chrome browser
    When click on pets_and_animals
    Then search pets_and_animals
    When click on search icon

    # Browse items by category(mens_fashion_and_grooming)
    Given launch chrome browser
    When click on mens_fashion_and_grooming
    Then search mens_fashion_and_grooming items
    When click on search icon

    # Browse items by category(Women's fashion  beauty)
    Given launch chrome browser
    When click on Womens fashion beauty
    Then search Womens fashion beauty items
    When click on search icon

    # Browse items by category(hobbies_sports_and_kids)
    Given launch chrome browser
    When click on hobbies,sports and kids
    Then search hobbies,sports and kids items
    When click on search icon

    # Browse items by category(business & industry)
    Given launch chrome browser
    When click on business and industry
    Then search business and industry model
    When click on search icon

    # Browse items by category(essentials)
    Given launch chrome browser
    When click on essentials
    Then search essentials items
    When click on search icon

    # Browse items by category(education)
    Given launch chrome browser
    When click on education
    Then search education organization
    When click on search icon
#
    # Browse items by category(services)
    Given launch chrome browser
    When click on services
    Then search services items
    When click on search icon

    # Browse items by category(jobs)
    Given launch chrome browser
    When click on jobs
    Then search jobs
    When click on search icon

    # Browse items by category(agriculture)
    Given launch chrome browser
    When click on agriculture
    Then search agriculture items
    When click on search icon

    # Browse items by category(overseas jobs)
    Given launch chrome browser
    When click on overseas jobs
    Then search overseas jobs
    When click on search icon

#senario number 5
  Scenario: navigate to bikroy all ads page
    Given launch chrome browser
    Then Click on all ads
    When click on select location
    Then click on dhaka
    When click on mirpur
    Then select sort results by box
    When select newest on top
    Then select urgent
    When select type of poster All
    Then click on mobiles
    When click on mobilePhones
    Then search apple in search box
    When click on search button

#senario number 6
  Scenario: navigate to bikroy all ads page
    Given launch chrome browser
    Then Click on all ads
    When click on select location
    Then click on dhaka
    When click on mirpur
    Then select sort results by box
    When select newest on top
    Then select urgent
    When select type of poster All
    Then click on electronics
    When click on laptops
    Then search asus in search box
    When click on search button


#senario number 7
  Scenario: navigate to bikroy all ads page
    Given launch chrome browser
    Then Click on all ads
    When click on select location
    Then click on dhaka
    When click on mirpur
    Then select sort results by box
    When select newest on top
    Then select urgent
    When select type of poster All
    Then click on vehicles
    When click on motorbikes
    Then search rtr 4v in search box
    When click on search button

#senario number 8
  Scenario: navigate to bikroy language change page
    Given launch chrome browser
    Then Click on bangla

#senario number 9
  Scenario: navigate to bikroy about page
    Given launch chrome browser
    Then Click on about us
    When sent massage on email

#senario number 10
  Scenario: navigate to bikroy jobs
    Given launch chrome browser
    Then Click explore more
    When click on view all jobs
    Then click on search box write computer
    When click on search

#senario number 11

  Scenario: navigate to bikroy login and database
    Given launch chrome browser
    Then Click on login
    When click on continue with email
    Then enter email
    When type password
    Then Click login button
#senario number 12
#navigate to bikroy account database
    Then Click on My account
    When click on profile database
#senario number 11
  Scenario: navigate to bikroy login and database
    Given launch chrome browser
    Then Click on login
    When click on continue with email
    Then enter email
    When type password
    Then Click login button
    Then Click on My account
    When click on profile database
#senario number 13
  Scenario: navigate to bikroy logout
    Given launch chrome browser
    Then Click on login
    When click on continue with email
    Then enter email
    When type password
    Then Click login button
    Then Click on My account
    When click on setting
    Then click on logout
