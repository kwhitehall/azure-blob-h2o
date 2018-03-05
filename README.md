# azure-blob-h2o

Example of how to access Azure Blob Storage from  a H2O Python script running on
an Azure Ubuntu Data Science Virtual Machine (DSVM).

# Azure Storage Explorer

## Links

- https://azure.microsoft.com/en-us/features/storage-explorer/
- https://docs.microsoft.com/en-us/azure/storage/common/storage-dotnet-shared-access-signature-part-1

First, use the Azure Storage Explorer to create a SAS (shared access signature) key
to be used to access the Blob Container from H2O per the following screen-shots:

Open Storage Explorer and select your container.  Then right-mouse it, and
select "Get Shared Access Signature...".

![image 1](img/Azure-Storage-Explorer-1.png "")

Specify the timespan of the SAS key; I gave this one a 1-year expiration:

- ![image 2](img/Azure-Storage-Explorer-2.png "")

Capture both the value of the URL and the Query String.  The **STORAGE_URL_QUERY_STR**
environment variable on the DSVM needs to be set to the value of the query string.

- ![image 3](img/Azure-Storage-Explorer-3.png "")

# Running the Python 3 script on the DSVM

**h2o_example.py** does two things:
- Loads the standard iris dataset from a URL
- Loads the exect same iris dataset from Azure Blob Storage using the SAS key
- "describes" each dataframe to validate their sameness

Since th **h2o** library is already installed in the DSVM you don't need to
install it yourself via conda or pip.

For this example script, set environment variable **STORAGE_URL_QUERY_STR** to be the value
of your SAS key.

Program execution and output is shown below:

```
cjoakim@cjoakimdsvm:~/github/azure-hcm$ python h2o_example.py
Checking whether there is an H2O instance running at http://localhost:54321..... not found.
Attempting to start a local H2O server...
  Java Version: openjdk version "1.8.0_151"; OpenJDK Runtime Environment (build 1.8.0_151-8u151-b12-0ubuntu0.16.04.2-b12); OpenJDK 64-Bit Server VM (build 25.151-b12, mixed mode)
  Starting server from /anaconda/envs/py35/lib/python3.5/site-packages/h2o/backend/bin/h2o.jar
  Ice root: /tmp/tmpijw5ciac
  JVM stdout: /tmp/tmpijw5ciac/h2o_cjoakim_started_from_python.out
  JVM stderr: /tmp/tmpijw5ciac/h2o_cjoakim_started_from_python.err
  Server is running at http://127.0.0.1:54321
Connecting to H2O server at http://127.0.0.1:54321... successful.
Warning: Your H2O cluster version is too old (6 months and 20 days)! Please download and install the latest version from http://h2o.ai/download/
--------------------------  ----------------------------------------
H2O cluster uptime:         03 secs
H2O cluster version:        3.13.0.369
H2O cluster version age:    6 months and 20 days !!!
H2O cluster name:           H2O_from_python_cjoakim_np7wnk
H2O cluster total nodes:    1
H2O cluster free memory:    3.556 Gb
H2O cluster total cores:    4
H2O cluster allowed cores:  2
H2O cluster status:         accepting new members, healthy
H2O connection url:         http://127.0.0.1:54321
H2O connection proxy:
H2O internal security:      False
H2O API Extensions:         XGBoost, Algos, AutoML, Core V3, Core V4
Python version:             3.5.2 final
--------------------------  ----------------------------------------
reading the iris data from: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
Parse progress: |█████████████████████████████████████████████████████████████████████████████| 100%
Rows:150
Cols:5


         C1                  C2                  C3                  C4                   C5
-------  ------------------  ------------------  ------------------  -------------------  -----------
type     real                real                real                real                 enum
mins     4.3                 2.0                 1.0                 0.1
mean     5.843333333333334   3.0539999999999994  3.758666666666667   1.1986666666666668
maxs     7.9                 4.4                 6.9                 2.5
sigma    0.8280661279778637  0.4335943113621737  1.7644204199522624  0.7631607417008414
zeros    0                   0                   0                   0
missing  0                   0                   0                   0                    0
0        5.1000000000000005  3.5                 1.4000000000000001  0.2                  Iris-setosa
1        4.9                 3.0                 1.4000000000000001  0.2                  Iris-setosa
2        4.7                 3.2                 1.3                 0.2                  Iris-setosa
3        4.6000000000000005  3.1                 1.5                 0.2                  Iris-setosa
4        5.0                 3.6                 1.4000000000000001  0.2                  Iris-setosa
5        5.4                 3.9000000000000004  1.7000000000000002  0.4                  Iris-setosa
6        4.6000000000000005  3.4000000000000004  1.4000000000000001  0.30000000000000004  Iris-setosa
7        5.0                 3.4000000000000004  1.5                 0.2                  Iris-setosa
8        4.4                 2.9000000000000004  1.4000000000000001  0.2                  Iris-setosa
9        4.9                 3.1                 1.5                 0.1                  Iris-setosa
storage_url_query_string: ?st=2018-03-02T10%3A13%3A00Z&se=2019-03-03T10%3A13%3A00Z&sp=rl&sv=2017-04-17&sr=c&sig=scDAsMJp93QdJcvxVBJWTNfa9vouiv0tU%2FC%2Fo%2BO02UA%3D
reading the (identical) iris data from: https://cjoakimh2ostorage.blob.core.windows.net/h2o/iris.data?st=2018-03-02T10%3A13%3A00Z&se=2019-03-03T10%3A13%3A00Z&sp=rl&sv=2017-04-17&sr=c&sig=scDAsMJp93QdJcvxVBJWTNfa9vouiv0tU%2FC%2Fo%2BO02UA%3D
Parse progress: |█████████████████████████████████████████████████████████████████████████████| 100%
Rows:150
Cols:5


         C1                  C2                  C3                  C4                   C5
-------  ------------------  ------------------  ------------------  -------------------  -----------
type     real                real                real                real                 enum
mins     4.3                 2.0                 1.0                 0.1
mean     5.843333333333334   3.0539999999999994  3.758666666666667   1.1986666666666668
maxs     7.9                 4.4                 6.9                 2.5
sigma    0.8280661279778637  0.4335943113621737  1.7644204199522624  0.7631607417008414
zeros    0                   0                   0                   0
missing  0                   0                   0                   0                    0
0        5.1000000000000005  3.5                 1.4000000000000001  0.2                  Iris-setosa
1        4.9                 3.0                 1.4000000000000001  0.2                  Iris-setosa
2        4.7                 3.2                 1.3                 0.2                  Iris-setosa
3        4.6000000000000005  3.1                 1.5                 0.2                  Iris-setosa
4        5.0                 3.6                 1.4000000000000001  0.2                  Iris-setosa
5        5.4                 3.9000000000000004  1.7000000000000002  0.4                  Iris-setosa
6        4.6000000000000005  3.4000000000000004  1.4000000000000001  0.30000000000000004  Iris-setosa
7        5.0                 3.4000000000000004  1.5                 0.2                  Iris-setosa
8        4.4                 2.9000000000000004  1.4000000000000001  0.2                  Iris-setosa
9        4.9                 3.1                 1.5                 0.1                  Iris-setosa
H2O session _sid_9884 closed.
cjoakim@cjoakimdsvm:~/github/azure-hcm$
```
