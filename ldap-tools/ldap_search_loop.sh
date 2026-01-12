#!/bin/bash
# Description: Queries LDAP for multiple UIDs and unwraps long DN lines.

while IFS= read -r line || [[ -n "$line" ]]; do
  #skip blank lines in input file
    [[ -z "$line" ]] && continue

    ldapsearch -D "cn=root" -w "$LDAP" \
               -s sub -b "ou=ldap,c=us" -L \
               "(&(objectclass=person)(erpswdlastchanged>=20190829130000.000000Z)(uid=$line))" \
               mail uid erpswdlastchanged | perl -p -e 's/\n //g'


done < "/home/userid/uids" > output.txt























done < "/home/userid/uids"
