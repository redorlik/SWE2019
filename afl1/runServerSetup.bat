:: Starts the application in docker containers
docker-compose up --build -d

:: If you dont delete volumes, you can comment out line below
:: or when the db has been set up
docker-compose run web /usr/local/bin/python create_db.py

:: Opens Chrome at std docker-toolbox ip
start chrome http://192.168.99.100:80

PAUSE

:: If you dont want to delete volumes after exit, remove the "-v"
:: docker-compose down -v

:: Line below doesn't delete volumes
docker-compose down