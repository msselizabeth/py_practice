# Exception
class ModelNotTrainedError(Exception):
    pass

class InvalidDataError(Exception):
    pass



# Model Class
class Model:
    def __init__(self, name, dataset, trained=False):
        self.name = name
        self.trained = trained
        self.dataset = dataset
        
    def train(self):
        pass
    
    def predict(self, x):
        if not self.trained:
            raise ModelNotTrainedError("Model should be trained before predicting. Try to tarin model first.")