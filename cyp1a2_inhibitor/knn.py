import numpy
from scipy import stats
from sklearn import feature_selection
from sklearn import preprocessing
from sklearn import ensemble
from sklearn.cross_validation import train_test_split
from sklearn import cross_validation
from sklearn import metrics
from sklearn import grid_search
from sklearn import neighbors

x=numpy.loadtxt("volume_property.txt")
sel=feature_selection.VarianceThreshold(threshold=0.0)
x=sel.fit_transform(x)

def nearest_neighbors(training_feature,training_target,test_feature,test_target):
	values=range(1,10,1)
	
	parameters=[{'n_neighbors':values}]
	neigh=grid_search.GridSearchCV(neighbors.KNeighborsRegressor(weights='distance'), parameters, cv=5,scoring="mean_squared_error",n_jobs=6)
	
	neigh.fit(training_feature,training_target)
	slope,intercept,r_value,p_value,std_err=stats.linregress(training_target,neigh.predict(training_feature))
	print r_value
	
	slope,intercept,r_value,p_value,std_err=stats.linregress(test_target,neigh.predict(test_feature))
	print r_value
	print neigh.best_params_
	num=0
num=0
while num<10:
	train,test=train_test_split(x,test_size=int(x.shape[0]*0.15))

	feature= train[0:,1:]
	target= train[0:,0]

	feature_test=test[0:,1:]
	target_test= test[0:,0]
	nearest_neighbors(feature, target, feature_test,target_test)
	num=num+1
	
	print "------------------------"


