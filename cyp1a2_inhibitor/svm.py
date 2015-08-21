import numpy
from scipy import stats
from sklearn import feature_selection
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn import cross_validation
from sklearn import metrics
from sklearn import grid_search
from sklearn import svm
x=numpy.loadtxt("volume_property.txt")
sel=feature_selection.VarianceThreshold(threshold=0.0)
x=sel.fit_transform(x)
x=preprocessing.MinMaxScaler().fit_transform(x)

def svm_run(training_feature,training_target,test_feature,test_target):
	values=numpy.logspace(-5,5,11,base=2)
	parameters=[{'C':values,'gamma':values,'epsilon':values}]

	svm_svr=grid_search.GridSearchCV(svm.SVR(kernel='rbf'), parameters, cv=5,scoring="mean_squared_error",n_jobs=6)
	
	svm_svr.fit(training_feature,training_target)
	slope,intercept,r_value,p_value,std_err=stats.linregress(training_target,svm_svr.predict(training_feature))
	print r_value
	
	
	slope,intercept,r_value,p_value,std_err=stats.linregress(test_target,svm_svr.predict(test_feature))
	print r_value
	

	print svm_svr.best_params_
	num=0
#for i in svm_svr.predict(feature_test):
	#print i,target_test[num]
#	num=num+1




num=0
while num<10:
	train,test=train_test_split(x,test_size=int(x.shape[0]*0.15))
	feature= train[0:,1:]
	target= train[0:,0]
	feature_test=test[0:,1:]
	target_test= test[0:,0]

	svm_run(feature, target, feature_test,target_test)
	num=num+1

