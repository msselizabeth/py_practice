from base import Model

# Exception
class ModelNotTrainedError(Exception):
    pass

class InvalidDataError(Exception):
    pass


class KNN(Model):
    def __init__(self, name, k=3):
        super()