# report-tagging
Repository for report name tagging

## Installation
1. Setup virtualenv / production environment
2. `pip install -r requirements.txt`

## Running the app
`python app.py`

## API usage

**About:**

Accepts a report name and returns tags based on the given report name. Currently being down by breaking down the report name into smaller components and doing regex matchings against a stored mapping. 

**Parameters:** Report name (Mandatory)

**Usage:**  

```
~reportTagging?report=<REPORT NAME>
```

**Return Type:** JSON. Contains a list of associated tags.
