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
            $('#name').text(data['first_name'] +' '+ data['middle_name']+' '+ data['last_name'])
            $('#email_id').text(data['email_id'])
            $('#email_id2').val(data['email_id'])
            $('#phone_no').text(data['phone_number'])
            $('#img').attr('src','/media/'+data["image"])
            $('#not_found').text('')
        },
        error: function(data){
          $('#result').hide()
          $('#not_found').text('No doctor found')
        }
    });
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





