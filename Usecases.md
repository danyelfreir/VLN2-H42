1. 
Name: Register User
Number: 1
Description: A prominent user wants to register as a Fyre Sale user
Priority: High
Author: Gissur Már Jónsson
Source: Nr 1 in requirements
Actors: prominent seller or buyer
Precondition: User does not already exist 
Postcondition: User is created and can now make bids on items or adding new items up for auction.
Trigger: A prominent user has an item he wishes to auction or desires to make a bid on a item that has been listed for auction
Main success scenario:
Extensions:

2. 
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
Main success scenario: User successfully logs in with a username and a password
Extensions: User cannot log in due to having the wrong username or password. The user has to apply for a new password for the existing user

3. 
Name: Seller checks his rating
Number: 3
Description: seller checks his rating in his user profile
Priority: High
Author: Gissur Már
Source: Nr 3 in requirements
Actors: Seller 
Precondition: Seller has been rated by a buyer
Postcondition: User can take actions to either preserve his rating or get a better rating
Trigger: User wants to check if he has a good rating. 
Main success scenario: User sees his rating listed on his profile
Extensions: User has not been rated by any buyer and can therefor not have a rating.

4. 
Name: Buyer checks seller rating
Number: 4
Description: Buyer intends to make a bid on an item and wishes to assess the sellers reliablility
Priority: High
Author: Gissur Már 
Source: Nr 3 in requirements
Actors: Buyer
Precondition: Seller has been rated by a buyer
Postcondition: Buyer can decide if seller is reliable considered his rating.
Trigger: A buyer intends to make a bid and wants to assess the seller
Main success scenario: Seller has a rating and the buyer can decide if he wants to make a bid or not. 
Extensions: Seller does not have a rating. 


Spurning um að sleppa
Name: Log out user
Number: 5
Description: User wants to log out of his session
Priority: High
Author: Gissur Már Jónsson
Source: Nr 4 in requirements
Actors: Buyer or seller
Precondition: User is logged in and wishes to log out
Postcondition: User has been successfully logged out 
Trigger: 
Main success scenario:
Extensions: 

6. 
Name: Edit user information
Number: 5
Description: The user wishes to edit his name or biography
Priority: High
Author: Gissur Már 
Source: Nr 5 in requirements
Actors: Buyer or seller
Precondition: User already exists 
Postcondition: User successfully updates or adds to his biography and all information about the user is as correct.
Trigger: User has some incorrect userinformation and he wishes to correct it or wishes to add some trivial information to his biography
Main success scenario: 
Extensions: User cancels or wishes to discard the updated biography. 

7. 
Name: Search by item name
Number: 7
Description: The user searches for an item by name 
Priority: High
Author: Gissur Már 
Source: Nr 7 in requirements
Actors: Seller or buyer
Precondition: The item is listed for sale
Postcondition: The item is found by searching and the user can make a bid or update item information if the item is his own.
Trigger: The user wishes to search item by name either
Main success scenario:
Extensions: Item is not listed and no information is 