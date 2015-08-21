import numpy
import math
from scipy import stats
from sklearn import feature_selection
from sklearn import preprocessing
from sklearn import linear_model
from sklearn import svm
from sklearn import linear_model
from sklearn import ensemble
from sklearn.cross_validation import train_test_split
from sklearn import cross_validation
from sklearn import gaussian_process
from sklearn.cross_validation import ShuffleSplit
from sklearn import metrics
from sklearn import grid_search
from sklearn.ensemble import AdaBoostRegressor
from sklearn import tree
x=numpy.loadtxt("cyp3a4_fixpka_property.txt")
sel=feature_selection.VarianceThreshold(threshold=0.0)
x=sel.fit_transform(x)
from sklearn.externals import joblib

def random_forest(training_feature,training_target,test_feature,test_target):
	values=range(10,210,10)
	parameters=[{'n_estimators':values}]
	'''
	dt=grid_search.GridSearchCV(ensemble.RandomForestClassifier(), parameters, cv=5,scoring="accuracy",n_jobs=6)
	dt.fit(training_feature,training_target)
	print dt.score(training_feature, training_target)
	print dt.score(test_feature, test_target)
	#print dt.best_estimator_
	#model=dt.best_estimator_
	#importances=model.feature_importances_
	#for item in importances:
	#	print item
			
	
	values_small=range(1,3)
	parameters=[{'n_estimators':values,'learning_rate':values_small}]
	dt=grid_search.GridSearchCV(ensemble.AdaBoostClassifier(),parameters,cv=5,scoring="accuracy",n_jobs=6)
	dt.fit(training_feature,training_target)
	print dt.score(training_feature, training_target)
	print dt.score(test_feature, test_target)
	print dt.best_estimator_
	
	'''
	parameters=[{'n_estimators':values}]
	dt=grid_search.GridSearchCV(ensemble.ExtraTreesClassifier(),parameters,cv=5,scoring="accuracy",n_jobs=6)
	dt.fit(training_feature,training_target)
	#print dt.score(training_feature, training_target)
	#print dt.score(test_feature, test_target)
	#print dt.best_estimator_
	model=dt.best_estimator_
	importances=model.feature_importances_
	for item in importances:
		print item
	
	
	
	

num=0
while num<1:
	train,test=train_test_split(x,test_size=int(x.shape[0]*0.15))

	feature= train[0:,1:]
	target= train[0:,0]

	feature_test=test[0:,1:]
	target_test= test[0:,0]
	random_forest(feature, target, feature_test,target_test)
	num=num+1

