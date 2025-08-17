import json
import requests
import pandas as pd

def custom_labmda(event, context):
    print("Event Data :",event)
    response = requests.get("https://google.com/")
    print(response.text)
    print(response.status_code)

    d={'col1':[1,2],'col2':[3,4]}
    df= pd.DataFrame(data=d)
    print(df)
    print("DataFrame created successfully!")

    return {
        'statusCode': 200,
        'body': json.dumps('Custom Lambda function executed successfully!')
    }