#optional change file_path
cd file_path

#optional: setup virtual environment
pip install virtualenv
virtualenv venv

#optional: activate virtual environment
source venv/bin/activate
python translate.py