#! /bin/bash 

domain_name="domain_name"
username="username"
password="password"
file_name="userdata.json"

ftp -np $domain_name >ftp_new.log<<END_SCRIPT
verbose
quote USER $username
quote PASS $password
cd /public_html
put $file_name
quit
END_SCRIPT
exit 0