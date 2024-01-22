from gpycraft.fileIO.filecraft import filecraft
from gpycraft.fireStore import firestoreupload
import pandas as pd
import textwrap
io=filecraft()

#print(io.read_dotfile('asdotfile..'))

#df=io.read_dotfile('new..')

#print(io.write_dotfile(df))
#cols=['Units Sold','Sale Price','Gros Sales','Profit']
#io.in_dotfile('Financial Sample.xlsx','asdotfile..',column=cols)



#data=io.dotfile_aspd('new.txt')
#print(data.columns)
#coladd=['Semester']
#print(io.xl_asdotfile(xl_filePath='output_data.xlsx',dotfile_path='collage.txt',column=coladd))
#coladd=['Semester']
#io.dotfile_asxl('new.txt',fieldNumber=4,byPass=True)

#df=io.dotfile_aspd('/workspaces/gpycraft-1.0.0/new.txt')
#io.pd_asdotfile(df)
#print(df.shape[1])
#io.dotfile_asxl('/workspaces/gpycraft-1.0.0/default_dotfile.txt',fieldNumber=df.shape[1],byPass=True)

credentials=[
{
    "type": "service_account",
    "project_id": "realtime-375815",
    "private_key_id": "908d305ab62d292a5053f92038d2bd0456d3daae",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDPq2NqZmYpA9nI\npwWnAakdtFVK9b7f0VE8/sYSzV83gygdcMec4J+pUMg7H/JMOauLt8CCt3E962vy\n6cO49p0w8KEvJlAhcEA8HJRZEGKtFpyeeNPH90J4KlTOb4xTkwjGNTO1NbrAtn8q\nNQ8WfDUNheE2q0TjXJ2RE3A1IW1zcBr/oU6stgpr/mqYImm7/DOFTZKXH0lVYZrA\nIa1yybVSv/uyBSQBzcFxDKm587Ty9VgRaAPLVaCl2U+lSWiF7TbiJPooP/htTLZV\ny2NUzYatW9YceQkn/b7hzvyiMq5y7kT8j3evIn+mA8Ky5QNJ/O/jwXCaT3/U5TDv\nXzi5Irc9AgMBAAECggEAHROKH+Omeien3ohEKlX5L8eICa7Owtez4C5r3UYUBtm+\nTCD2UejBcht1bZHTgwiwFCfuNF8q49iKjMBePw+IgsmuR8O9hHELDV+TBcVdi46W\n7zlLrbvY+qoypZTIuQrlN5tLWhvjwgfLVkWHj0ZkxzfviJACXTMifKWUGFxNztOq\n2IBNk5QNGXcBi3BIKREcUVhfbVBIcxW26lXePiZU7c06p37wJwfc9amC85XTs+ZW\n6M5AM9DLQvgz30d3GVuMR1ntMjfSq9e2shpdHhLQzFbRFACaJIHQmZgG0tKaQG2r\n5Z06X/Stpz4v1jgVtwzZWyXu1jLH6gNuDHNxP6cGoQKBgQDu6ea/i0cN0kCYxkiD\npD8T1rrwFh/hcsB/qfeK1l+y6T1BL94o8Pnge15xzU4sw3w/uV2eqpUN8l1LoAzG\nobFlFOqoRlBHN87eT09onpPHAKWE2BbR6+VfpN7lrGPSsvHKVMEEdL+7t+94KViu\nt6wQPFqpHm+/4QY6Z/hkEDPyzwKBgQDehXWlkImHDFjadLrGXKtXaUCzwQ/C2mwn\nXFYWclOavHo8DO6/FYOkUh/ONoBHaXIZCY5+9d8tC1M0PoD5XANrDY6PJPoLuOJu\noOch+zGFqykcEawkymFvqLi6CIQrynp2GZo5RukxaEffuqcA5ioG74MRsPLGEXZI\n48LZe9coMwKBgQC+xYDelC1BiRDRrQr8Kuu/QKh2y4PbdtDlX+ftMe6qovmpkrp3\nwKwWpwwsHP7+WX5eN/rclmN9BnmeyIdLGJPZHhGeGr9BjvudooDLDkz8C7UfVZkr\nOI0oiTL+/F+dQAw4PuL9Vug+0cnjDkjlAn7fXAIcptQeyGU7wAekhxekGwKBgCOF\nrpg1kJ7Ma8rD46US2g9kL/4CDeAPOkC2Ts/ahFopSGIZtmsupgsvSQCEVsoPnTU9\n/09pNK1eJ3QpnjEwbSND0MQtJPWGGC+M5Bjanrc18aQXdiGRZSiMCKE6Bs9uzUnZ\nIHOQTF2kxgSDKXHNTFw7E/NZCghwdS+BnHNXf6tdAoGAKmV3uoAmx9P83AXhdCU5\ngTPZARgGe8D++Ab0GK3FD4dRTWJzmE9HHLpl9cUD3x8s6eErEN3oF1Cj/n+oBGZf\n3MxZ5YYxMaghsCBSmwNxY0Ftz5SaWesGoGEII2sLRdWp7nV9HvWIZlf5O6NE80We\nViQEFy6zD0/1u5nQQM4SOwQ=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-2zqt0@realtime-375815.iam.gserviceaccount.com",
    "client_id": "113755318902014915745",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-2zqt0%40realtime-375815.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
  }
]

fire_instance=firestoreupload(credentials,storage_bucket='realtime-375815.appspot.com')


#fire_instance.upload_file(local_file_path='/workspaces/gpycraft-1.0.0/new.txt')
#fire_instance.get_file('https://storage.googleapis.com/realtime-375815.appspot.com//workspaces/gpycraft-1.0.0/dossier/privatekey.pem')

columns=['Temperature','Humidity']
io.xl_asdotfile('/workspaces/gpycraft-1.0.0/sensor1.xlsx',column=columns,spacing=10)
#print(io.dotfile_aspd('/workspaces/gpycraft-1.0.0/sensor1.txt'))
#io.dotfile_asxl('/workspaces/gpycraft-1.0.0/sensor1.txt',fieldNumber=2,byPass=True)

""""def spacing(data):
    content = ''
    tuple_data = data.split(' ')
    for data_tuple in tuple_data:
        content += ''.join(f'{data_tuple:<10}')
        final=textwrap.dedent(content)
    return final

with open('/workspaces/gpycraft-1.0.0/sensor1.txt', 'a') as file:
    # Create a string representing your row of data
    data = [
        "20,0 30,1 50,0.\n",
        "20,0 30,2 50,0.\n",
        "20,0 30,3 50,0.\n",
        "20,0 30,4 50,0.\n",
    ]
    
    for values in data:
        data_row = ''.join(values)
        # Modify this line based on your data format
        row = spacing(data_row)
        
        # Append the data to the file
        file.write(row)

"""