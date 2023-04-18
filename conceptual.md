### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  - The main differences are that JavaScript is mainly used through the browser on the client side and Python  is typically for server side programs.
  - Python is more commonly used for data management and structuring while javascript can be user for a variety of things like creating media on a page.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  - First you could use '.get(arg1, arg2)' and pass in the value you're searching for as arg1, and a default value as arg2 if not found.
  - You could also implement some sort of validation to only try to access that key if it exists, 'if x in dict' etc...

- What is a unit test?

  - The lowest level of test, typically tesing a single method or function. It does not test the interoperability of the functions.

- What is an integration test?

  - Next level up from unit tests, will take multiple or groups of functions and test that they are working together properly, this is where you would test your framework and ensure the flow of data is correct throughout your program

- What is the role of web application framework, like Flask?

  - The role of a WAF is simply to make the development process easier. Giving the developer access to methods and operations that would be useful when creating a web app.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  - Generally using a path variable in a route url is best when that parameter is more or less the subject of the page, and you might use a query string to pass extra information about the page, like maybe sort low to high, or enable dark mode etc.

- How do you collect data from a URL placeholder parameter using Flask?

  - You pass the path variable into the decorator function, from there you can access the value of the url placeholder

- How do you collect data from the query string using Flask?

  - request.args['query-term'], or request.args.get('query-term')

- How do you collect data from the body of the request using Flask?

  - Either request.data or request.form

- What is a cookie and what kinds of things are they commonly used for?

  - Cookies are a name value pair and they are used to store small bits of information on a client/browser and this data can be sent back and forth from client to server. They are commonly used for things like a shopping cart or to track how the user uses the site.

- What is the session object in Flask?

  - Sessions are a 'magic' dictionary and can be used to store data as long as the browsing session persists. The session object is used to track this data and interact with it accordingly.

- What does Flask's `jsonify()` do?

  - jsonify() is a way to respond to a request in which data is parsed and sent back in a json format return jsonify({'score': '17'})