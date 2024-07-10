# google-sheet-automation
This is a simple python code to automate google sheet.

## Step-by-Step Guide to Obtain keys.json
### Google Cloud Console
* Go to the Google Cloud Console. Th url is https://console.cloud.google.com/

### Select or Create a Project
* Select an existing project from the project selector dropdown menu at the top of the page, or create a new project by clicking on the project name.
* Go to API's and services or search using seach box and the click on enable apis and services and the enable google sheets api.

### Navigate to IAM & Admin > Service Accounts
* In the left-hand navigation menu, click on IAM & Admin, then click on Service Accounts.

### Create a New Service Account
* Click on Create Service Account at the top of the page.
* Enter a name and description for the service account.
* Click Create.

### Grant Permissions
* After creating the service account, you’ll be prompted to grant permissions to the service account.
* Add the necessary roles (e.g., Project > Editor for full access, or more restricted roles like Google Sheets > Viewer or Editor depending on your needs).
* Click Continue.

### Generate a New Key
* Click Create Key.
* Select JSON as the key type.
* Click Create. This downloads a JSON file containing your service account credentials (keys.json).

### Save the keys.json File
* Save the downloaded keys.json file to a secure location on your computer.


## Important note:
* To finish, copy the email address of the service account (which is a randomly generated email ID representing the IAM user). Next, share the Google Sheets document with this email address and assign the appropriate permissions (viewer, editor, or owner) as needed.
* Also its important to set the perimission of the IAM user correctly while creating the user.
