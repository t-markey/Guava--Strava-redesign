# Guava

A redesign of the popular platform Strava, used by many to upload  GPS Data from workouts to be shared with friends

## Features

* Login Authentication
* Database to store posts & workout logs
* Users can upload GPS data from
* Visual map view of your runs from GPS data

## Examples
Activity form and Gps data rendered into html with google maps 

![Activity Form](/guava/examples/example.png)
![Map](/guava/examples/map_example.png)

## Usage / Status
-In Process of being hosted-
-Still working out some issues with the database and gps files-
-Currently only accepted .fit files for gps ( from Garmin )-

```bash
pipenv shell
export FLASK_APP=testing.py
flask run
```


## Credits
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

https://pypi.org/project/fitparse/1.0.0/

https://github.com/mcandocia/examples

https://maxcandocia.com/article/2017/Sep/22/converting-garmin-fit-to-csv/



## License
[GPL3](https://choosealicense.com/licenses/gpl-3.0/)
