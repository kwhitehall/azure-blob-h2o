import h2o
import os
import sys

# Example Python 3 script for the Ubuntu Azure DSVM showing h2o data access to Azure Blob Storage.
#
# $ pip list | grep h2o -> h2o (3.13.0.369)
# $ python h2o_example.py
#
# Chris Joakim, Microsoft, 2018/03/05

try:
    h2o.init(nthreads=2, max_mem_size=4)

    iris_data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    print('reading the iris data from: ' + iris_data_url)
    df1 = h2o.import_file(iris_data_url)
    df1.describe()

    # Environment variable 'STORAGE_URL_QUERY_STR' contains a shared access signature (SAS)
    # that was created for the 'h2o' container in the 'cjoakimh2ostorage' account.
    # The SAS key allows for read access to the containers contents, and not just an individual file.
    # The SAS key was generated with the Azure Storage Explorer -> create container, right-mouse, Get Shared Access Signature...
    # This particular key was given a 1-year expiration date.
    #
    # See https://azure.microsoft.com/en-us/features/storage-explorer/
    # See https://docs.microsoft.com/en-us/azure/storage/common/storage-dotnet-shared-access-signature-part-1

    storage_url_query_string = os.environ['STORAGE_URL_QUERY_STR']
    print('storage_url_query_string: ' + storage_url_query_string)

    # Form the URL for the 'iris.data' blob in the 'h2o' container within the 'cjoakimh2ostorage'
    # storage account; append the query string with signature.
    blob_url = 'https://cjoakimh2ostorage.blob.core.windows.net/h2o/iris.data' + storage_url_query_string
    print('reading the (identical) iris data from: ' + blob_url)
    df2 = h2o.import_file(blob_url)
    df2.describe()
except:
    print("exception encountered: ", sys.exc_info()[0])

h2o.cluster().shutdown()
