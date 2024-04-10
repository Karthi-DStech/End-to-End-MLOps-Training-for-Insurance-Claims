import json
import numpy
import joblib
import time
from azureml.core.model import Model

# from inference_schema.schema_decorators \
#     import input_schema, output_schema
# from inference_schema.parameter_types.numpy_parameter_type \
#     import NumpyParameterType


def init():
    """
    This function loads the Light Gradient Boost model from the file into a global object.
    
    prints
    -------
    The time the model was initialized.
    
    execution
    ---------
    model_path: str
        The path to the model file.
        
    LGBM_MODEL: object
        The global object that stores the model.
    """
    global LGBM_MODEL
   
    model_path = Model.get_model_path("insurance_model")
    LGBM_MODEL = joblib.load(model_path)

    print("model initialized" + time.strftime("%H:%M:%S"))


def run(raw_data, request_headers):
    """
    This function receives the data and passes it through the model for prediction.
    
    parameters
    ----------
    raw_data: json
        The data received from the client to make predictions.
        
    request_headers: dict
        The headers of the request.
        
    prints
    -------
    json info
        Demonstrate how we can log custom data into the 
        Application Insights traces collection.
        
    RequestId: str
        The internally generated value used to correlate a log entry with the 
        Application Insights requests collection.
        
    TraceParent: str
        The HTTP 'traceparent' header may be set by the caller to implement 
        distributed tracing (per the W3C Trace Context proposed specification) 
        and can be used to correlate the request to external systems.
        
    returns
    -------
    dict
        The prediction result.
    """
    data = json.loads(raw_data)["data"]
    data = numpy.array(data)
    result = LGBM_MODEL.predict(data)
    
    # Log the input and output data to appinsights:
    info = {
        "input": raw_data,
        "output": result.tolist()
        }
    print(json.dumps(info))
   
    print(('{{"RequestId":"{0}", '
           '"TraceParent":"{1}", '
           '"NumberOfPredictions":{2}}}'
           ).format(
               request_headers.get("X-Ms-Request-Id", ""),
               request_headers.get("Traceparent", ""),
               len(result)
    ))

    return {"result": result.tolist()}
