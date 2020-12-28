![Logo-with-text-for-Git-Hub-Top.png](https://i.postimg.cc/W1x2QZnB/Logo-with-text-for-Git-Hub-Top.png)



# Edvive Bulk Emails

###### Version 1.0.1

This program is for sending bulk emails with Gmail by parsing emails , developed by Edvive.



# Table of Content

* [Introduction](#introduction)
* [Usage](#usage)
  * [Installation](#installation)
    * [Windows](#windows)
    * [Linux](#linux)
  * [Sending Emails](#sending-email)
    * [Browsing CSV File](#browsing-csv-file)
    * [Subject and Type](#subject-and-type)
    * [Email Body](#email-body)
    * [Variables](#variables)
    * [Email Field](#email-field)
    * [Credentials](#credentials)
    * [Logs](#logs)
* [Miscellaneous](#miscellaneous)
  * [Enabling less secure app access](#less-secure-app-access)
  * [Creating CSV files](#creating-csv-files)
    * [From Google Sheets](#from-google-sheets)
    * [From Microsoft Excel](#using-microsoft-excel)
    * [By writing](#by-writing)
  * [Virtual Environment](#virtual-environment)
* [Developers guide](#developers-guide)
  * [Tasks](#tasks)
    * [Intentional Bugs](#intentional-bugs)
    * [Limitations](#limitations)
    * [Zero-day vulnerabilities](#zero-day-vulnerabilities)
    * [Improvements](#improvements)
  * [Reference](#reference)
    * [Bulkmail](#bulkmail)
    * [PySimpleGui](#pysimplegui)
    * [Executable](#executable)
* [Contact](#contact)
  * [Submission](#submission)
  * [Issues and Support Tickets](#issues-and-support-tickets)
  * [Edvive](#edvive)
    * [General Contact](#general-contact)
    * [Internship Opportunity](#internship-opportunity)



# Introduction

This is the very first version of Edvive's own emailing software for sending bulk emails with Gmail after parsing data from a single [CSV file](https://en.wikipedia.org/wiki/Comma-separated_values). The app is written in Python and can send both Plaintext and HTML emails and eventually can be personalized for each recipient.

# Usage

The software is just a one-window GUI application. So this is pretty easy to use. All a user has to do is write up the stuff, press some buttons and it's done!

## Installation

### Windows

There is no installation required. Anyone can download the standalone binary from [Github](https://github.com/Edvive/Bulk-Email-GUI/blob/master/dist/BulkMail.exe) or [MediaFire](https://www.mediafire.com/file/39es6w8csbvoar9/BulkMail.exe/file). After downloading,  just double-clicking the BulkMail.exe will start the application.

### Linux

If you are a Linux user, first clone this repository by using `git clone https://github.com/Edvive/Bulk-Email-GUI/` command. Then get into the folder using `cd Bulk-Email-GUI` command and then [create a virtual environment](#virtual-environment) inside the folder. Activate the virtual environment and install the required packages using `pip install -r requirements.txt` command. Then you can just do `python3 gui.pyw` and you're good to go with.
The same method can be applied by windows users too who already have installed python. They just need to write `python gui.pyw` instead.


For either OS, you will see this window if the program runs successfully-

![window.png](https://i.postimg.cc/ydfDwdr2/window.png)

## Sending Email

For this documentation, we will use the following table for example showing purpose-

```
Name   |Contact|    Email    | ID
-------|-------|-------------|----
Mr. X  | 11111 | x@gmail.com | 101
-------|-------|-------------|----
Mr. Y  | 22222 | y@yahoo.com | 102
-------|-------|-------------|----
Mr. Z  | 33333 | z@gmail.com | 103
```

Using the software, *we will be sending confirmation emails for organization's new members*.

### Browsing CSV File

The first thing you will need is a CSV file that contains all the email addresses and other data. Check [Creating CSV Files](#creating-csv-files) section in case you already do not have one.

According to the aforementioned table, the CSV file will look like below when opened-

```
Name,Contact,Email,ID
Mr. X,11111,x@gmail.com,101
Mr. Y,22222,y@yahoo.com,102
Mr. Z,33333,z@gmail.com,103
```



When you have your CSV file ready, click on the `Browse` button and import your CSV file. You do not have to have it in the same folder. 

![Browse](https://i.postimg.cc/FHtN1fWb/browse.png)

After you have selected a valid CSV file, the column names of the file will be prompted in the screen. An error will be shown if the file is not valid. The filed names will be required later on.

![validity](https://i.postimg.cc/fRrW7wv5/validity.png)

### Subject and Type

The subject field is pretty self explanatory. You have to write down the subject of your email here. We will write `Confirmation Email` in this text box.

The radio buttons asks you to select email type. It either would be HTML or just plain text. We will cover both of them in this document.



### Email Body

Here comes the important part. Not only we need to send an email, but also need to personalize each email.

![Email demo](https://i.postimg.cc/wvksp0Z7/demo.png)

In the picture, we can see emails containing recipients' `Name`, `Contact No` and `ID`. Doing this is tricky enough. But thankfully we got a cool templating system. All we need to do is wrap the parts which are going to be changed in each using `angular braces` aka `<>` with a variable and the program will do the rest.

So, the mail body for the `HTML` email in the picture will look something like this-

```html
<h1 align='center'>EDVIVE</h1>

<b>Dear <name></b>,
<br>
<br>
Your request for joining Edvive as an intern has been granted. You can now join our <a href=https://edvive.com/<id>">workspace</a>.
<br>
<br>
<i>Your work ID: <id></i>
<br>
<br>
Note: We will send a secret link for our community group to <i><contact></i>. If this contact is unavailable, please let use know.
<br>
Thank you
```

And the mail body for the `plaintext` email in the example will look something like this-

```
Dear <name>,

Your request for joining Edvive as an intern has been granted. You can now join our workspace by going to this link: https://edvive.com/<id>

Your work ID: <id>

Note: We will send a secret link for our community group to <contact>. 
If this contact is unavailable, please let use know.

Thank you
```

Notice how we replaced the places where the `Name`, `Contact No` and `ID` will be present in the emails, with `<name>`, `<contact>` and `<id>` consecutively.

![mail body](https://i.postimg.cc/HLr2TcCQ/example.png)



### Variables

Now as we have replaced the parts in our email body, we need the program to know what parts we have changed. Look at the `Variable Name` and `Field Name` textboxes there. And then check the `Fields` list the above of the subject textbox.

To let the program know what to replace with what, we will follow 3 steps-

1. Write the part wrapped with `<>` in the `Variable Name` box.
2. Write the column name of related data in `Field Name` box.
3. Click on `Add`.

Check the following images for better understanding-

![variable relation](https://i.postimg.cc/VNMdmm57/example.png)

![variable example](https://i.postimg.cc/t4QK8bQR/example.png)

Same goes for the other variables-

![variables](https://i.postimg.cc/DwpMn3Rb/example.png)

You will be notified whether your variable was successfully added or not through the text beside the `Send` button. The app will fail to add a variable if the related column does not exist in the database. For example `Age` column for our demo database.

![succes/failure](https://i.postimg.cc/Dy8GRVQN/example.png)



### Email Field

Name of the column that contains the email addresses of the recipients. You'll need to write the column name exactly what it is. Emails won't be sent properly otherwise.

![email](https://i.postimg.cc/nLHBRX34/example.png)



### Credentials

In the `Email Address` and `Password` column, you have to type in your Gmail address and password (Your data would not be stolen. You might check the [codes](https://github.com/Edvive/Bulk-Email-GUI)). Before doing that, make sure to [enable less secure apps](#less-secure-app-access) in your Gmail account.

Just type in your Gmail address and Password and click send. That's all.

![credentials](https://i.postimg.cc/1t4QKK6L/example.png)

Note: You will receive `Credentials do not match` error if your email/password is incorrect or less secure app access is `disabled`. 

Don't forget to disable the less secure app login again after sending your mails!



### Logs

After your emails are sent (or while they are still being sent) you can see `success.log` and `failure.log` files present in the same folder where `BulkMail.exe`/`gui.pyw` is located. They will look like below when opened-

```
Session starts at 27/12/2020, 21:03:30
Email sent to x@gmail.com at 27/12/2020, 21:03:31
Email sent to y@yahoo.com at 27/12/2020, 21:03:33
Email sent to z@gmail.com at 27/12/2020, 21:03:34

Session ends at 27/12/2020, 21:03:34
-----------------------
```





# Miscellaneous

## Less Secure App Access

Turning on

1. Go to [your google account settings for less secure access](https://myaccount.google.com/lesssecureapps).
2. Click the turn off button.

Turning Off

1. Go to [your google account settings for less secure access](https://myaccount.google.com/lesssecureapps).
2. Click the turn off button.

## Creating CSV Files

### From Google Sheets

1. First of all log in into your Google account and browse [Google sheets](https://docs.google.com/spreadsheets/) website. 

2. Then create or open an already created spreadsheet.

3. On top-left you will find the `File` tab. Click on it and do the following-

   `File > Download > Comma Seperated Values(.csv)`

![csv google](https://i.postimg.cc/nV7Y09xW/example.png)



### Using Microsoft Excel

1. Open the `Microsoft Office Excel` document. 

2. On top left, you will find the `File` tab. Do the following-

   `File > Export > Change File Type > Other File Type > CSV`

![Microsoft Excel](https://i.postimg.cc/QMsRdZb8/example.png)



### By writing

For this documentation, we will use the following table for example showing purpose-

```
Name   |Contact|    Email    | ID
-------|-------|-------------|----
Mr. X  | 11111 | x@gmail.com | 101
-------|-------|-------------|----
Mr. Y  | 22222 | y@yahoo.com | 102
-------|-------|-------------|----
Mr. Z  | 33333 | z@gmail.com | 103
```

Here the column names are- `Name`,`Contact`, `Email` and `ID`.
So the first line of the CSV file would be - `Name,Contact,Email,ID`

In the next three lines, we will typing out the rows serially, without any extra space. The lines will be- `Mr. X,11111,x@gmail.com,101`, `Mr. Y,22222,y@yahoo.com,102` and `Mr. Z,33333,z@gmail.com,103`.

So the CSV file will look like below-

```
Name,Contact,Email,ID
Mr. X,11111,x@gmail.com,101
Mr. Y,22222,y@yahoo.com,102
Mr. Z,33333,z@gmail.com,103
```

Notice there are no `space` used unless it was strictly required to express the full name.



## Virtual Environment

To install and Run virtual environment, you need to do the following-

1. Open command prompt and run `pip install virtualenv`

2. Inside the relevant directory (where the `requirements.txt` file is located), run `python -m venv virtualenv`

3. Run `virtualenv\Scripts\activate.bat` in command prompt. If successful, you'll see changes in command prompt.
4. Run `pip install -r requirements.txt` in `virtual environment` to install necessary modules



# Developers' Guide

## Tasks

This section will be updated when Edvive launches the campaign related to this application. 

### Intentional Bugs (To-be)

### Limitations (To-be)

### Zero-day vulnerabilities (To-be)

### Improvements (To-be)



## Reference

### Bulkmail

`bulkmail` is the module used for sending emails in this project.  

Since the package is under [MIT License](https://choosealicense.com/licenses/mit/) , developers who are going to contribute to `gui.pyw` are permitted to make changes to the `bulkmail` package if necessary. The package files has been included in this repository.

Installation: `pip install bulkmail`

For better understanding about `bulkmail`, check the documentation [here](https://roughweed.github.io/csv-bulk-email/).



### PySimpleGui

`PySimpleGui` is a Python GUI package made on top of `Tkinter`. This specific package has been used to make the GUI interface of this application.

Installation: `pip install pysimplegui`

Check the full documentation [here](https://pysimplegui.readthedocs.io/en/latest/).



### Executable

To convert the `gui.pyw` into a `standalone executable`, the `pyinstaller` package has been used.

Installation: `pip install pyinstaller`

Check the full documentation [here](https://www.pyinstaller.org/).

# Contact

## Submission

To submit your improvements, you can always fork the repository, make changes and make pull request anytime.

Submission process for Edvive's programs will be declared later.



## Issues and Support Tickets

For any question or development issue about this program, file a ticket [here](https://github.com/Edvive/Bulk-Email-GUI/issues).



## Edvive

### General Contact

* [Official Website](https://edvive.com)
* [Facebook](https://www.facebook.com/edviveofficial/)
* [Instagram](https://www.instagram.com/edviveofficial/)
* [LinkedIn](https://www.linkedin.com/company/edvive/)

### Internship Opportunity

Visit [here](https://edvive.com/apply/) to know about the latest internship opportunity.