**Description:**

Food donation is a database application for the homeless. This is an application which helps homeless people to get food from nearby restaurants. Restaurants that volunteer to donate the food that goes into waste every day to those in need register themselves on this platform and donate the food.

**Functionalities:**
The basic functionalities of our application are -

- The users and restaurants can register themselves.
- Login into the application
- Search for a restaurant
- Place an order.
- Update the food quantity every time when a user places an order.
- Show the popular restaurants around the user (trigger)
- Generate a monthly report of the restaurants with number of orders placed from them.(stored procedure)

**Attributes:**

- We have implemented three tables:
- Restaurant table, customer table and the order table.
- The restaurant table keeps track of all restaurants, each of which is identified by a unique identifier: rID.
- The customer table keeps track of all registered users, with attributes such as email, phone number and password, which are essential for authentication and login.
- The order table keeps track of all orders placed by customers in every restaurant he/she has visited.

![](RackMultipart20210306-4-1vmd300_html_59b2b0ac6c05caf7.png)

**Restaurant table:**

rID: unique identifier of the restaurant

rLatitude: latitude of the restaurant

rLongitude: longitude of the restaurant

rPhone: phone number used to contact the restaurant

rCuisine: Food type: Indian/Mexican/Italian, etc.

Cuisine\_qty: the amount of servings of food left in the restaurant

Food property: Gluten free/ peanut allergy/ dairy free

rRating: rating of the restaurant, from 0-5

rAddress: zip code of the restaurant

![](RackMultipart20210306-4-1vmd300_html_c15d7cb3e7cee8bb.png)

**Orders table:**

order\_id: unique id for the orders placed

order\_date: Date of the orders placed

Order\_quantity: no. of orders placed

![](RackMultipart20210306-4-1vmd300_html_1da3e37f6d02611e.png)

**Customer table:**

Cust\_id: primary key, unique identification for customer

Cust\_name: customer name

Cust\_email: customer email

Cust\_phone: customer phone number, used to contact customer

![](RackMultipart20210306-4-1vmd300_html_61c615224db0813e.png)

**Schema:**

![](RackMultipart20210306-4-1vmd300_html_dbcbe3b7dc79562f.png)

**Entity Relation Diagram:**

![](RackMultipart20210306-4-1vmd300_html_773427afab1f0e61.jpg)

**Data:**

**Customers table:**

![](RackMultipart20210306-4-1vmd300_html_c02dacee73a8fcef.png)

**Orders table:**

![](RackMultipart20210306-4-1vmd300_html_640e84b735ef938f.png)

**Restaurant table:**

![](RackMultipart20210306-4-1vmd300_html_f8a2a228be95238d.png)

**Backend:**

We will use Azure SQL server as the database to hold the data. We have used Azure VM (4vCPU, 16G RAM) as the backend server and deploy our backend script there. We also have made a REST API that accepts user requests and could directly interact with the Azure database.

**Functional dependencies:**

- **Restaurant table:**
  - **rID** → rName, rCuisine, rPhone, rAddress, rRating, cuisine\_qty, rAddress

- **Orders table:**
  - **Order\_id →** order\_date, order\_quantity, cust\_id, order\_cuisine, rID

- **Customers table:**
  - **Cust\_id →** cust\_name, cust\_email, cust\_phone, credential

**Functionality description**

Homeless people can-

- Register: Adds new entry to the customer table, email, phone, credential
- Login: verify their name and credential
- Search for nearby restaurants based on ratings and location.
- Place order: add a new entry to the order table, update cuisine\_qty in restaurant table.

Other functionalities-

- Restaurants can register themselves.
- Generate a monthly report to know the restaurant names and number of orders placed that month

**SQL Queries:**

**Table creation:**

![](RackMultipart20210306-4-1vmd300_html_f86c19c391860525.png)

**Insertion queries**

![](RackMultipart20210306-4-1vmd300_html_29f9d6910ff80b76.png)

![](RackMultipart20210306-4-1vmd300_html_cb5b048884892b0f.png)

**Stored procedure**

![](RackMultipart20210306-4-1vmd300_html_2fa5bc44255c9d29.png)

**Frontend**

