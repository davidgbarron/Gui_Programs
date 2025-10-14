# Gui_Programs
This is a collection of my own programs I have coded with a Graphic user interface using python.

# Distinctiveness and Complexity

   This project is based on my love for investing and the markets. I wanted to build something great with all the knowledge I already 
possessed and the knowledge earned from taking this CS50 course, as well as makig a distinct app from all the other projects
in the course.  
	
   The "Stock Trader" app is a trading platform that allows you to view stocks from the Nasdaq exchange. Its Distinctiveness
from the other courses is in the fact that it has the potential to tap into different real-time APIs to fetch its data. Even in this
Iteration, it is totally different from the other projects in that it emulates a real-time API call to fetch data for a particular ticker/symbol.
by having a static snapshot in the form of a JSON file that allows us to get the symbol and its information through our Utilities file.
This allows us to display the stock's information, in essence emulating a real-time API call to get the latest info on that stock. Of course, 
I chose to make it static for this project.

   This project has the potential to plug in real-time data by setting up API calls to a service.
like "TradingView," for example. And fetching the data in real-time and rendering it on our UI. The reason I chose not to take this path and 
Keeping it in an offline static file is because I didn't want to have to set up an API key and share it online; this is not good practice.
Also, to avoid having you, the code reviewers, have to set up or pay for an API that would provide real-time data yourselves. The only project
In this course that this reminds me of, would be the "Mail" project. But this stock projec is distinct in the fact that with the "Mail" project, this was already implemented for us on the backend. In fact, for that project, the entire backend was mostly done for us by you. Whereas here, I had to create 
the entire backend myself for this to work as intended. And to accomplish the vision of this project. That is what makes this not only distinct but also more complex than all the other projects in the course. Finally, this app is fully mobile responsive/accessible. Which also separates it from all the other projects.
	
   The UI has also been completely designed from the ground up in a dark theme that's reminiscent of most tech sites in the same sector.
I decided to incorporate different methods to modify our UI efficiently. I used Javascript to modify the UI without refreshing the page, and also
a couple of clever ways to check if the user is signed in from Javascript. This allows us to either display certain aspects of the UI or allow certain
calls from being made purely from the front-end side. This was further compounded by making sure that in the event this was somehow bypassed, The Django
Decorators would catch this and prevent the user from accessing those features that they should not have access to.
	
   The Stock Trader app allows users to create a trading account by signing up. Or logging in if the user already has one. If logged out, and the user
clicks on the accounts link—users will be redirected to the login page where they can, either log in or register for an account. I did this to make it simpler for the user to either log in or sign up. Upon successful login, the user will be redirected to the "Account" page, where they can view their account.

   The Stocks link can be viewed regardless of authentication. This page displays a list of stocks in alphabetical order in a range of "50" items per page. 
Any of these can be clicked on to be taken to that stock's trading page. The pagination at the bottom of the page was also customized to facilitate navigation of all the available pages. However, this page also has a "Search Stocks" feature that allows the user to do just that: search for any stock that is valid and exists. If the stock exists, the user will be taken to that stock's page. Again, depending on whether the user is signed in or not, the page will dynamically update the UI accordingly to reflect this.

   The Stock page allows users to trade the selected symbol/ticker. This shows a stock chart that's prepopulated with mathematically generated data. 
I did this as part of simulating an API real-time data call mentioned in a previous paragraph. This generates random market data every time the page loads. This in and of itself is a complex and distinctive endeavor as well. For chart rendering I used TradingView's "LightweightChart," which allows us to render the chart and candles, but the generated random data has to be generated and created into candles by us. For this, the use of the Math library in Javascript was imperative. I also included some code that will apply random variations so that the charts render with gap-ups or gap-downs upon loading. I did all this to offer a different price for the stock upon loading, ensuring a constant change that will allow the traders to simulate market fluctuations upon them 
visiting the page. This will obviously be omitted if we were to go the real-time data route.

   The Trade modal in the stock page is where all the magic happens. Here users have the ability to place buy or sell trades at the current market price. 
If the user is not logged in, upon clicking either the "buy" or "sell" buttons, they will be redirected to the login page. This is one of the places I used a clever way of checking whether the user was signed in or not before proceeding. This check is done on the front end and directly directs the user to the login page, never even making it to a backend call. I did this for convenience to the user. If the user is logged in, they will be shown their "Total Buying Power" in "USD" along with the current amount of shares they currently own (if any). Upon placing either a buy or sell order, if the user has enough buying power to make the trade. They will automatically buy or sell at the current market price. And that order will get automatically added to the "Order History"; this includes the time, the amount, the total in USD, and the average price (market price). This will also update the "Total Buying Power," as well as the updated shares owned. This is all happening to our UI on the fly without a page refresh. There are also messages if the user tries to buy or sell more shares than 
they have buying power to execute, or if the user tries to buy or sell an unusual amount of shares.

   The trade history updates on the fly upon placing a trade; this is all calculated on our back end and updated on our front end without any
