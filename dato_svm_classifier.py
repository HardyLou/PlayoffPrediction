import graphlab as gl

# Load the data
trainingdata = gl.SFrame('training.csv')
testingdata = gl.SFrame('trainingData/trainingdata_2012.csv')

# Make sure the target is binary 0/1
#trainingdata['team1_win'] = trainingdata['outcome'] > 0

# Make a logistic regression model
model = gl.svm_classifier.create(trainingdata, target='outcome', features=['tm1PER', 'tm1winPerc', 'tm2PER', 'tm2winPerc', 'seasonSeries'])

# Extract the coefficients
coefficients = model['coefficients']         # an SFrame

# Make predictions (as margins, or class)
predictions = model.predict(testingdata)    # Predicts 0/1
#predictions = model.predict(testingdata, output_type='margin')

# Evaluate the model
results = model.evaluate(testingdata)       # a dictionary