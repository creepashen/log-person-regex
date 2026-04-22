# log-person-regex
Simple Python project to parse and extract structured information from unstructured log data using regex

# Log Parser Regex

A simple Python project that extracts structured data from unstructured log strings using regular expressions.

## Features

- Extracts user, id, and action from log text
- Works with messy log formats
- Ignores extra fields like INFO, ERROR, WARN, time, and code
- Returns clean structured output as tuples

## How it works

The script uses Python's `re` module to match patterns in text and extract useful information.

It focuses on three fields:
- user
- id
- action

## Example
### Input

[INFO] user=Ahmed id=A12 action=login time=10:30
[ERROR] user=Sara id=B77 action=fail_login code=404

```python

###output
[
 ('Ahmed', 'A12', 'login'),
 ('Sara', 'B77', 'fail_login')
]
