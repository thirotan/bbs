#/bin/sh

pip install -r requirements.txt
pip install -r test_requirements.txt

cp config.py instance/

sqlite3 bbs/db.sqlite3 < schema.sql
