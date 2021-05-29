import ipfshttpclient
import config

client = ipfshttpclient.connect(config.ipfs)


def upload_file(file):
    uploaded_file=client.add(file)
    return(uploaded_file['Hash'])

def get_url(file_hash):
    url='/ipfs/'+file_hash
    return(url)