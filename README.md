# Django Library

Django Library is a Library Management Tool that allows users to search for books and check them out online.
Checked-out books are viewable for the user via their own online library card. 

The inspiration for this was based on an existing need in the office of my current employer. Currently there is a small cache of books relevant to the business. However there is no real way of tracking who has borrowed a volume. In addition, those based on client side have no way of being able to access the books, or even see what would be available. 
 
## UX
 
The main guiding principles for the UX of this project was for the library to be approachable and intuitive. 
I felt it important to draw a clear delineation between Borrowers and Librarians, and used the app authentication to offer different features for each type of user. An example user story for each is offered below:

As a Borrower, when I am logged into the Library, I want to be able to view a list of the books. 
As a Librarian, when I am logged into the library, I want to see the cost of books, and do not want other borrowers to acces this information. 

## Features

Authorisation       Django's default authorisation was used. This allowed separation of user/superuser as well as streamlining                      the addition of user management / password management features. 

Library View       The main library view shows all books in the library catalogue in a card format. I used colour coding to                        intuitively show books checked in / out as well as a simple icon system. The icons themselves doubled as                      a button to check in / out selected books. 

Filter / Search     The filter / search functions allow a user to quickly define the book that they are looking for or the                          genre that they have an interest in. 

Library Card        At a glance, users can see all of their checked out books.

Stripe Integration  To offer users the ability to pay fines / membership online. 

### Features Left to Implement

Past MVP, the library could evolve in a number of directions. I think what could add the most value would be a full history of books, so that statistics could be built up of the books that have proven to be more popular and / or useful. 

## Technologies Used


## Testing


## Deployment



## Credits

### Acknowledgements

- I received inspiration for this project from X
