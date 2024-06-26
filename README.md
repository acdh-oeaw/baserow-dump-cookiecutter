# baserow-dump-cookiecutter

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to export data from [Baserow](https://baserow.io/)

## what is this for

* Automagically export data from [Baserow](https://baserow.io/) 
* if wanted, converts JSON dumps of your Baserow Database into semantically enriched TEI/XML documents


## Quickstart
* Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.7.0 or higher) by running `pip install -U cookiecutter`

> [!TIP]  
> Install `cookiecutter` inside a [virtual environment](https://docs.python.org/3/library/venv.html). To create a virtuale environment run `python -m venv venv` and activate it by running `source venv/bin/activate`

* To generate a new to export data from [Baserow](https://baserow.io/) project run `cookiecutter gh:acdh-oeaw/baserow-dump-cookiecutter` and answer the following questions, see below:

```json
{
    "projcet_name": "Baserow Export",  // some eyecandy, used only in the created repo's REAMDE.md
    "directory_name": "baserow-entities", // the name of the directory cookiecutter will create the export-repo
    "db_id": 1234567 // the id of the database export, can be changed later any time
} 
```
* change into the new created repo, by default `baserow-entities`
* follow the instructions of the README.me located in `baserow-entities/README.md`

> [!IMPORTANT]
> if you run the export via GH-Actions (which you should) make sure you granted GH-ACTIONS write permissions, e.g. herer https://github.com/organizations{yourorganisation}/settings/actions
