
Name: Register User
Number: 1
Description: A prospective user wants to register as a Fyre Sale user
Priority: High
Author: Gissur Már
Source: Nr 1 in requirements
Actors: prospective seller or buyer 
Precondition: User does not already exist 
Postcondition: User is created and can now make bids on items or adding new items up for auction.
Trigger: A prospective user has an item he wishes to auction or desires to make a bid on a item that has been listed for auction
Main success scenario: 
    1. prospective user clicks on the "Sign up button"
    2. prospective user fills out the email for the new account
    3. prospective user fills out the username for the new account
    4. prospective user fills out the rest of the form to create the account
    5. prospective user receives a confirmation email wich he validates
    5. user logs into account with chosen username and password
Extensions:
    2.a. A user with given email already exists 
    3.a. A user with the chosen username aldready exists



Name: Log in user
Number: 2
Description: Existing user logs in to Fyre Sale
Priority: High
Author: Gissur Már
Source: Nr 2 in requirements
Actors: seller or buyer
Precondition: User already exists 
Postcondition: User is logged in
Trigger: User wants to make a bid, review a bid or put a new item up for auction
Main success scenario:
    1. User clicks the "Log in" button
    2. User enters his username and password and submits
    3. User is now logged in
Extensions:
    2.a User enters incorrect username or password


Name: Seller checks his rating
Number: 3
Description: seller checks his rating in his user profile
Priority: Medium
Author: Gissur Már
Source: Nr 3 in requirements
Actors: Seller 
Precondition: Seller has been rated by a buyer
Postcondition: User can take actions to either preserve his rating or get a better rating
Trigger: User wants to check if he has a good rating. 
Main success scenario: 
    1. user clicks on his profile image to access his user information
    1. user sees his rating listed
Extensions:
    1.a. User is not logged in see use case 2
    2.a. User has not received a rating from a buyer and does not have a rating


Name: Buyer checks seller rating
Number: 4
Description: Buyer intends to make a bid on an item and wishes to assess the sellers reliablility
Priority: Medium
Author: Gissur Már 
Source: Nr 3 in requirements
Actors: Buyer
Precondition: Seller has been rated by a buyer
Postcondition: Buyer can decide if seller is reliable considered his rating.
Trigger: A buyer intends to make a bid and wants to assess the seller
Main success scenario:
    1. Buyer clicks on the seller profile
    2. Buyer sees the seller rating
Extensions:
    2.a. Seller has not yet received a rating from a buyer



Name: Log out user
Number: 5
Description: User logs out to close his session
Priority: High
Author: Gissur Már Jónsson
Source: Nr 5 in requirements
Actors: Buyer or seller
Precondition: User is logged in
Postcondition: User has been successfully logged out 
Trigger: user wants to finish his session
Main success scenario:
    1. User clicks the logout button
    1. User confirms logging out
Extensions: 


Name: Edit user information
Number: 6
Description: The user wishes to edit his name or biography
Priority: High
Author: Gissur Már 
Source: Nr 6 in requirements
Actors: Buyer or seller
Precondition: User already exists and is logged in
Postcondition: User successfully updates or adds to his biography and all information about the user is as correct as it gets at that time.
Trigger: User has some incorrect user information and he wishes to correct it or wishes to add some trivial information to his biography
Main success scenario:
    1. The user clicks on the profile image to open the user profile
    2. The user chooses to update the biography
    3. The user inserts new required information in a form
    4. the user saves the updated information
Extensions:
    1.a. The user is not logged in see use case 2
    4.a. The user discards the inserted information

Name: Edit user profile image
Number: 7
Description: The user wishes to change his profile image
Priority: High
Author: Gissur Már
Source: Nr 7 in requirements
Actors: Seller or buyer
Precondition: User is logged in
Postcondition: User has updated his profile image
Trigger: User wishes to change his profile image to appear more trustworthy
Main Success Scenario:
    1. The user clicks on the profile image to open the user profile
    2. The user clicks on the "change image" button
    3. the user uploads a new profile image
    4. user submits changes
Extensions:
    1.a. The user is not logged in see use case 2
    4.a. The user discards the changes to the profile image

Name: Search by item name
Number: 8
Description: The user searches for an item by name 
Priority: High
Author: Gissur Már 
Source: Nr 8 in requirements
Actors: Seller or buyer
Precondition: The item searched for is listed for auction
Postcondition: The item is found by searching and the user can take further action.
Trigger: The user wishes to search item by name
Main success scenario:
    1. The user inserts an item name or part of an item name in the search field and presses enter
    2. The user chooses and clicks on an item he wishes to inspect
Extensions: 
    1.a. Item with given name is not listed and therefor no item is previewed


Name: Order by Name
Number: 9
Description: The user orders items that have been put up for auction by name
Priority: High
Author: Gissur Már 
Source: Nr 10 in requirements
Actors: All users
Precondition: No precondition
Postcondition: Items are sorted ascending or descending by name
Trigger: The user wishes to order items by name to have a better or different overview of the items listed
Main success scenario:
    1. The user orders the items available in ascending or descending order by clicking the order by name option
Extensions: None


