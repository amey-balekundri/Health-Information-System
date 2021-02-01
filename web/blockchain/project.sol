pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

contract health{
    
    mapping(address =>Patient) private patient;
    mapping(address =>Doctor) private doctor;
    mapping(address=>Report[]) private report;
    mapping(address=>mapping(address=>uint)) private patientToDoctor;
    mapping(address=>mapping(address=>uint)) private doctorToPatient;
    
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    

    struct Patient{
        address id;
        uint aadhaar_id;
        string[] reports;
        address[] doctor_list;
    }
    
    struct Doctor{
        address id;
        uint aadhaar_id;
        address[] patient_list;
    }
    
    struct Report{
        uint timestamp;
        string file;
        string file_hash;
    }
    
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    

    modifier isPatient(address id) {
        Patient memory p = patient[id];
        require(p.id > address(0x0));
        _;
    }
    
    function addPatient(uint aadhaar_id) public{
        //patient[msg.sender]=Patient({doctor_list:new address[](0)});
        Patient memory p=patient[msg.sender];
        require(!(p.id > address(0x0)));
        patient[msg.sender].id=msg.sender;
        patient[msg.sender].aadhaar_id=aadhaar_id;
        patient[msg.sender].reports=new string[](0);
        patient[msg.sender].doctor_list=new address[](0);
    }
    
    function patientInfo() public view isPatient(msg.sender) returns(uint,string[] memory,address[] memory){
        Patient memory p=patient[msg.sender];
        return(p.aadhaar_id,p.reports,p.doctor_list);
    }
    
     function addReport(string memory file,string memory file_hash) public isPatient(msg.sender){
        Patient storage p=patient[msg.sender];
        Report memory r;
        r.file_hash=file_hash;
        r.file=file;
        r.timestamp=now;
        report[msg.sender].push(r);
        p.reports.push(file_hash);
    }
    
    function grantAccessToDoctor(address doc_address) public isPatient(msg.sender) isDoctor(doc_address){
        require(!(patientToDoctor[msg.sender][doc_address]>0) && !(doctorToPatient[doc_address][msg.sender]>0));
        Patient storage p=patient[msg.sender];
        Doctor storage d=doctor[doc_address];
       
        uint pl=p.doctor_list.length;
        p.doctor_list.push(doc_address);
        patientToDoctor[msg.sender][doc_address]=pl+1;
       
        uint dl=d.patient_list.length;
        d.patient_list.push(msg.sender);
        doctorToPatient[doc_address][msg.sender]=dl+1;
    }
    
    function revokeAccess(address doc_address) public isPatient(msg.sender) isDoctor(doc_address){
        uint dindex=patientToDoctor[msg.sender][doc_address];
        uint pindex=doctorToPatient[doc_address][msg.sender];
        Patient storage p=patient[msg.sender];
        Doctor storage d=doctor[doc_address];
        p.doctor_list[dindex-1]=p.doctor_list[p.doctor_list.length-1];
        d.patient_list[pindex-1]=d.patient_list[d.patient_list.length-1];
        patientToDoctor[msg.sender][p.doctor_list[p.doctor_list.length-1]]=dindex;
        doctorToPatient[doc_address][d.patient_list[d.patient_list.length-1]]=pindex;
        p.doctor_list.pop();
        d.patient_list.pop();
        patientToDoctor[msg.sender][doc_address]=0;
        doctorToPatient[doc_address][msg.sender]=0;
    }
    
    function viewReport() public view isPatient(msg.sender) returns(Report[] memory){
     return(report[msg.sender]);
    }
    
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    modifier isDoctor(address id) {
        Doctor memory d = doctor[id];
        require(d.id > address(0x0));
        _;
    }
    function addDoctor(uint aadhaar_id) public{
        Doctor memory d=doctor[msg.sender];
        require(!(d.id > address(0x0)));
        doctor[msg.sender].id=msg.sender;
        doctor[msg.sender].aadhaar_id=aadhaar_id;
        doctor[msg.sender].patient_list=new address[](0);
    }
    
    function doctorInfo() public view isDoctor(msg.sender) returns(uint,address[] memory){
        Doctor memory d=doctor[msg.sender];
        return(d.aadhaar_id,d.patient_list);
    }
    
    function viewPatientReport(address pat_address) public view isDoctor(msg.sender) isPatient(pat_address) returns(Report[] memory){
        require(patientToDoctor[pat_address][msg.sender]!=0 && doctorToPatient[msg.sender][pat_address]!=0);
        return(report[pat_address]);
    }
    
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////   
    
    
    
    
    
}

