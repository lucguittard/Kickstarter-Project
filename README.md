# Model API

The model API of this project takes a JSON GET string and returns a rank-measure prediction of a campaigns success relative to other campaigns. 

When running the model takes JSON input of the following format: {'backers_count': integer, 'goal': float, 'spotlight': boolean, 'staff_pick': boolean}

To run the model and recieve a prediction, refer to /model-and-api/app/app.py. First run the app.py file in a terminal, go to the locally-hosted URL that gets generated, and navigate to the /api page. In a separate terminal window, run the follwing: 
$ curl -X GET <"your_URL_here/api"> -H "Content-Type: application/json" --data '{"backers_count":"your_integer", "goal":"your_float", "spotlight":"your_boolean", "staff_pick":"your_boolean"}'


# Getting the Model

The work involved in arriving at a model -- exploratory visualizations, feature engineering, model exploration and optimization, as well its pickling -- can be found in the DSproject3_jupyter.ipynb in the /model-and-api/notebooks/subdirectory. 


# Setting up a PostgreSQL Database

A sample setup of a PostgreSQL Database can be found in the db_pg.py file in the /database-starter subdirectory. 