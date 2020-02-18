# Django Library

Django Library is a Library Management Tool that allows users to search for books and check them out online.
Checked-out books are viewable for the user via their own online library card. 

The inspiration for this was based on an existing need in the office of my current employer. Currently there is a small cache of books relevant to the business. However there is no real way of tracking who has borrowed a volume. In addition, those based on client side have no way of being able to access the books, or even see what would be available. 
 
## UX
 
The main guiding principles for the UX of this project was for the library to be approachable and intuitive. 
I felt it important to draw a clear delineation between Borrowers and Librarians, and used the app authentication to offer different features for each type of user. An example user story for each is offered below:

*As a Borrower, when I am logged into the Library, I want to be able to view a list of the books. 
*As a Librarian, when I am logged into the library, I want to see the cost of books, and do not want other borrowers to acces this information. 

For navigation, I felt that access to the "book" view would be of paramount interest. Becaus of this I opted to have a pop-in nave menu - therefore allowing the user the full screen for viewing books. The Nav menu is accessible via clicking on an easily recognisable "burger" icon. I fixed the options available in the menu, but had the unavailable /or irrellevant options greyed out - dependent on the user's situation. 

For Search / Filter I used the universal magnifying glass icon. I ekected to use a version with a plus inside of it therefore offering the user a clue that the icon would reveal a menu. In order to ensure that these icons would be compatible with smaller screens, I had the Search/Filter icon hide on opening of the nav menu. I also ensured that the nav menu was clickable even when the filter menu was open, and that all transitions between the states remained smooth. 

## Design

As noted in the UX section, I wanted an unfussy design. The Library announcement banner hides on scrolling, but the filter and search elements are made sticky. The nav and search buttons (and add book if logged in as a super-user) are fixed near the bottom of the screen. this is all to leave as much screen real estate as possiible for viewing available books. 

In order to leave the interface uncluttered, I elected lo leave as much white space as possible (utilising a large left & right margin on desktop sizes - but removing it on smaller screens). For the books/tiles I used a simple complementary colour scheme via some help from https://www.canva.com/colors/color-wheel/.

I chose Fjalla One and Noto Sans as my font pairing. I feel that Noto sans is exceptionally legible under almost any condition, whilst Fjalla One is eye catching without being obtrusive. 

I used FontAwesome for the iconography on the books. The simple concept of an Open Book being available - whilst Closed is unavailable I feel is underlined by the colour scheme used. 

 
## Features

Authorisation       Django's default authorisation was used. This allowed separation of user/superuser as well as streamlining                      the addition of user management / password management features. 

Library View       The main library view shows all books in the library catalogue in a card format. I used colour coding to                        intuitively show books checked in / out as well as a simple icon system. 

Filter / Search     The filter / search functions allow a user to quickly define the book that they are looking for or the                          genre that they have an interest in. 

Check in / Out      Once the user has found a book that they are interested in, they have the option to click on it and check                     the volume out. Once a book is checked out, it is unavailable to all other users. The book can only be                         checked back in by the original borrower.

Library Card        At a glance, users can see all of their checked out books.

Add Books           This functionality is hidden for all but the Librarian (superuser). 

Stripe Integration  To offer users the ability to pay a membership subscription online. (This is not required in a real world                     application for the app. It was added to fulfil the requirements of the brief). 

### Features Left to Implement

Past MVP, the library could evolve in a number of directions. I think what could add the most value would be a full history of books, so that statistics could be built up of the books that have proven to be more popular and / or useful. 

## Technologies Used

In addiiton to Python / Django I used the following:

Spectre.css - a very lightweight and unobtrusive css frasmework. In hindsight, I would have perhaps worked quicker just utilizing 'vanilla' css / flexbox, but I enjoyed experimenting with a new framweork and grid paradigm. https://picturepan2.github.io/spectre/

Whitenoise - a fantastic utility that streamlined the deployment process. It allowed me to host static files on Heroku, therefore circumventing the requirement for AWS (or similar) hosting. http://whitenoise.evans.io/en/stable/

PostgreSQL - fantastic open source database. https://www.postgresql.org/

Pipenv - Virtual environment (required as using a Mac)

Python-Dotenv - used to manage the .env file. 

iTerm - Terminal used specifically to manage the virtual env and internal server. 


## Testing

The project was tested in multiple screen sizes. I utilised Google Dev tools to check at desktop and mobile resolutions, ensuring that media queries were used wherever pertinent. 

HTML was validated via W3 validation tools https://validator.w3.org/#validate_by_input
CSS was validated similarly at https://jigsaw.w3.org/css-validator/

I ensured that all functions were manually checked, including the log in / out signup screens. Multiple books were added to test the add book functionality and specific books added to test edge cases.

The book entitled "my word is my bond" was created specifically to test for titles booked out by other users.

I manually compared the User / Superuser views to ensure that there are no visual artifacts, and also to confirm that the separation of features is as intended. 

For instance, the following was manually tested:

As a Librarian, when I am logged into the library, I want to see the cost of books, and do not want other borrowers to access this information. 

I was able to confirm that the mock pricing appended to books is only viewavble when logged in as 'Librarian'

## Deployment

Local Deployment was cumbersome as I'm currently using a Mac. It necessitated separate installs of python, django, and a virtual environment. I opted for Pipenv. The .env file was managed via python-dotenv. 
Whilst working locally, I opted to use the inbuilt db.Sqlite3 - but migrated to Postgres on hosting with Heroku

Deployed to Heroku using Gunicorn, Whitenoise, Postgres and dj-database-url. 
In fairness, I had multiple issues with Heroku, most of which I had caused myself by not properly managing my Pipfile / Pipfile.lock. However I feel that I have learned a lot from this and would be more confident using Heroku in future. 
The url for the delpoyment is https://warm-forest-68273.herokuapp.com/

## Credits

### Acknowledgements

- I received inspiration for this project from my current workplace (AND Digital). The ability to monitor a small works library is a current requirement, especially for workers based off site. Implementation of an app such as this could address the problems re management / access. 

- I feel that I have to acknowledge the following tutorial - https://testdriven.io/blog/django-stripe-tutorial/
It allowed me to implement Stripe as the method shown in the Code Institute tutorials did not work on my setup. 
However, even following the advice offered, I found that Django could not access the Stripe secret/publishable keys via environmental variables. The issue did not occur in any of the other values in my .env file - so I am unsure if the problem was once again my system setup - or perhaps my inexperience in using stripe. 
