# House Party Py
**Basic python version of original project which is written in C#**

It's a file wiper program which can get commands remotely and acts in emergency stiuations. 
Program's name inspired by Iron Man 3 movie where Tony Stark activates the "House Party Protocol" when his house is destroyed.
It's written for preventing your private datas captured by police or thieves. 



## Methods and Features
* Written in Python 3.4
* Encrypts target files with AES algorithm with random key. It uses unique random key for every single file.  

## Usage
``` python3 hpp.py --help ```
 * -d Directory to be encrypted
 * -u Url in which the script takes command
 * -i interval for checking the url

Example:
``` python3 hppy.py -d /home/utku/secret -u http://utkusen.com/command.txt -i 60 ```

## Giving Command

* You need to have a hosting account which can run php scripts (you can register for a free one)

Change the `$password` section and upload it to your hosting as `.php` file (ex: bust.php) And upload a blank `command.txt` file with it.

```php
<?php

$password = "utku123";  // Change it

?>

<html>
<head>
<title>Panel</title>
</head>
<body>
<?php 
if (isset($_POST["password"]) && ($_POST["password"]=="$password")) {
?>

<?php
$file = fopen("command.txt","w");
echo fwrite($file,"1");
fclose($file);
?>
<b>Completed</b>

<?php 
}
else
{

if (isset($_POST['password']) || $password == "") {
  print "<p align=\"center\"><font color=\"red\"><b>Incorrect Password</b><br>Please enter the correct password</font></p>";}
  print "<form method=\"post\"><p align=\"center\">Please enter your password for start wiping<br>";
  print "<input name=\"password\" type=\"password\" size=\"25\" maxlength=\"10\"><input value=\"Login\" type=\"submit\"></p></form>";
}

?>

</body>
</html>
```
* Collect your evidence files into one folder.
* For giving the encrypt command, open your `bust.php` file (http://yourwebsite.com/bust.php) with your mobile phone's or computer's browser
* Enter your password
* Action Starts

## Warning

While this may be helpful for some, there are significant risks. You could go to jail on obstruction of justice charges 
just for running House Party Protocol, even though you are innocent.