page refresh. Each trade takes a row in our order history modal; this modal also becomes scrollable after a certain number of scrolls reach the height limit. This is a convenient way to keep everything clean and neat without having to worry about the modal extending way too far down the page.

   Finally, the Account page is where the users' financials live. The first two modals show the "Total Account Value," which is calculated on the backend.
by taking the sum of all the currently owned stocks' market value, plus the "Total Buying Power." The "Total Buying Power" is also calculated on the backend whenever a user makes a trade. If the user buys, the total amount of that trade gets deducted from our Total Buying Power; if they sell, then it gets 
added. "The Stock Portfolio" modal is similar to the Stocks page modal, albeit a lot simpler. This shows the current stocks owned by the user. Along with
their quantity and total market value. If the user sells all their shares in a currently owned stock. This portfolio will reflect that by removing that 
stock from this list dynamically. If the user does not own a stock and buys it, this will dynamically reflect that. The "Trade History" modal on this page is similar to the one on the Stock page; however, instead of showing the history for that specific stock symbol. It shows the history of all the trades ever 
made by the user, for all stock tickers/symbols. This also becomes scrollable after a certain number of entries populate the modal. This was done for convenience and to keep a clean and tidy look.

# What's Contained In Each File

## /

#### models.py
   This contains the py code for our models. There's a total of three django models used for this project.
* StockOwned
this model is used to keep track of our currently owned stocks
* StockTrade
this model is used to keep track of our traded stocks, bought or sold.
* User
this model is used to keep track of our balance, stocks owned, and stocks traded.

#### urls.py
   This contains the py code for our urls. 

#### utils.py
   This contains the py code for our utils. These functions facilitate getting stocks from our nasdaq_full_tickers.json, as well as filtering
functions for stock lists and our pagination.

#### views.py
   This contains the py code for our views. There's a total of 10 view functions that reside here. There's are in charge of interacting with our 
front end to sucessfully view stocks, login, logout, register, view accounts, view specify stock symbol pages, buy, sell, and search.

## template/stocks/

#### account.html
   This contains the html code for our account page. Which renders our Total Account Value, Total Buying Power Modals. Along with our
Stock Portfolio and Trade History modals.

#### index.html
   This contains the html code for our homepage. It consists of our Stock app name, along with an image that's blended in with a gradient background
This all purely Aesthetic.

#### layout.html
   This contains the html code for our general layout that's extended to all of our other .html files. This layout houses the Main toolbar that allows 
the user to navigate to their account and stocks page, as well as display the users name if logged in. Also displays the Login and Signup buttons

#### login.html
   This contains the html code for our login page. This is a simple modal that allows us to login or give the user the option to register.
	
#### register.html
   This contains the html code for our register page. Similar to the login page it allows a user to register and get their own account in our database.
	
#### stock.html
   This contains the html code for our stock page. It consists of our stock name, Generated stock chart with fluctuating price data. Our Trading Modal,
that allows us to place either buy or sell trades at market price. Our Market Data modal, which gives us the stocks financial information. and finally our stock Order History modal. Which gives us the order history for the current stock page.

#### stocks.html
   This contains the html code for our stocks page. It consists of our Search Stocks bar, along with our list of stocks modal, with a pagination of "50" items
per page. Clicking any of these stocks will take us to their trading stock page.

## static/stocks/

#### charts.js
   This is where the heart of our UI lives, and a lot of our functionality as well. Houses all our event listeners, and sets up all our constants and
variables associated with our UI elements. Our functions for search, select, buy, sell, and all our fetch, PUT, GET calls reside here. This also has the
code for our LightweightChart rendering as well as the Math and generate data functions that are used to create dynamic pre-populated chart data.

#### nasdaq_full_tickers.json
   This file contains a JSON object that has a data snapshot of all the stock sticker/symbols in the nasdaq index. This was chosen for simplicity. This 
can of course be replace with real-time data by getting an subscription to an API feed like "Trading View". 

#### styles.css
   This contains all the css code for our entire project. This file contains a dark-theme look and feel. It allows make our app mobile-responsive

# How to run the application
run the following commands in the root of our project using command prompt:
python manage.py makemigrations stocks
python manage.py migrate
python manage.py runserver

If you'd to run on mobile, update the ALLOWED_HOSTS in the settings.py of the project to include your host machine's ip
and run the following command: 
python manage.py runserver 0.0.0.0:8000
subsequently navigate to your host machines ip on your mobile device's browser eg 192.168.50.200
	
# Additional information for the staff
   Thank you! I had an awesome time making this app from start to finish. And overcoming the challenges along the way. No extra requirements
to run the application are needed.
	




	
	
	
