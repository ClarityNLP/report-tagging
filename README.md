# report-tagging
Repository for report name tagging

## Installation
1. Setup virtual / production environment
2. `pip install -r requirements.txt`
3. Edit the `config.cfg` file provided with appropriate credentials.

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

## Helpers

**loaddata.py**

Helper script to extract tag mappings from the Report Type Mapper and populate it into the database.

**tag.py**

Helper script which accepts a report name and returns a list of associated tags. Follows the logic of breaking down a report name into bigrams and unigrams and then doing a regex match based on the tag mapping entries stored in the database.
