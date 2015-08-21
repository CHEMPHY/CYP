import numpy
from scipy import stats
from sklearn import feature_selection
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn import cross_validation
from sklearn import metrics
from sklearn import grid_search
from sklearn import svm
x=numpy.loadtxt("cyp3a4_fixpka_property.txt")
sel=feature_selection.VarianceThreshold(threshold=0.0)
x=sel.fit_transform(x)
x=preprocessing.MinMaxScaler().fit_transform(x)

print x

def svm_run(training_feature,training_target,test_feature,test_target):
	values=numpy.logspace(-5,5,11,base=2)
	parameters=[{'C':values,'gamma':values}]

	svm_svc=grid_search.GridSearchCV(svm.SVC(kernel='rbf'), parameters, cv=5,scoring="mean_squared_error",n_jobs=6)
	
	svm_svc.fit(training_feature,training_target)
	print svm_svc.score(training_feature, training_target)
	print svm_svc.score(test_feature, test_target)
	print svm_svc.best_estimator_

num=0
while num<10:
	train,test=train_test_split(x,test_size=int(x.shape[0]*0.15))
	feature= train[0:,1:]
	target= train[0:,0]
	feature_test=test[0:,1:]
	target_test= test[0:,0]

	svm_run(feature, target, feature_test,target_test)
	num=num+1