Name: Order by price
Number: 10
Description: The user wishes to order items that have been put up for auction by price or current highest bid
Priority: High
Author: Gissur Már 
Source: Nr 9 in requirements
Actors: All users
Precondition: No precondition
Postcondition: Items are ordered by price or highest current bid
Trigger: The user wishes to order items by name to have better or different overview of the items listed
Main success scenario:
    1. The user orders the items available in ascending or descending order by clicking the order by name option
Extensions: None


Name: See item detail
Number: 11
Description: Users clicks the item to see further information.
Priority: High
Author: Gissur Már
Source: Nr 11 in requirements
Actors: All users
Precondition: No precondition
Postcondition: Further information about the item is previewed
Trigger:
Main success scenario:
    1. User clicks the item of interest to open the detailed information for said item
Extensions: None


Name: Create item
Number: 12
Description: User creates a new item to put up for auction
Priority: High
Author: Gissur Már 
Source: Nr 12 in requirements
Actors: Seller
Precondition: User has to be logged in to create an item to auction. 
Postcondition: Item is created and put up for auction
Trigger: A user wishes to put an item up for auction
Main success scenario:
    1. User chooses the "New ad" option 
    2. User fills out the form to create a new item
    3. User saves the form and adds a new item up for auction
Extensions:
    1.a. The user is not logged in and can´t create a "New ad" see use case 2
    3.a. The user discards the form for creating a new item 


Name: See item information
Number: 13
Description: User can see detailed information for each listed item
Priority: High
Author: Gissur Már
Source: Nr 14 and 15 in requirements
Actors: All users
Precondition: Detailed information about an item is awailable
Postcondition: Detailed information about an item is displayed
Trigger: A user wishes to view detailed information about an item to decide if he wants to make a bid
Main success scenario:
    1. User clicks on the image of item of interest
    2. A page with detailed information about the item is displayed
Extensions:
    2.a. Item information can be missing or lacking


Name: Make a bid
Number: 14
Description: A buyer makes a bid for a listed item
Priority: High
Author: Gissur Már
Source: Nr 16 in requirements
Actors: Buyer
Precondition: An offer for the listed item has not already been accepted by the seller
Postcondition: A new bid for the item awaits review by seller
Trigger: A potental buyer sees an item he want to bid on
Main success scenario:
    1. A potential buyer scrolls through the listed items and sees an item of interest
    2. The potential buyer clicks on an item of interest to see more detailed information along with the make bid button
    3. The potential buyer inserts the amount he wants to bid and sends the bid clicking the make bid button
    4. The potential buyer repeats step 1 - 3 as many time as he wants with increased amount until offer is accepted or item is marked as sold.
Extensions:
    2.a. the potential buyer is not logged in and therefor the make bid button is not awailable, see use case 2
    3.a. The potential buyer inserts an amount that is lower than the current highest bid wich is denied by default


Name: Receive a bid
Number: 15
Description: Receive a bid on an item
Priority: High
Author: Gissur Már
Source: Nr 13 in requirements
Actors: Seller
Precondition: An item must be listed for auction (Not already sold)
Postcondition: The seller can decide if he wants to accept or decline after receiving an offer
Trigger: A buyer makes a bid for a listed item
Main success scenario: 
    1. The seller receives notification regarding a new bid on a listed item of his
    2. The seller reviewes the bid and can accept or decline the offer
Extensions:
    None 


Name: Reviewing a bid
Number: 16
Description: 14
Priority: High 
Author: Gissur Már
Source: Nr 15 in requirements
Actors: Seller
Precondition: The potential buyer has made a valid bid on an item.
Postcondition: The buyer can proceed to checkout to finalize the sale
Trigger: The seller accepts the buyers bid
Main success scenario: 
    1. The seller receives a notification regarding a bid for an item in his posession
    2. The seller proceeds to review the bid
    3. The seller either accepts or declines the bid
Extensions:


Name: Finalizing a sale
Number: 17
Description: A prospective buyer with an accepted offer finalizes the offer by entering his payment and contact information
Priority: High
Author: Gissur Már
Source: nr 16 - 17 in requirements
Actors: Buyer
Precondition: an offer is accepted by a seller
Postcondition: The delivery information for the item is sent to the seller
Trigger: The offer from a prospective buyer is reviewed and then accepted by the seller
Main success scenario:
    1. The buyer receives notification that his offer has been accepted
    2. The buyer proceeds to checkout
    3. The buyer fills out a form with the delivery information and 
    4. The buyer fills out a form with payment information and makes a payment
    5. the buyer reviews the the filled out form for delivery and sends the form if satisfied
Extensions:
    4.a. payment is not authorized user tries again with a different payment method 
    5.a. User decides to change some delivery information. 


Name:
Number:
Description:
Priority:
Author:
Source:
Actors:
Precondition:
Postcondition:
Trigger:
Main success scenario:
Extensions:

17. 
Name:
Number:
Description:
Priority:
Author:
Source:
Actors:
Precondition:
Postcondition:
Trigger:
Main success scenario:
Extensions:

18. 
Name:
Number:
Description:
Priority:
Author:
Source:
Actors:
Precondition:
Postcondition:
Trigger:
Main success scenario:
Extensions: