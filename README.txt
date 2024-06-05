Page URL: http://wangehacker.cn/DVWA/login.php
requests - for making HTTP requests
termcolor - coloring output in the terminal

Function, cracking takes two arguments: url and username
The function:
1. iterates over a list of passwords
2. strips each password of any whitespace
3. Prints message indicating current password being tried in red
4. Constructs a dictionary 'data' with the username, password, and a login key with the value submit
5. Sendas a POST request to the url with the data dictionary
6. Checks if the login_failed is present in the response 
If it does it continues to the next iteration
If it's not, print message in green indicating found username and password before exiting the program

The next part of the code opens the password_file in read mode and assigns it to variable passwords
With statement closes the file once we are done with it
cracking function is then called

For the password file, download the rockyou.txt file