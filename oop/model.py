from collections import UserList, UserDict
from dataclasses import dataclass


# Exception
class ModelNotTrainedError(Exception):
    pass

class InvalidDataError(Exception):
    pass


#DataSet 
class DataSet(UserList):
    def mean(self):
        mean = sum(self.data) / len(self.data)
        return mean
    
    def normalize(self):
        min_val = min(self.data)
        max_val = max(self.data)
        res = [(num - min_val) / (max_val - min_val) for num in self.data]
        self.data = res
    
    def add_value(self, new_value):
        if not isinstance(new_value, int) or not isinstance(new_value, float):
            raise InvalidDataError("The value is not valid.")
        self.data.append(new_value)



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
 
# inheritance class         
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


# Experiment
@dataclass
class Experiment():
    id: int
    model: Model
    dataset_size: int
    is_successful: bool
    
# Experiment manager
class ExperimentManager(UserDict):
    def add_exp(self, exp):
        self.data[exp.id] = exp
    
    def get_all(self):
        return self.data
    
    def get_successful(self):
        return [exp for exp in self.data.values() if exp.is_successful] 
    
    
data = DataSet([1, 2, 3, 4])
data.normalize()

model = LinearRegressionModel("baseline", data)
model.train()
print(model.predict())

exp1 = Experiment(id=1, model=model, dataset_size=len(data), is_successful=True)
exp2 = Experiment(id=2, model=model, dataset_size=len(data), is_successful=True)
exp3 = Experiment(id=3, model=model, dataset_size=len(data), is_successful=False)



manager = ExperimentManager()
manager.add_exp(exp1)
manager.add_exp(exp2)
manager.add_exp(exp3)



print(f"All experiments: {manager.get_all()}")
print(f"Only successful experiments {manager.get_successful()}")

