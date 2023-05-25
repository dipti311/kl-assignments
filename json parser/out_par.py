import json
f=open('sample_data.json')
req_data=json.load(f)
req_list=[]
parameters=req_data['parametersList']
#print(req_data)
for item in req_data['parametersList']:
    dict={
       
        "parameterName":item["parameterName"],
        "min_value":item["min"],
        "max_value":item["max"],
        "avg_value":item["avg"]
    }
    req_list.append(dict)
final_list=json.dumps(req_list,indent=4)
with open("output_parser","w") as file:
    file.write(final_list)

f.close()
