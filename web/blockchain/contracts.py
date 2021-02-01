from blockchain import blockchain

web3,chain_id=blockchain.connect_blockchain()
contract=blockchain.load_contract()

##################################################################################################

def addPatient(patient_account,aadhaar_id):
    trxn=contract.functions.addPatient(aadhaar_id).buildTransaction({
        'chainId':chain_id,
        'gas':700000,
        'gasPrice':web3.toWei('50','gwei'),
        'nonce':web3.eth.getTransactionCount(patient_account.address)
    })
    signed_trn = web3.eth.account.sign_transaction(trxn, private_key=patient_account.privateKey)
    return(web3.eth.sendRawTransaction(signed_trn.rawTransaction))

def patientInfo(patient_account):
    return(contract.functions.patientInfo().call(transaction={"from":patient_account.address}))

def addReport(file_name,file_hash,patient_account):
    trxn=contract.functions.addReport(file_name,file_hash).buildTransaction({
        'chainId':chain_id,
        'gas':700000,
        'gasPrice':web3.toWei('50','gwei'),
        'nonce':web3.eth.getTransactionCount(patient_account.address)
    })
    signed_trn = web3.eth.account.sign_transaction(trxn, private_key=patient_account.privateKey)
    return(web3.eth.sendRawTransaction(signed_trn.rawTransaction))

def grantAccessToDoctor(doctor_address,patient_account):
    trxn=contract.functions.grantAccessToDoctor(doctor_address).buildTransaction({
        'chainId':chain_id,
        'gas':700000,
        'gasPrice':web3.toWei('50','gwei'),
        'nonce':web3.eth.getTransactionCount(patient_account.address)
    })
    signed_trn = web3.eth.account.sign_transaction(trxn, private_key=patient_account.privateKey)
    return(web3.eth.sendRawTransaction(signed_trn.rawTransaction))

def revokeAccess(doctor_address,patient_account):
    trxn=contract.functions.revokeAccess(doctor_address).buildTransaction({
        'chainId':chain_id,
        'gas':700000,
        'gasPrice':web3.toWei('50','gwei'),
        'nonce':web3.eth.getTransactionCount(patient_account.address)
    })
    signed_trn = web3.eth.account.sign_transaction(trxn, private_key=patient_account.privateKey)
    return(web3.eth.sendRawTransaction(signed_trn.rawTransaction))

def viewReport(patient_account):
    return(contract.functions.viewReport().call(transaction={'from':patient_account.address}))

##################################################################################################


def  addDoctor(doctor_account,aadhaar_id):
    trxn=contract.functions.addDoctor(aadhaar_id).buildTransaction({
        'chainId':chain_id,
        'gas':700000,
        'gasPrice':web3.toWei('50','gwei'),
        'nonce':web3.eth.getTransactionCount(doctor_account.address)
    })
    signed_trn = web3.eth.account.sign_transaction(trxn, private_key=doctor_account.privateKey)
    return(web3.eth.sendRawTransaction(signed_trn.rawTransaction))

def doctorInfo(doctor_account):
    return(contract.functions.doctorInfo().call(transaction={'from':doctor_account.address}))

def viewPatientReport(patient_address,doctor_account):
    return(contract.functions.viewPatientReport(patient_address).call(transaction={'from':doctor_account.address}))