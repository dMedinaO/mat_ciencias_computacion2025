from sklearn.metrics import (accuracy_score, recall_score, precision_score, 
                             f1_score, matthews_corrcoef, roc_auc_score)

from sklearn.metrics import (r2_score, root_mean_squared_error, mean_absolute_error)

class UtilsFunctions:

    @classmethod
    def get_regression_metrics(cls, y_true, y_pred):

        return {
            "r2" : r2_score(y_true, y_pred),
            "RMSE" : root_mean_squared_error(y_true, y_pred),
            "MAE" : mean_absolute_error(y_true, y_pred),
        }
    
    @classmethod
    def get_metrics(cls, y_true, y_pred, average="weighted"):

        return {
            "accuracy" : accuracy_score(y_true, y_pred),
            "recall_score" : recall_score(y_true, y_pred, average=average),
            "precision_score" : precision_score(y_true, y_pred, average=average),
            "f1_score" : f1_score(y_true, y_pred, average=average),
            "mcc" : matthews_corrcoef(y_true, y_pred),
        }
    
    @classmethod
    def get_roc_auc(cls, y_true, y_prob):

        return roc_auc_score(y_true, y_prob)