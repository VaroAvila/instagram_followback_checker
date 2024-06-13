# instagram_followback_checker
Simple local and secure script to check who is not following you back from your following list. 

I have seen over-engineered solutions to get the list of people not following your Instagram account back: from complex web scraping approaches to shady services that go against the Instagram's terms of service and ask for your login credentials. That's why I developed a simple script that uses your Instagram information locally and does not require a login or access to your credentials. This script only works for the accounts you own/have access to (you need to export your data from the account center).

## How to Use

### Step 1: Export Your Instagram Data
1. Log in to your Instagram account.
2. Go to your profile and click on the settings icon.
3. Select "Privacy and Security".
4. Scroll down to "Data Download" and click "Request Download". (To simplify the process you can choose to download only your connections/follower/ing information data)
   Alternatively you can go directly to this link https://www.instagram.com/download/request/
5. Choose the format (JSON) and click "Next".
6. Make sure to select the right range of time for the downloaded data (e.g.: {since the creation of the account - today})
7. Enter your password and click "Request Download".
8. Wait for the email from Instagram with the download link.
9. Download and unzip the file.

### Step 2: Locate the Followers and Following Files
1. Inside the downloaded data folder, navigate to the `connections` folder.
2. Find the path to the `followers_1.json` and `following.json` files.

### Step 3: Set Up the Python Script
1. Create a new directory for the project.
2. Inside this directory, clone this repository with "git clone https://github.com/VaroAvila/instagram_followback_checker.git"
3. Open the "compare_followers.py" script with a text editor
4. Replace "path_to_your_directory" with the right paths to the followers and following files. Make sure the name of the file is correct too.
5. Do the same with the path where you want to export the .txt file with the results. 

    e.g:
          followers_file = os.path.join('C:\\Users\\User\\Desktop\\connections\\followers_and_following', 'followers_1.json') # followers file

          following_file = os.path.join('C:\\Users\\User\\Desktop\\connections\\followers_and_following', 'following.json')   # following file

          output_file = os.path.join('C:\\Users\\User\\Desktop', 'not_following_back.txt')   # output .txt file

### Step 4: Execute the Script

1. Open a terminal (e.g.: powershell terminal as admin in Windows)
2. Go to the folder where your script is
3. Run "python compare_followers.py" on the console

### Step 5: Output

   The program will output the list of all the accounts you are following that are not following you back. It will also export it to a .txt file in the path you provided on step 3. 

