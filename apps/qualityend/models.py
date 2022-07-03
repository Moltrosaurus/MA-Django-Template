from django.db import models

# Models nach "www.deploymachinelearning.com" Anleitung

# The Endpoint object represents ML API endpoint. / Keeps information about our endpoints
# Attributes:
#       name: Name of the endpoint, it will be used in API URL
#       owner: The string with the owner name,
#       created_at: Date when endpoint was created.

class Endpoint(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)



# The MLAlgorithm represents the ML algorithm pbject. / Keeps information about ML algorithms used in the service
# Attributes:
#       name: Name of algorithm
#       description: short description of how algorithm works
#       code: The code of the algorithm
#       version: Version of the algorithm similar to software versioning
#       owner: name of the owner
#       created_at: date when MLAlgorithm was added
#       parent_endpoint: The reference to the Endpoint

class MLAlgorithm(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


# The MLAlgortihmStatus represent status of the MLAlgorithm which can change during the time.
# Attributes:
#       status: Status of algorithm in the endpoint. Can be:testing, staging, production, ab_testing.
#       active: The boolean flag which point to currently active status.
#       created_by: the name of creator
#       created_at: The date of status creation
#       parent_mlalgorithm: The reference to corrensponding MLAlgorithm


class MLAlgorithmStatus(models.Model):
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name= "status")

# The MLRequest will keep information about all requests to ML algorithms. / will be needed to monitor ML algorithms and run A / B tests.
# Attributes:
#       input_data: The input data to ML algorithm in JSON format
#       full_response: The response of the ML algorithm
#       response: The response of the ML algorithm in JSON format
#       created_at: The date when request was created
#       parent_mlalgorithm: The reference to MLAlgorithm used to compute response

class MLRequest(models.Model):
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)




