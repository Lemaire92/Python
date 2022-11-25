import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=-'',username=' ' ,password=' ',allow_agent=False,look_for_keys=False)

sftp = client.open_sftp()
sftp.put('','')
sftp.close()