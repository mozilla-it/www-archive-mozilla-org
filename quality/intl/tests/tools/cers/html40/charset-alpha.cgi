#!/bin/sh
echo 'Content-Type: text/html; charset='$QUERY_STRING
echo
cat alphabetical.html
