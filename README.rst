================================
New User Automation Setup Readme
================================

-------------------------------------
Automation of new user accounts in AD
-------------------------------------

Introduction
============

Business Challenge:
Increased demand placed on the IT department to setup network accounts for new
users.  The volume of requests has increased, and the time allotted for each
setup has decreased

Desired Solution:
Automate the process of receiving new user setup requests, verify request
content, and generating new user accounts.  Return documentation of success
and errors to the IT department.


IPO Analyses
------------

Input:
    - Email received with new user request.
    - Emails are sent from management staff.
    - Receiving mailbox is a shared help desk email account.
    - Request details are contained in an attached PDF.  The PDF format is
      standardized.

Process:
  - Macro
    * Sweep mailbox for new user request
    * Read PDF attachement for new user values
    * Create new user account(s)
    * Create new user account info sheet
    * Notify IT department with success and or errors

  - Micro
    * Handshake the service account credentials kept on server
    * Check sending user authority before account creation
    * Copy PDF new user requests to the server
    * Read/Write values to database
    * Check if account already present in AD
    * Keep score of last email processed
    * One time new user passwords generated and encrypted

Output:
  - Completed account setups for new users.
  - Including:
  - Active Directory
  - Microsoft 365
  - Email Signatures(HTML)
  - FTP
  - Return notification of account creation success and any errors to the IT
    team for review.

Proposed Tech
-------------

    #. Virtualization of server running OS, Database, and Application.
    #. Dev setup running on Oracle VirtualBox.  Image created as a VMDK for production
       deployment to Veeam vSphere
    #. Linux Ubuntu Server (stable, reliable and capable of hosting all elements in a
       single location)
    #. MongoDB database (reduced architecture and maintenance needed compared to SQL)
    #. Python 3.8 (strong community support and library features for network code)
    #. PowerShell (further connection options for Microsoft products)
    #. Django/Jinja2 (HTML templating)
    #. Microsoft Graph API (RESTful api for interacting with MS 365 cloud data)
    #. OAuth 2.0 and OpenID Connect (Authorization and authentication)

Proposed Architecture
---------------------
    - Presentation Layer - Human interfaces
    - Business Logic - Business rules and workflows
    - Database Layer - Interaction with data stores

    Types of modules:
        - Goal to maintain levels of abstraction between high-level and low-level modules.
        - High-level - Business or domain specific 
        - Low-level - Tech specific

Components
----------

NewUserRequest:
- The selection of values submitted by management to create a new user.

UserAccount:
- Everything (data) that’s contained in a user account in AD, Office365, and
other systems.

ApplicationTimeClock:
- When did we first run?  When did we last run?  How often are we to run?
What time is it now?

StandardConnection:
- Do you want to connect to a server, system, or service?  Read access?
Write access?  Goal is to create a class that accepts RESTful verbs to
perform CRUD operations.

============== ==============
 HTTP Verb      CRUD        
============== ==============
 POST           Create      
 GET            Read        
 PUT            Update/     
                Replace     
 PATCH          Update/     
                Modify      
 DELETE         Delete      
============== ============== 

StandardEmail:
- Want to search for an email? Want to open an email?  Want to get its
attachments? Want to write and send a new email?

StandardPDF:
- Want to open a PDF? Want to copy out the PDF contents? Want to create a new
PDF?

SecurityLockBox:
- Want to hide your credentials for security purposes?  Holds the encryption
needed to access keys for services on the network.
- Use the python keyring library to store and retrieve encrypted network
credentials.

OneTimePassword:
- Generate a random one-time password for new user accounts.
Hash the password as needed.

Resources
----------
poetry https://python-poetry.org/
flake8 https://flake8.pycqa.org/en/latest/index.html#
jinja2 https://jinja.palletsprojects.com/en/3.1.x/

