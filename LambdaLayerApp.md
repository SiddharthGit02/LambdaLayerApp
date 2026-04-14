Create a Lambda Function
I created a function with runtime Python ver 3.12
-------------
Copy code from Lambda.py to Lambda Function
local Python code is in main.py
-------------
Now we will create layer, we need numpy and pandas libraries to run the code.
We can use AWS managed layer can our custom layer.
-------------
For Custom Layer, we will need Docker installed
In Powershell, run below command

`docker run -v "${PWD}:/var/task" "public.ecr.aws/sam/build-python3.12" /bin/sh -c "pip install -r requirements.txt -t python/lib/python3.12/site-packages/; exit"`

`Compress-Archive -Path python -DestinationPath my_pandas_layer_py312.zip`
--------------
Upload file in S3 bucket
Then create a layer in Lambda, 
Select option for S3, copy file URL from S3 bucket
In compatibility - `x86` and runtime `Python3.12`
---------------
In Lambda Function, add custom layer
then run Lambda code.
