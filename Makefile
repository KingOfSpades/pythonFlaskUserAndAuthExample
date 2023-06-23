run:
	FLASK_APP=flaskr/app.py \
	flask run \
	--debug \
	--cert=adhoc

database:
	python3 flaskr/models.py

clean_database:
	rm flaskr/instance/myDB.db