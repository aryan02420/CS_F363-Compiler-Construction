#!/bin/bash

set -e

echo "What are the lengths of lexemes that match the patterns in your lexer design?"
echo "[1, ∞)"

echo "How many distinct patterns are there in your lexer design?"
cat scanner.py | grep -o -P "(([^%a-z]r\')|(IDENT\[\'))(.*)\'" | sed -E "s/.*'(.*)'.*/\1/g" | uniq | wc -l

echo "How many distinct token types are there in your lexer design?"
cat scanner.py | grep -o -P "tokens = {[A-Z ,]*}" | grep -o -P "[A-Z]+" | uniq | wc -l

echo "How many of these token types are encoded into an enumerated type or a number?"
echo "..."

echo "How many of these token types are just the lexemes themselves?"
# cat scanner.py | grep -o -P "IDENT\[\'.*\'\] = [A-Z]+" | tr '[:upper:]' '[:lower:]' | sed "s/[a-z]+\[\'[a-z]+\'\].*/lol/g"
cat scanner.py | grep -oP "\] = [A-Z]+" | uniq -u | wc -l