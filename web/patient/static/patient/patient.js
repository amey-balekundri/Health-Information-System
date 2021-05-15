$(document).ready(function(){
  
  $('#result').hide()
  $('#reportimg').hide()
  $('#reportpdf').hide()

  $("#search_here").click(function(){
    var doctor=$("#search_value").val();
    $.ajax({
        type:"GET",
        url: "access_doctor/search_doctor/",
        data: {'doctor':doctor},
        dataType:'json',
        success: function(data){
            $('#result').show()
            $('#name').text('Name:' + data['first_name'] +' '+ data['middle_name']+' '+ data['last_name'])
            $('#email_id').text('Email Id:' + data['email_id'])
            $('#email_id2').val(data['email_id'])
            $('#specialization').text('Specialization:'+data['specialization'])
            $('#city').text('City:'+data['city'])
            $('#phone_no').text('Phone No:'+data['phone_number'])
            $('#img').attr('src','/media/'+data["image"])
            $('#not_found').text('')
        },
        error: function(data){
          $('#result').hide()
          $('#not_found').text('No doctor found')
        }
    });
})

$('#filter').click(()=>{
  var city=$('#id_city').val();
  var specialization=$('#id_specialization').val();
  const csrf=$('[name=csrfmiddlewaretoken]').val();
  $.ajax({
    type:"GET",
    url:"access_doctor/search_doctor2/",
    data:{'city':city,'specialization':specialization},
    dataType:'json',
    success:(data)=>{
      let result=data.map((doc,index)=>{
        let data=`
        <div class="col-sm-12 col-md-6 col-lg-3">
          <form method="POST" action="/patient/access_doctor/grant_access/" enctype="multipart/form-data">
          <input type="hidden" name="csrfmiddlewaretoken" value="${csrf}">
            <div class="card mx-2 my-2 p-2">
              <img src="/media/${doc.image}" class="card-img-top mx-auto" alt="..." id="img"></img>
              <div class="card-body mx-auto text-center">
                <p class="card-title">Name:${doc.first_name} ${doc.middle_name} ${doc.last_name}</p>
                <p class="card-text">Email Id:${doc.email_id}</p>
                <input type="hidden" name="email_id" value=${doc.email_id}>
                <p class="card-text">Specialization:${doc.specialization}</p>
                <p class="card-text">City:${doc.city}</p>
                <p class="card-text">Phone No:${doc.phone_number}</p>
                <input type="submit" class="btn1" value="Grant Access">
              </div>
            </div>
          </form>
        </div>`
        return data
      })
      if(data.length!=0) document.getElementById('filter_result').innerHTML=result.join('')
      else document.getElementById('filter_result').innerHTML="<h1>No Results Found</h1>"
    },
    error:()=>{
      document.getElementById('filter_result').innerHTML="<h1>No Results Found</h1>"
    }
  })
})

$("#search_value").keyup(function(){
  $('#result').hide()
})


$("#report_file").change(function(event){
  var ext=$("#report_file").val().split('.').pop();
  var allowedext=['pdf','txt','jpg','jpeg','png']

  if(allowedext.includes(ext)){
    if(['jpg','jpeg','png'].includes(ext)){
      $('#reportimg').show()
      $('#reportpdf').hide()
      var reportimg=document.getElementById('reportimg');
      reportimg.src=URL.createObjectURL(event.target.files[0]);
      reportimg.onload=function () { 
        URL.revokeObjectURL(reportimg.src)
       }
    }
    else{
      $('#reportimg').hide()
      $('#reportpdf').show()
      var reportpdf=document.getElementById('reportpdf');
      reportpdf.src=URL.createObjectURL(event.target.files[0])+'#toolbar=0';
      reportpdf.onload=function () { 
        URL.revokeObjectURL(reportpdf.src)
       }
    }
  }
  else{
    alert('Invalid file type')
  }
})







});





