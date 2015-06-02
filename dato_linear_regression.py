import graphlab

# Load the data (From an S3 bucket)
trainingdata =  graphlab.SFrame('training.csv')
testingdata = graphlab.SFrame('trainingData/trainingdata_2012.csv')

# Make a linear regression model
model = graphlab.linear_regression.create(trainingdata, target='outcome', features=['tm1PER', 'tm1winPerc', 'tm2PER', 'tm2winPerc', 'seasonSeries'])

# Extract the coefficients
coefficients = model['coefficients']

# Make predictions
predictions = model.predict(testingdata)

# Evaluate the model
results = model.evaluate(testingdata)