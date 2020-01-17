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

Add Books           This functionality is hidded for all but the Librarian (superuser). 

Stripe Integration  To offer users the ability to pay a membership subscription online. (This is not required in a real world                     application for the app. It was added to fulfil the requirements of the brief). 

### Features Left to Implement

Past MVP, the library could evolve in a number of directions. I think what could add the most value would be a full history of books, so that statistics could be built up of the books that have proven to be more popular and / or useful. 

## Technologies Used

In addiiton to Python / Django I used the following:

Spectre.css - a very lightweigh and unobtrusive css frasmework. In hindsight, I would have perhaps worked quicker just utilizing 'vanilla' css / flexbox, but I enjoyed experimenting with a new framweork and grid paradigm. https://picturepan2.github.io/spectre/

Whitenoise - a fantastic utility that streamlined the deployment process. It allowed me to host static files on Heroku, therefore circumventing the requirement for AWS (or similar) hosting. http://whitenoise.evans.io/en/stable/

PostgreSQL - fantastic open source database. https://www.postgresql.org/


## Testing

The project was tested in multiple screen sizes. I implemnented Pytest to check logic / functions within the app. 


## Deployment

Deployed to Heroku using Gunicorn, Whitenoise, Postgres and dj-database-url. 
In fairness, I had multiple issues with Heroku, most of which I had caused myself by not properly managing my Pipfile / Pipfile.lock. However I feel that I have learned a lot from this and would be more confident using Heroku in future. 
The url for the delpoyment is https://warm-forest-68273.herokuapp.com/

## Credits

### Acknowledgements

- I received inspiration for this project from my current workplace (AND Digital). The ability to monitor a small works library is a current requirement, especially for workers based off site. Implementation of an app such as this could address the problems re management / access. 

- I feel that I have to acknowledge the following tutorial - https://testdriven.io/blog/django-stripe-tutorial/
It allowed me to implement Stripe as the method shown in the Code Institute tutorials did not work on my setup. 
However, even following the advice offered, I found that Django could not access the Stripe secret/publishable keys via environmental variables. The issue did not occur in any of the other values in my .env file - so I am unsure if the problem was once again my system setup - or perhaps my inexperience in using stripe. 

- Because of the amended implementation of Stripe. No JS was required for this applicaiton. 
