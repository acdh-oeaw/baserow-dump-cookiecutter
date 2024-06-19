# {{cookiecutter.project_name}} Entities

Automagically export data from [Baserow](https://baserow.io/) 

## initial (local) set up

* create a virtual environment `python -m venv venv` and activate it `source venv/bin/activate`
* update pip to latest version and install needed python packages `pip install -U pip && pip install -r requirements.txt`
* copy/rename `dummy.env` to `secret.env` and add your Baserow credentials

## export the data

* run `source ./export_env_variables.sh` to set your Baserow credentials as environment variables.
* run `python dump_data.py`

## convert dumps to TEI/XML
* adapt the TEI-Header in `tei-template.xml` to your needs
* run `python make_tei.py`

## GitHub-Actions

* Create GitHub secrets called `BASEROW_USER`,  `BASEROW_PW` and `BASEROW_TOKEN` add your Baserow credentials
* Go to the settings of the repository and grant GitHub Actions write permissions for your repo
* Go to GitHub Actions and start the workflow -> the exported data will be checked into your repo
* Be Aware, TEI/XML dumps are not created by the GitHub Action. You'll need to adapt the workflow yourself.

-----
created with [basrow-dump-cookiecutter](https://github.com/acdh-oeaw/transkribus-export-cookiecutter)