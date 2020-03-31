# Convert your excel and csv as API

It can read from excel and csv file url

Documentation
-----------
Please open [https://excel2api.herokuapp.com/docs](https://excel2api.herokuapp.com/docs)

Documentation explanation:
* `host/v1/api/excel`
    * query string `sheet_name` is sheet name to open
    * query string `sheet_url` is url where excel will be open
    * query string `row_range` is range row:
        * `1:50` mean will display data from row 1 to 49
        * `:50` mean will display data from first to 49
        * `50` mean will display data from first to 49
    * query string `column_range` is range row:
        * `date` mean will display only column `date`
        * `date,age` mean will display only column `date` and `age`

* `host/v1/api/csv`
    * query string `sheet_url` is url where csv will be open
    * query string `row_range` is range row:
        * `1:50` mean will display data from row 1 to 49
        * `:50` mean will display data from first to 49
        * `50` mean will display data from first to 49
    * query string `column_range` is range row:
        * `date` mean will display only column `date`
        * `date,age` mean will display only column `date` and `age`
    
Manual Installation
------------
* Need python 3.7+
* Backed by python [fast api](https://github.com/tiangolo/fastapi)
* `pip install -r requirements.txt`
* Run with command `uvicorn app:app --reload --port 8000`

Manual Installation
------------
* Need python 3.7+
* `pip install -r requirements.txt`
* change configuration in `conf/.env.yaml`
* change `env` in `conf/.env.yaml`
* Backed by python [fast api](https://github.com/tiangolo/fastapi)

Running unit test
------------
```shell script
  python -m unittest discover -v -s ./tests
```


Contribution
------------
We are always happy to have new contributions. 
We have `marked issues good for anyone looking to get started`, and welcome.