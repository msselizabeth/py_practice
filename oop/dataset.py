from collections import UserList, UserDict


class InvalidDataError(Exception):
    pass

class NormalizeError(Exception):
    pass

# DataSet
class DataSet(UserList):
    def __init__(self, initial_data=None):
        super().__init__(initial_data or [])
        self.encoders = {}       
        self.normalization_stats = {}  
        self.is_encoded = False
        self.is_normalized = False
    
    def add_sample(self, row: dict):
        """Add a new row to dataset"""
        if type(row) is not dict:
            raise TypeError("Object must be a dictionary")
        self.data.append(row)

    def encode_categorical(self) -> tuple:
        """
        Find all fields with str type → create mapping → change strings to nums. Modyfies self and saves encoders
        """
        if self.is_encoded:
            raise NormalizeError("Dataset is already encoded.")
        # find str fields
        string_fields = set()
        for item in self.data:
            for key, value in item.items():
                if isinstance(value, str):
                    string_fields.add(key)
    
        # save mappings
        encoders = {}
        for col in string_fields:
            #  get unique values from dataset
            unique_values = list(set(i.get(col) for i in self.data))
            mapping = {value: index for index, value in enumerate(unique_values)}
            encoders[col] = mapping
            # update string values to numbers
            for row in self.data:
                row[col] = encoders[col][row[col]]
                
        self.is_encoded = True
        self.encoders = encoders


    def normalize(self, feature_names: list[str]) -> tuple:
        """
        Normalize specific num values. Returns updated dataset and stats
        """
        
        if self.is_normalized:
            raise NormalizeError("Dataset is alredy normalized")
        stats = {}
        for feature in feature_names:
            values = [item[feature] for item in self]
            min_val = min(values)
            max_val = max(values)
            # check if we need to normalize -> edge case
            if min_val == max_val:
                self.stats[feature] = {
                    "min": min_val,
                    "max": max_val,
                    "note": "all values in this feature are identical — normalization skipped"}
                continue
            # save min and max to denormalize
            stats[feature] = {
            "min": min_val,
            "max": max_val
            }
            # change values in dataset to normalized
            for item in self:
                item[feature] = (item[feature] - min_val) / (max_val - min_val)
                
        self.is_normalized = True
        self.normalization_stats = stats
            
    def to_X_y(self, label_name="label"):
        """Split into  X (features) and Y (labels)"""
        
        X = []
        Y = []
        for item in self:
            if label_name not in item:
                raise KeyError(f"Label '{label_name}' not found in data item: {item}")
            Y.append(item[label_name])
            features = []
            for key, value in item.items():
                if key != label_name:
                    features.append(value)
            X.append(features)
            
        self.feature_names = [key for key in self[0].keys() if key != label_name]
        self.label_name = label_name
    
        return(X, Y)
    
    
    # def mean(self):
    #     mean = sum(self.data) / len(self.data)
    #     return mean

       



data = DataSet([
        {
            "age": 25,
            "education": "Bachelor",
            "salary": 2000,
            "city": "Toronto",
            "label": "Low",
        },
        {
            "age": 32,
            "education": "Master",
            "salary": 3500,
            "city": "Toronto",
            "label": "Medium",
        },
        {
            "age": 45,
            "education": "PhD",
            "salary": 8000,
            "city": "New York",
            "label": "High",
        },
        {
            "age": 29,
            "education": "Bachelor",
            "salary": 2800,
            "city": "London",
            "label": "Low",
        },
        {
            "age": 38,
            "education": "Master",
            "salary": 5100,
            "city": "London",
            "label": "Medium",
        },
        {
            "age": 52,
            "education": "PhD",
            "salary": 10000,
            "city": "Toronto",
            "label": "High",
        },
    ])

data.encode_categorical()
print(data)
data.normalize(['age', 'salary'])
print(data)
X, Y = data.to_X_y("label")
print(X)
print(Y)


print(data.encoders)



        
        

    
