$(document).ready(function() {
  var max = 100;
  $(".blog-card-description").each(function() {
      var str = $(this).text();
      if ($.trim(str).length > max) {
          var subStr = str.substring(0, max);
          var hiddenStr = str.substring(max, $.trim(str).length);
          console.log(hiddenStr)
          $(this).empty().html(subStr);
          $(this).append('<a href="javascript:void(0);" class="link"> Read more…</a>');
          $(this).append('<span class="addText">'+hiddenStr+'</span>');
      }
  });
  $(".link").click(function() {
      $(this).siblings(".addText").contents().unwrap();
      $(this).remove();
  });
});

//***** */ pop up team member *******//

$(document).ready(function(){
  $(".trigger_popup_fricc").click(function(){
    console.log("hello1");
    document.querySelector(".hover_bkgr_fricc").style.display = 'block';
    document.querySelector("body").style.overflow = 'hidden';
  })

  $(".popupCloseButton").click(function(){
    console.log("hello2");
    document.querySelector(".hover_bkgr_fricc").style.display = 'none';
  document.querySelector("body").style.overflow = 'visible';
  })

})



const togglePassword = document.querySelector('#togglePassword');
  const password = document.querySelector('#id_password');

  togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

const togglePassword2 = document.querySelector('#togglePassword2');
  const password2 = document.querySelector('#id_password2');

  togglePassword2.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password2.getAttribute('type') === 'password' ? 'text' : 'password';
    password2.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});


const togglePassword3 = document.querySelector('#togglePassword3');
  const password3 = document.querySelector('#id_password3');

  togglePassword3.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password3.getAttribute('type') === 'password' ? 'text' : 'password';
    password3.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

const togglePassword4 = document.querySelector('#togglePassword4');
  const password4 = document.querySelector('#id_password4');

  togglePassword4.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password4.getAttribute('type') === 'password' ? 'text' : 'password';
    password4.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

const togglePassword5 = document.querySelector('#togglePassword5');
  const password5 = document.querySelector('#id_password5');

  togglePassword5.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password5.getAttribute('type') === 'password' ? 'text' : 'password';
    password5.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});

const togglePassword6 = document.querySelector('#togglePassword6');
  const password6 = document.querySelector('#id_password6');

  togglePassword6.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password6.getAttribute('type') === 'password' ? 'text' : 'password';
    password6.setAttribute('type', type);
    // toggle the eye slash icon
    this.classList.toggle('fa-eye-slash');
});




const inputField = document.getElementById("company_email");

$(document).ready(function(){
  $("#company_email").change(function () {
    var email = $(this).val();

    $.ajax({
      url: '/validate_username/',
      data: {
        'email': email
      },
      dataType: 'json',
      success: function (data) {
        if (data.is_taken) {
          document.getElementById("msg13").innerHTML = "Email Already Exists!!!";
          inputField.value = " ";
        }
      }
    });

  });
});


const inputField2 = document.getElementById("another_email");

$(document).ready(function(){
  $("#another_email").change(function () {
    var email = $(this).val();

    $.ajax({
      url: '/validate_username/',
      data: {
        'email': email
      },
      dataType: 'json',
      success: function (data) {
        if (data.is_taken) {
          document.getElementById("msg5").innerHTML = "Email Already Exists!!!";
          inputField2.value = " ";
        }
      }
    });

  });
});


const inputField3 = document.getElementById("usr_email");

$(document).ready(function(){
  $("#usr_email").change(function () {
    var email = $(this).val();

    $.ajax({
      url: '/validate_username/',
      data: {
        'email': email
      },
      dataType: 'json',
      success: function (data) {
        if (data.is_taken) {
          document.getElementById("msg").innerHTML = "Email Already Exists!!!";
          inputField3.value = " ";
        }
      }
    });

  });
});


// const check_username = document.getElementById("username");

// $(document).ready(function(){
//   $("#username").change(function () {
//     var username = $(this).val();
//     console.log(username)
//     $.ajax({
//       url: '{% url "validate_user" %}',
//       data: {
//         'username': username
//       },
//       dataType: 'json',
      
//       success: function (data) {
//         if (data.is_taken) {
//           document.getElementById("msg").innerHTML = "Username Already Exists!!!";
//           check_username.value = " ";
//           console.log(username)
//         }
//       }
//     });

//   });
// });


