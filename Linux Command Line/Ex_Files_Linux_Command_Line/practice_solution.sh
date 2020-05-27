#!/bin/bash
# find invalid user info in the auto.log 
wc auth.log 

#less auth.log  


#show content 
cat auth.log | grep "input_userauth_request"

#get 9th value
cat auth.log | grep "input_userauth_request" | awk '{print $9}'

#sort and get unique value 
cat auth.log | grep "input_userauth_request" | awk '{print $9}' | sort -u

# save the users in users.txt 
cat auth.log | grep "input_userauth_request" | awk '{print $9}' | sort -u >users.txt
