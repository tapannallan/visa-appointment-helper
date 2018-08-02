# visa-appointment-helper
A simple shell+python script to look for visa appointments

This script uses the human captcha solver service, [deathbycaptcha](http://deathbycaptcha.com/) as well as the excellent android integration tool [automate](http://llamalab.com/automate/) from llamalab to try look for a available appointment in German visa portal. Appointments are randomly made available when someone cancels and is therefore crucial to be intimated as soon as one is available.


### Installation

1. Copy this zip to any location and unzip everything into one folder while retaining the folder structure
2. change permissions on setup.sh using `chmod +x setup.sh`
3. Execute `./setup.sh`. This will give you the pre-requisites before you can run setup.
    * Edit the property in `setenv` file to the the root folder
    * Set execute permissions on all the scripts as well as executables
    * Comment out the echo messages and the exit command
4. Now, run `./setup.sh` to install pip and the required python dependencies. Make sure you have python3 installed before you run this


### Configure Android Phone for Notifications
1. Install Automate App in your android Phone
2. Find the flow file in lib/Play sound on msg.flo
3. Copy this into your phone and import the flow into your automate app
4. Edit the flowchart of the flow and configure individual blocks
    * In Cloud Receive, "To Google account" should be your google email account and give random variable names to sender, device and payload. We do not use these variables anywhere
    * In Play sound, select the proper sound URI, can be any song. Edit the start position if necessary
5. Now navigate to https://llamalab.com/automate/cloud/. 
    * Generate a secret key by clicking on the button on the right of the textbox. Make sure you select the email account the same as you have in #4.
    * Enter your email address in the "To" field. This should be the same as the email give in #4
    * Device can be left empty or specify a particular device id if you want
    * Enter a random payload. Any text is fine, even leave it empty if you want
6. Now copy the request string found under `Example webform request`. This should like this `secret=ioavua79hvasdf97asduf9adsfh&to=myemail%40gmail.com&device=&payload=Hello%20World!`. Open run.sh and replace the string at line no. 51 after `-d`. Uncomment the next line if you want to notify two different users and configure it in the same way. Infact, you can add as many notification lines as you want.


### Configurations
* The logic to determine if a available date is useful enough to notify the user is made in `lib/parse_response.py`. Edit it according to your requirements

### Enhancements
* Notify deathbycaptcha when captcha is wrong
* Automatically book appointment instead of just notifying


### Crontab
* Open terminal and execute `crontab -e`
* In the file, add a new line with this content: `*/5 * * * * bash /<path to the folder>/visa-appointment-helper/run.sh > /dev/null 2>&1`
* Save the file