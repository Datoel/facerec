from facerec.feature import AbstractFeature
from facerec.classifier import AbstractClassifier

class PredictableModel(object):
	def __init__(self, feature, classifier):
		if not isinstance(feature, AbstractFeature):
			raise TypeError("feature must be of type AbstractFeature!")
		if not isinstance(classifier, AbstractClassifier):
			raise TypeError("classifier must be of type AbstractClassifier!")
		
		self.feature = feature
		self.classifier = classifier
	
	def compute(self, X, y):
		features = self.feature.compute(X,y)
		self.classifier.compute(features,y)

	def predict(self, X):
		q = self.feature.extract(X)
		return self.classifier.predict(q)