We use Reactive Native and build a mobile App. When user first open the App, he/she would be prompt to Registration or Log In. After successfully authenticating him/herself, A map with nearby restaurants would be displayed. Users can also switch to a list view to view restaurants in a different fashion. In the List view page, use can also check out store sales report. After the user clicks an item and enters the restaurant detail page, Store details would be presented, and he/she can place an order for this restaurant.

**API Reference**

![](RackMultipart20210306-4-1vmd300_html_dd82b515a7ef6208.jpg)[ **http://fooddonationdb.westus2.cloudapp.azure.com:5000/signup**
](http://fooddonationdb.westus2.cloudapp.azure.com:5000/signup)

Function for user signup. Body parameters:

- cust\_name: full name of the user
- cust\_email: email for user registration
- cust\_phone: phone number of the user
- credential: password for user login

Sample Query:

{

&quot;order\_quantity&quot;: 20,

&quot;cust\_id&quot;: &quot;cs003&quot;,

&quot;rID&quot;: &quot;keyvgz56hizj7jd8djotfmvlh4it73uyaibiu2o68q00lcvyojy58k9hytre2vsy&quot;

}

Sample Response:

{

&quot;success&quot;: **true**

}

![](RackMultipart20210306-4-1vmd300_html_dd82b515a7ef6208.jpg)

[**http://fooddonationdb.westus2.cloudapp.azure.com:5000/login**](http://fooddonationdb.westus2.cloudapp.azure.com:5000/login)

Function for login. Body parameters:

- email: user email for login
- password: user password for authentication

Sample query:

{

&quot;email&quot;: &quot;[ada@uw.edu](mailto:ada@uw.edu)&quot;,

&quot;password&quot;: &quot;12345678&quot;

}

Sample response:

{

&quot;cus\_id&quot;: &quot;12kqtw6hy64dobkk0ofnv21y223fe0z667uaqw0czfy3u7ym2z8lilwsy1pw6dg9&quot;,

&quot;cus\_name&quot;: &quot;ada lovelace&quot;,

&quot;success&quot;: **true**

}

![](RackMultipart20210306-4-1vmd300_html_dd82b515a7ef6208.jpg)

[**http://fooddonationdb.westus2.cloudapp.azure.com:5000/placeOrderWithTrigger**](http://fooddonationdb.westus2.cloudapp.azure.com:5000/placeOrderWithTrigger)

Function for placing a order at a restaurant:

- order\_quantity: the amount of food to be consumed
- cust\_id: customer ID number
- rID: restaurant ID number

Sample query:

{

&quot;order\_quantity&quot;: 20,

&quot;cust\_id&quot;: &quot;cs003&quot;,

&quot;rID&quot;: &quot;keyvgz56hizj7jd8djotfmvlh4it73uyaibiu2o68q00lcvyojy58k9hytre2vsy&quot;

}

Sample response:

{

&quot;success&quot;: **true**

}

![](RackMultipart20210306-4-1vmd300_html_dd82b515a7ef6208.jpg)

[**http://fooddonationdb.westus2.cloudapp.azure.com:5000/searchMostPopularRestaurants**](http://fooddonationdb.westus2.cloudapp.azure.com:5000/searchMostPopularRestaurants)

Function for getting a list of &quot;popular&quot; restaurants nearby:

- latitude: user latitude
- longitude: user longitude
- radius: search radius

Sample query:

{

&quot;latitude&quot;: 47.6248771,

&quot;longitude&quot;: -122.3258786,

&quot;radius&quot;: 1000

}

Sample response:

[

{

&quot;cuisine&quot;: &quot;Mexican&quot;,

&quot;distance&quot;: 608,

&quot;id&quot;: &quot;9wvo61nj4m28cojww4fbvewbl3g2k0vsgusyduu9lbfjvxcm8yop2tgofses3vjl&quot;,

&quot;lat&quot;: 47.6215392,

&quot;lng&quot;: -122.3323116,

&quot;name&quot;: &quot;R9&quot;,

&quot;phone&quot;: &quot;2424905651&quot;,

&quot;popularity&quot;: 4.0784,

&quot;quantity&quot;: 540,

&quot;rating&quot;: &quot;4.2&quot;

},

{

&quot;cuisine&quot;: &quot;Greek&quot;,

&quot;distance&quot;: 0,

&quot;id&quot;: &quot;49s25nvxlksftgmh5a89jo2bf2trgurxur5exgd8rh9e0vjtn0s2xnonktekqskn&quot;,

&quot;lat&quot;: 47.6248771,

&quot;lng&quot;: -122.3258786,

&quot;name&quot;: &quot;R10&quot;,

&quot;phone&quot;: &quot;6107972792&quot;,

&quot;popularity&quot;: 4.0,

&quot;quantity&quot;: 550,

&quot;rating&quot;: &quot;4.0&quot;

},

{

&quot;cuisine&quot;: &quot;Indian&quot;,

&quot;distance&quot;: 742,

&quot;id&quot;: &quot;1ow7277jgn13w5i9u4howyj5qjjmmypewojtv8pwvjrjx902v03m8zs182wewhhb&quot;,

&quot;lat&quot;: 47.6239122,

&quot;lng&quot;: -122.3356781,

&quot;name&quot;: &quot;R1&quot;,

&quot;phone&quot;: &quot;5211198870&quot;,

&quot;popularity&quot;: 3.8516,

&quot;quantity&quot;: 525,

&quot;rating&quot;: &quot;4.0&quot;

},

{

&quot;cuisine&quot;: &quot;Japanese&quot;,

&quot;distance&quot;: 882,

&quot;id&quot;: &quot;r76uzsfmijohthjcevrcqwcjh1ydsj5x0caa9l279gjzfcq4h79xmj32iapvljmt&quot;,

&quot;lat&quot;: 47.6218226,

&quot;lng&quot;: -122.3367534,

&quot;name&quot;: &quot;R8&quot;,

&quot;phone&quot;: &quot;1121682299&quot;,

&quot;popularity&quot;: 3.8236,

&quot;quantity&quot;: 537,

&quot;rating&quot;: &quot;4.0&quot;

},

{

&quot;cuisine&quot;: &quot;Italian&quot;,

&quot;distance&quot;: 921,

&quot;id&quot;: &quot;keyvgz56hizj7jd8djotfmvlh4it73uyaibiu2o68q00lcvyojy58k9hytre2vsy&quot;,

&quot;lat&quot;: 47.6226383,

&quot;lng&quot;: -122.3377189,

&quot;name&quot;: &quot;R2&quot;,

&quot;phone&quot;: &quot;4557682231&quot;,

&quot;popularity&quot;: 3.3158,

&quot;quantity&quot;: 478,

&quot;rating&quot;: &quot;3.5&quot;

},

{

&quot;cuisine&quot;: &quot;British&quot;,

&quot;distance&quot;: 802,

&quot;id&quot;: &quot;yjmg2si4e7mfe7mm1q516moaksi9kir7ks27sdtds8j7ix1qfe006n2kxf6a4em4&quot;,

&quot;lat&quot;: 47.6236507,

&quot;lng&quot;: -122.3364272,

&quot;name&quot;: &quot;R3&quot;,

&quot;phone&quot;: &quot;8722127616&quot;,

&quot;popularity&quot;: 2.8396,

&quot;quantity&quot;: 570,

&quot;rating&quot;: &quot;3.0&quot;

}

]

![](RackMultipart20210306-4-1vmd300_html_dd82b515a7ef6208.jpg)

[**http://fooddonationdb.westus2.cloudapp.azure.com:5000/searchRestaurantByLatLng**](http://fooddonationdb.westus2.cloudapp.azure.com:5000/searchRestaurantByLatLng)

Function for getting a list of nearby restaurants:

- latitude: user latitude
- longitude: user longitude
- radius: search radius

Sample query:

{

&quot;latitude&quot;: 47.6248771,

&quot;longitude&quot;: -122.3258786,

&quot;radius&quot;: 1000

}

Sample response:

[

{

&quot;cuisine&quot;: &quot;Greek&quot;,

&quot;distance&quot;: 0,

&quot;id&quot;: &quot;49s25nvxlksftgmh5a89jo2bf2trgurxur5exgd8rh9e0vjtn0s2xnonktekqskn&quot;,

&quot;lat&quot;: 47.6248771,

&quot;lng&quot;: -122.3258786,

&quot;name&quot;: &quot;R10&quot;,

&quot;phone&quot;: &quot;6107972792&quot;,

&quot;quantity&quot;: 550,

&quot;rating&quot;: &quot;4.0&quot;

},

{

&quot;cuisine&quot;: &quot;Mexican&quot;,

&quot;distance&quot;: 608,

&quot;id&quot;: &quot;9wvo61nj4m28cojww4fbvewbl3g2k0vsgusyduu9lbfjvxcm8yop2tgofses3vjl&quot;,

&quot;lat&quot;: 47.6215392,

&quot;lng&quot;: -122.3323116,

&quot;name&quot;: &quot;R9&quot;,

&quot;phone&quot;: &quot;2424905651&quot;,

&quot;quantity&quot;: 540,

&quot;rating&quot;: &quot;4.2&quot;

},

{

&quot;cuisine&quot;: &quot;Indian&quot;,

&quot;distance&quot;: 742,

&quot;id&quot;: &quot;1ow7277jgn13w5i9u4howyj5qjjmmypewojtv8pwvjrjx902v03m8zs182wewhhb&quot;,

&quot;lat&quot;: 47.6239122,

&quot;lng&quot;: -122.3356781,

&quot;name&quot;: &quot;R1&quot;,

&quot;phone&quot;: &quot;5211198870&quot;,

&quot;quantity&quot;: 525,

&quot;rating&quot;: &quot;4.0&quot;

},

{

&quot;cuisine&quot;: &quot;British&quot;,

&quot;distance&quot;: 802,

&quot;id&quot;: &quot;yjmg2si4e7mfe7mm1q516moaksi9kir7ks27sdtds8j7ix1qfe006n2kxf6a4em4&quot;,

&quot;lat&quot;: 47.6236507,

&quot;lng&quot;: -122.3364272,

&quot;name&quot;: &quot;R3&quot;,

&quot;phone&quot;: &quot;8722127616&quot;,

&quot;quantity&quot;: 570,

&quot;rating&quot;: &quot;3.0&quot;

},

{

&quot;cuisine&quot;: &quot;Japanese&quot;,

&quot;distance&quot;: 882,

&quot;id&quot;: &quot;r76uzsfmijohthjcevrcqwcjh1ydsj5x0caa9l279gjzfcq4h79xmj32iapvljmt&quot;,

&quot;lat&quot;: 47.6218226,

&quot;lng&quot;: -122.3367534,

&quot;name&quot;: &quot;R8&quot;,

&quot;phone&quot;: &quot;1121682299&quot;,

&quot;quantity&quot;: 537,

&quot;rating&quot;: &quot;4.0&quot;

},

{

&quot;cuisine&quot;: &quot;Italian&quot;,

&quot;distance&quot;: 921,

&quot;id&quot;: &quot;keyvgz56hizj7jd8djotfmvlh4it73uyaibiu2o68q00lcvyojy58k9hytre2vsy&quot;,

&quot;lat&quot;: 47.6226383,

&quot;lng&quot;: -122.3377189,

&quot;name&quot;: &quot;R2&quot;,

&quot;phone&quot;: &quot;4557682231&quot;,

&quot;quantity&quot;: 478,

&quot;rating&quot;: &quot;3.5&quot;

}

]

![](RackMultipart20210306-4-1vmd300_html_dd82b515a7ef6208.jpg)

[**http://fooddonationdb.westus2.cloudapp.azure.com:5000/getOrderNumbers**](http://fooddonationdb.westus2.cloudapp.azure.com:5000/getOrderNumbers)

Function for getting a list of restaurants with non-zero orders in a given month and year

- month: query month
- year: query year

Sample query:

{

&quot;month&quot;:2,

&quot;year&quot;: 2021

}

Sample response:

{

&quot;results&quot;: [

{

&quot;name&quot;: &quot;R1&quot;,

&quot;order&quot;: 10

},

{

&quot;name&quot;: &quot;R7&quot;,

&quot;order&quot;: 5

},

{

&quot;name&quot;: &quot;R9&quot;,

&quot;order&quot;: 4

},

{

&quot;name&quot;: &quot;R2&quot;,

&quot;order&quot;: 3

},

{

&quot;name&quot;: &quot;R10&quot;,

&quot;order&quot;: 2

},

{

&quot;name&quot;: &quot;R4&quot;,

&quot;order&quot;: 2

},

{

&quot;name&quot;: &quot;R6&quot;,

&quot;order&quot;: 2

},

{

&quot;name&quot;: &quot;R8&quot;,

&quot;order&quot;: 1

},

{

&quot;name&quot;: &quot;R3&quot;,

&quot;order&quot;: 1

}

],

&quot;success&quot;: **true**

}