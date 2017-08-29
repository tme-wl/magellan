/**
 * Created by tme on 2017/3/24.
 */

$(document).ready(function () {
  $('#checka').iCheck({
    checkboxClass: 'icheckbox_square-green',
    radioClass: 'iradio_square-green',
    increaseArea: '20%' // optional
  });
  $("#checkb").iCheck({
    radioClass: 'iradio_square-green',
    increaseArea: '20%' // optional

  })
});

      function choice_table(id_name) {
          $("#MyClass").removeClass("active");
          $("#MyStudent").removeClass("active");
          $("#MyTeacher").removeClass("active");
          $("#MyCourse").removeClass("active");
          $("#MyScore").removeClass("active");

          $("#" + id_name).addClass("active");
          $.ajax({
              type: "get",
              dataType: "json",
              url: '/sqlobj/gettable/?tablename=' + id_name,
              success: function (data) {
                  $("#table").html(data.table_html)
              }

          })
      }

      function getnowquestion(){
          var number = $("#number").val();
          var myurl = $("#myurl").val();
          var urllist = myurl.split('/');
          var newurl = '/' + urllist[1] + '/' + urllist[2]+'/' + (parseInt(number)) +'/';
          self.location=newurl;
          //getquestion(number);
      }
      function getquestion(number){

          $.ajax({
              type: "get",
              dataType: "json",
              url: '/sqlobj/getquestion/?question=' + number,
              success: function (data) {
                  $("#question").text(data.question);
                  $("#questionid").val(data.id);
                  $("#number").val(data.id);
                  $("#mysql").val('');
                  $("#questionclass").val(data.questionclass);
                  if (data.questionclass == 1){
                      $("#sqlyuju").css("display",'block');
                      $("#sqlchoice").css("display",'none');
                  }else if (data.questionclass == 2){
                      $("#sqlyuju").css("display",'none');
                      $("#sqlchoice").css("display",'block');
                  }else{
                      $("#sqlyuju").css("display",'none');
                      $("#sqlchoice").css("display",'none');
                  }
              }

          })

      }

      function getanswer(){
          var questionid = $("#questionid").val();
          $.ajax({
              type:'GET',
              dataType: "json",
              url:'/sqlobj/getanswer/',
              data:{"questionid":questionid},
              success:function(data) {
                  if (data.qclass == 1) {
                      $("#mysql").val(data.html);
                  }
                  else if(data.qclass == 2){
                      if (data.qchoice == 1)
                        $('#checka').iCheck('check');
                        $('#checkb').iCheck('uncheck');
                  }else if(data.qchoice == 2){
                        $('#checkb').iCheck('check');
                        $('#checka').iCheck('uncheck');
                  }
              }
          })
      }
      function uploadmysql(){
          var questionid = $("#questionid").val();
          var mysql = $("#mysql").val();
          var qclass = $("#questionclass").val();
          var chkRadio = $('input:radio[name="iCheck"]:checked').val();
          $.ajax({
              type:'POST',
              dataType: "json",
              url:'/sqlobj/uploadmysql/',
              data:{"mysql":mysql,"questionid":questionid,'qclass':qclass,'qchoice':chkRadio},
              success:function(data){
                  if(data.head == 'ok'){
                      $("#huadong").css("background-color","#dff0d8");
                      $("#huadong").css("border-color","#d6e9c6;");
                  }else{

                      $("#huadong").css("background-color","#edd");
                      $("#huadong").css("border-color","#eed;");
                  }

                  $("#alert").html(data.info);
                  $("#huadong").css("display","block");
                  setTimeout(function() { $("#huadong").css("display","none"); }, 2000);

              }

          })
      }
      function previous(){
          //var qid = parseInt($("#questionid").val())-1;
          var myurl = $("#myurl").val();
          var urllist = myurl.split('/');
          var newurl = '/' + urllist[1] + '/' + urllist[2]+'/' + (parseInt(urllist[3])-1) +'/';
          self.location=newurl;

      }

      function next(){
          //var qid = parseInt($("#questionid").val())+1;
          var myurl = $("#myurl").val();
          var urllist = myurl.split('/');
          var newurl = '/' + urllist[1] + '/' + urllist[2]+'/' + (parseInt(urllist[3])+1) +'/';
          self.location=newurl;

      }



  window.onload=function(){ scrop()};

      function scrop(){
        var the_hight_px = $(this).scrollTop();
        $("#huadong").css("top",the_hight_px+"px");

        $(window).scroll(function() {
            var the_hight_px = $(this).scrollTop();
                $("#huadong").css("top",the_hight_px+"px");
        });

    }