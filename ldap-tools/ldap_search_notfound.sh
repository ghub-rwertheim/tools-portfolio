#!/bin/bash
# Description: Queries LDAP and collects all those not founds in not_found.txt.

while IFS= read -r line || [[ -n "$line" ]]; do

    # Skip truly empty lines
    [[ -z "$line" ]] && continue

    # Capture the output of the search into a variable
    # only look for the 'dn' to keep the check lightweight

    result=$(ldapsearch -D "cn=root" -w "$LDAP" \
               -s sub -b "ou=ldap,c=us" -L \
               "(&(objectclass=person)(uid=$line))" dn | grep "dn:")

     # If the result variable is empty, the user was not found
    if [[ -z "$result" ]]; then
        echo "$line" >> not_found.txt
    fi

done < "/home/wertheimr-ipa/uids"
