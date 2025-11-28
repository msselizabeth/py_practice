from base import Model

# Exception
class ModelNotTrainedError(Exception):
    pass

class InvalidDataError(Exception):
    pass


class LinearRegressionModel(Model):
    def train(self):
        if not self.dataset:
            raise InvalidDataError("Please provide a dataset.")
        self.bias = sum(self.dataset) / len(self.dataset)
        self.trained = True
        
    def predict(self, x=None):
        if not self.trained:
            raise ModelNotTrainedError("Model is not trained yet.")
        return self.bias
