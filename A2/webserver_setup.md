A file that contains the sequence of steps/commands required to setup a functioning webserver with a file named comp370_hw2.txt being served from the www root.

## Notes for myself
- Port = communication endpoint for sending and receiving data
    - Identified by a port number to uniquely identify a specific process to which the data should be sent

## Enabling Port 8008 Traffic
1. Go to EC2 Dashboard
2. Select EC2 instance and find its Security Group
3. Click on the Security Groups tab and select the one for your instance
4. Click on Edit Inbound Rules
    i. Add a new inbound rule
    ii. Select Custom TCP Rule
    iii. Set Port Range to 8008
    iii. Set Source to Anywhere
5. Save rule

## Setting up Apache Webserver
1. Create a script called `install.sh`
2. Add the following lines to the script:
    ```
    #!/bin/bash

    sudo apt install apache2
    sudo systemctl start apache2
    sudo systemctl enable apache2
    ```
3. Run the script with `sudo ./install.sh`

## Modifying User Permissions to Modify Apache Webserver
1. Change to root user with `sudo su` command
2. Edit the file `/etc/apache2/ports.conf`
3. Change the line `Listen 80` to `Listen 8008` to indicate the server to listen to port 8008
4. Test the server by opening the page in a browser with the instance and port 8008

## Displaying the Text File
1. Change directory to `/var/www/html` and delete the default `index.html` file
2. Create a new file called `comp370_hw2.txt` and add whatever text you want to it
3. When you open the server in browser, the text file should be displayed