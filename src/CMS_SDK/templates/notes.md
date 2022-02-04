

To use the Cisco Meeting Server API you need to follow these steps:

    Connect via HTTPS via the same TCP ports as you would use to access the Web Admin Interface - which is typically 443.
    Enter your credentials to login to MMP.
    Configure a new 'api' user with a username and password, Set them using the MMP command user: add <username> (api).

This command creates a new api user and prompts for a password for the user which must be entered twice to ensure that the intended password is configured.

On first login, the user will be asked to configure a new password. You must provide these credentials in order to use the API.


https://ciscocms.docs.apiary.io/#introduction/general-structure-of-methods
https://developer.cisco.com/docs/cisco-meeting-server/#!getting-started-with-apis
https://www.cisco.com/c/dam/en/us/td/docs/conferencing/ciscoMeetingServer/Reference_Guides/Version-3-0/Cisco-Meeting-Server-API-Reference-Guide-3-0.pdf


https://sphinx-rtd-tutorial.readthedocs.io/en/latest/install.html
