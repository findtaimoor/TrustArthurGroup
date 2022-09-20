$(document).ready(function () {
  $(".Readmore1").click(function () {
    $(".popupk1").show();
  });
  $("#close1").click(function () {
    $(".popupk1").hide();
  });
  $(".Readmore2").click(function () {
    $(".popupk2").show();
  });
  $("#close2").click(function () {
    $(".popupk2").hide();
  });
  $(".Readmore3").click(function () {
    $(".popupk3").show().focus();
  });
  $("#close3").click(function () {
    $(".popupk3").hide();
  });
  $(".Readmore4").click(function () {
    $(".popupk4").show().focus();
  });
  $("#close4").click(function () {
    $(".popupk4").hide();
  });

  var child = 1;
  var length = $("section .register-usr").length - 1;
  var formData = [];
  var formData2 = new FormData();

  $("section .register-usr").not("section .register-usr:nth-of-type(1)").hide();
  $("section .register-usr")
    .not("section .register-usr:nth-of-type(1)")
    .css("transform", "translateX(100px)");

  $(".individual-btn").click(function () {
    var typeofuser = 'individual';
    // formData.push({
    //   'typeofuser':typeofuser,
    // });
    formData2.append('typeofuser',typeofuser)
    nextFunction();
  });

  $(".business-btn").click(function () {
    child = 12;
    var typeofuser = 'business';
    // formData.push({
    //   'typeofuser':typeofuser,
    // });
    formData2.append('typeofuser',typeofuser)
    nextFunction();
  });

  

  $(".btn-register").click(function () {
    var fullname = document.getElementById("usr_name").value;
    var individual_email = document.getElementById("usr_email").value;
    var pass = document.getElementById("id_password").value;
    var re_pass = document.getElementById("id_password2").value;
    var check = document.querySelector("#check_term:checked") !== null;
    if (fullname == null || fullname == "") {
      document.getElementById("msg").innerHTML = "Please enter fullname";
    } else if (individual_email == null || individual_email == "" || !validateEmail(individual_email)) {
      document.getElementById("msg").innerHTML = "Please enter Valid email address";
    } else if (pass == null || pass == "") {
      document.getElementById("msg").innerHTML = "Please enter valid password";
    } else if (re_pass == null || re_pass == "") {
      document.getElementById("msg").innerHTML = "Please enter valid password";
    } else if (pass != re_pass ) {
      document.getElementById("msg").innerHTML = "Your passwords are not match";
    } else if (check == false) {
      document.getElementById("msg").innerHTML = "Please Check Term and condition";
    } else {
      formData.push({
        'Form':1,
        'fullname':fullname,
        'individual_email':individual_email,
        'password':pass,
        'check':check
      })

      formData2.append('fullname', fullname)
      formData2.append('individual_email', individual_email)
      formData2.append('password', pass)

      nextFunction();
    }
  });

  $(".btn-register-2").click(function () {
    var phone = document.getElementById("usr_phone").value;
    var house_number = document.getElementById("usr_house_number").value;
    var street_name = document.getElementById("usr_street_name").value;
    var city = document.getElementById("usr_city").value;
    var state = document.getElementById("usr_state").value;
    var country = document.getElementById("usr_country").value;
    if (
      phone == null ||
      phone == "" ||
      phone.length < 11 ||
      phone.length > 11
    ) {
      document.getElementById("msg2").innerHTML = "Please Enter valid Phone Number";
    } else if (house_number == null || house_number == "") {
      document.getElementById("msg2").innerHTML = "Please Enter Valid House Number";
    } else if (street_name == null || street_name == "") {
      document.getElementById("msg2").innerHTML = "Please Enter valid Street Name";
    } else if (city == null || city == "") {
      document.getElementById("msg2").innerHTML = "Please Enter valid City Name";
    } else if (state == null || state == "") {
      document.getElementById("msg2").innerHTML = "Please Enter valid State Name";
    } else if (country == null || country == "") {
      document.getElementById("msg2").innerHTML = "Please Enter valid Country Name";
    } else {
      formData.push({
        'Form':2,
        'phone':phone,
        'house_number':house_number,
        'street_name':street_name,
        'city':city,
        'state':state,
        'country':country
      })

      formData2.append('phone', phone)
      formData2.append('house_number', house_number)
      formData2.append('street_name', street_name)
      formData2.append('city', city)
      formData2.append('state', state)
      formData2.append('country', country)
      
      nextFunction();
    }
  });

  $(".btn-register-3").click(function () {
    var birthdate = document.getElementById("usr_birthdate").value;
    var gender = document.getElementById("usr_gender").value;
    var occupation = document.getElementById("usr_occupation").value;
    var NIN = document.getElementById("NIN").value;
    var BVN = document.getElementById("BVN").value;
    if (birthdate == null || birthdate == "") {
      document.getElementById("msg3").innerHTML = "Please Enter valid Birth Date";
    } else if (gender == null || gender == "") {
      document.getElementById("msg3").innerHTML = "Please Select valid Gender";
    } else if (occupation == null || occupation == "") {
      document.getElementById("msg3").innerHTML = "Please Select valid Occupation";
    } else if (NIN == null || NIN == "") {
      document.getElementById("msg3").innerHTML = "Please Enter valid NIN Number";
    } else if (BVN == null || BVN == "") {
      document.getElementById("msg3").innerHTML = "Please Enter valid BVN Number";
    } else {
      formData.push({
        'Form':3,
        'birthdate':birthdate,
        'gender':gender,
        'occupation':occupation,
        'NIN':NIN,
        'BVN':BVN
      })
      
      formData2.append('birthdate', birthdate)
      formData2.append('gender', gender)
      formData2.append('occupation', occupation)
      formData2.append('NIN', NIN)
      formData2.append('BVN', BVN)

      nextFunction();
    }
  });

  $(".btn-register-4").click(function () {
    var joint_account = document.getElementById("joint_account").value;
    if (joint_account == "Yes") {
      formData.push({
        'Form':4,
        'joint_account':joint_account
      })
      
      formData2.append('joint_account', joint_account)
      nextFunction();

    } else if(joint_account == "No") {
      child = 9;
      formData.push({
        'Form':4,
        'joint_account':joint_account
      })
      
      formData2.append('joint_account', joint_account)
      nextFunction();
    }else{
      document.getElementById("msg4").innerHTML = "Please Select valid Join Account";
    }
  });

  $(".btn-register-5").click(function () {
    var another_name = document.getElementById("another_name").value;
    var another_email = document.getElementById("another_email").value;
    var another_pass = document.getElementById("id_password3").value;
    var another_re_pass = document.getElementById("id_password4").value;
    var check = document.querySelector("#checkbox_5:checked") !== null;
    if (another_name == null || another_name == "") {
      document.getElementById("msg5").innerHTML = "Please enter fullname";
    } else if (another_email == null || another_email == "" || !validateEmail(another_email)) {
      document.getElementById("msg5").innerHTML = "Please enter Valid email address";
    } else if (another_pass == null || another_pass == "") {
      document.getElementById("msg5").innerHTML = "Please enter valid password";
    } else if (another_re_pass == null || another_re_pass == "") {
      document.getElementById("msg5").innerHTML = "Please enter valid password";
    } else if (another_pass != another_re_pass ) {
      document.getElementById("msg5").innerHTML = "Your passwords are not match";
    } else if (check == false) {
      document.getElementById("msg5").innerHTML = "Please Check Term and condition";
    } else {
      formData.push({
        'Form':5,
        'another_name':another_name,
        'another_email':another_email,
        'another_pass':another_pass,
        'check':check
      })
      
      formData2.append('another_name', another_name)
      formData2.append('another_email', another_email)
      formData2.append('another_pass', another_pass)

      nextFunction();
    }
  });

  $(".btn-register-6").click(function () {
    var another_phone = document.getElementById("another_phone").value;
    var another_house_number = document.getElementById("another_house_number").value;
    var another_street_name = document.getElementById("another_street_name").value;
    var another_city = document.getElementById("another_city").value;
    var another_state = document.getElementById("another_state").value;
    var another_country = document.getElementById("another_country").value;
    if (
      another_phone == null ||
      another_phone == "" ||
      another_phone.length < 11 ||
      another_phone.length > 11
    ) {
      alert("please Enter Phone");
    } else if (another_house_number == null || another_house_number == "") {
      document.getElementById("msg6").innerHTML = "Please Enter Valid House Number";
    } else if (another_street_name == null || another_street_name == "") {
      document.getElementById("msg6").innerHTML = "Please Enter valid Street Name";
    } else if (another_city == null || another_city == "") {
      document.getElementById("msg6").innerHTML = "Please Enter valid City Name";
    } else if (another_state == null || another_state == "") {
      document.getElementById("msg6").innerHTML = "Please Enter valid State Name";
    } else if (another_country == null || another_country == "") {
      document.getElementById("msg6").innerHTML = "Please Enter valid Country Name";
    } else {
      formData.push({
        'Form':6,
        'another_phone':another_phone,
        'another_house_number':another_house_number,
        'another_street_name':another_street_name,
        'another_city':another_city,
        'another_state':another_state,
        'another_country':another_country,
      })
    
      nextFunction();

      formData2.append('another_phone', another_phone)
      formData2.append('another_house_number', another_house_number)
      formData2.append('another_street_name', another_street_name)
      formData2.append('another_city', another_city)
      formData2.append('another_state', another_state)
      formData2.append('another_country', another_country)

    }
  });

  $(".btn-register-7").click(function () {
    var another_birthdate = document.getElementById("another_birthdate").value;
    var another_gender = document.getElementById("another_gender").value;
    var another_occupation = document.getElementById("another_occupation").value;
    if (another_birthdate == null || another_birthdate == "") {
      document.getElementById("msg7").innerHTML = "Please Enter valid Birth Date";
    } else if (another_gender == null || another_gender == "") {
      document.getElementById("msg7").innerHTML = "Please Select valid Gender";
    } else if (another_occupation == null || another_occupation == "") {
      document.getElementById("msg7").innerHTML = "Please Select valid Occupation";
    } else {
      formData.push({
        'Form':7,
        'another_birthdate':another_birthdate,
        'another_gender':another_gender,
        'another_occupation':another_occupation
      })
      
      formData2.append('another_birthdate', another_birthdate)
      formData2.append('another_gender', another_gender)
      formData2.append('another_occupation', another_occupation)

      nextFunction();
    }
  });

  $(".btn-register-8").click(function () {
    var another_signature = $('#another_signature')[0].files[0]
    var another_photo = $('#another_photo')[0].files[0]
    var check1 = document.querySelector("#check_term8:checked") !== null;
    var check2 = document.querySelector("#check_sign:checked") !== null;
    var check3 = document.querySelector("#check_telefax:checked") !== null;
    if (another_signature == null || another_signature == "") {
      document.getElementById("msg8").innerHTML = "Please Upload Signature";
    } else if (another_photo == null || another_photo == "") {
      document.getElementById("msg8").innerHTML = "Please Upload Photo";
    } else if (check1 == false) {
      document.getElementById("msg8").innerHTML = "Please Check Term and condition";
    } else if (check2 == false) {
      document.getElementById("msg8").innerHTML = "Please Check Term and condition";
    // } else if (check3 == false) {
    //   alert("please Check Term and condition");
    } else {
      formData.push({
        'Form':8,
        'another_signature':another_signature,
        'another_photo':another_photo,
        'check1':check1,
        'check2':check2,
        'check3':check3
      })
      formData2.append('another_signature', another_signature)
      formData2.append('another_photo', another_photo)
      nextFunction();
    }
  });

  $(".btn-register-9").click(function () {
    var kin_name = document.getElementById("kin_name").value;
    var kin_relationship = document.getElementById("kin_occupation").value;
    if (kin_name == null || kin_name == "") {
      document.getElementById("msg9").innerHTML = "Please enter fullname";
    } else if (kin_relationship == null || kin_relationship == "") {
      document.getElementById("msg9").innerHTML = "Please Select valid Relationship";
    } else {
      formData.push({
        'Form':9,
        'kin_name':kin_name,
        'kin_relationship':kin_relationship
      })
      
      formData2.append('kin_name', kin_name)
      formData2.append('kin_relationship', kin_relationship)

      nextFunction();
    }
  });

  $(".btn-register-10").click(function () {
    var kin_phone = document.getElementById("kin_phone").value;
    var kin_house_number = document.getElementById("kin_house_number").value;
    var kin_street_name = document.getElementById("kin_street_name").value;
    var kin_city = document.getElementById("kin_city").value;
    var kin_state = document.getElementById("kin_state").value;
    var kin_country = document.getElementById("kin_country").value;
    if (
      kin_phone == null ||
      kin_phone == "" ||
      kin_phone.length < 11 ||
      kin_phone.length > 11
    ) {
      document.getElementById("msg10").innerHTML = "Please Enter valid Phone Number";
    } else if (kin_house_number == null || kin_house_number == "") {
      document.getElementById("msg10").innerHTML = "Please Enter Valid House Number";
    } else if (kin_street_name == null || kin_street_name == "") {
      document.getElementById("msg10").innerHTML = "Please Enter valid Street Name";
    } else if (kin_city == null || kin_city == "") {
      document.getElementById("msg10").innerHTML = "Please Enter valid City Name";
    } else if (kin_state == null || kin_state == "") {
      document.getElementById("msg10").innerHTML = "Please Enter valid State Name";
    } else if (kin_country == null || kin_country == "") {
      document.getElementById("msg10").innerHTML = "Please Enter valid Country Name";
    } else {
      formData.push({
        'Form':10,
        'kin_phone':kin_phone,
        'kin_house_number':kin_house_number,
        'kin_street_name':kin_street_name,
        'kin_city':kin_city,
        'kin_state':kin_state,
        'kin_country':kin_country
      })

      formData2.append('kin_phone', kin_phone)
      formData2.append('kin_house_number', kin_house_number)
      formData2.append('kin_street_name', kin_street_name)
      formData2.append('kin_city', kin_city)
      formData2.append('kin_state', kin_state)
      formData2.append('kin_country', kin_country)

      nextFunction();
    }
  });

  $(".btn-register-11").click(function () {
    var individual_signature = $('#individual_signature')[0].files[0]
    var individual_photo = $('#individual_photo')[0].files[0]
    var check1 = document.querySelector("#check_term11:checked") !== null;
    var check2 = document.querySelector("#check_sign2:checked") !== null;
    var check3 = document.querySelector("#check_telefax2:checked") !== null;
    if (individual_signature == null || individual_signature == "") {
      document.getElementById("msg11").innerHTML = "Please Upload Signature";
    } else if (individual_photo == null || individual_photo == "") {
      document.getElementById("msg11").innerHTML = "Please Upload Photo";
    } else if (check1 == false) {
      document.getElementById("msg11").innerHTML = "Please Check Term and condition";
    } else if (check2 == false) {
      document.getElementById("msg11").innerHTML = "Please Check Term and condition";
    } else if (check3 == false) {
      document.getElementById("msg11").innerHTML = "Please Check Term and condition";
    } else {
      formData.push({
        'Form':11,
        'individual_signature':individual_signature,
        'individual_photo':individual_photo,
        'check1':check1,
        'check2':check2,
        'check3':check3
      })
      
      formData2.append('individual_signature', individual_signature)
      formData2.append('individual_photo',  individual_photo)
      formData2.append('csrfmiddlewaretoken', $("input[name=csrfmiddlewaretoken]").val())


      $.ajax({
        method: 'POST',
        url: '/signup',
        data: formData2,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
    })
        .done(function (response) {
            window.location.href = '/signin';

        })
        .fail(function (response) {
            console.log(response)
        })
    }
    
  });


  $(".btn-register-12").click(function () {
    var company_name = document.getElementById("company_name").value;
    var company_number = document.getElementById("company_number").value;
    var tax_id = document.getElementById("tax_id").value;
    var company_industry = document.getElementById("company_Industry").value;
    var check = document.querySelector("#check_term12:checked") !== null;
    if (company_name == null || company_name == "") {
      document.getElementById("msg12").innerHTML = "Please enter fullname";
    } else if (company_number == null || company_number == "") {
      document.getElementById("msg12").innerHTML = "Please enter Valid Company Number";
    } else if (tax_id == null || tax_id == "") {
      document.getElementById("msg12").innerHTML = "Please enter Valid Tax ID";
    } else if (company_industry == null || company_industry == "") {
      document.getElementById("msg12").innerHTML = "Please Select Valid Company Industry";
    } else if (check == false) {
      document.getElementById("msg12").innerHTML = "Please Check Term and condition";
    } else {
      formData.push({
        'Form':12,
        'company_name':company_name,
        'company_number':company_number,
        'tax_id':tax_id,
        'company_industry':company_industry,
        'check':check
      })
      formData2.append('company_name', company_name)
      formData2.append('company_number', company_number)
      formData2.append('tax_id', tax_id)
      formData2.append('company_industry', company_industry)
      nextFunction();
    }
  });

  $(".btn-register-13").click(function () {
    var company_date = document.getElementById("company_date").value;
    var company_email = document.getElementById("company_email").value;
    var pass = document.getElementById("id_password5").value;
    var re_pass = document.getElementById("id_password6").value;
    var NIN = document.getElementById("company_NIN").value;
    var BVN = document.getElementById("company_BVN").value;
    // var check = document.querySelector("#check_term13:checked") !== null;
    if (company_date == null || company_date == "") {
      document.getElementById("msg13").innerHTML = "Please Enter valid Company Date";
    } else if (company_email == null || company_email == "") {
      document.getElementById("msg13").innerHTML = "Please Enter valid Email";
    } else if (NIN == null || NIN == "") {
      document.getElementById("msg13").innerHTML = "Please Enter valid NIN Number";
    } else if (BVN == null || BVN == "") {
      document.getElementById("msg13").innerHTML = "Please Enter valid BVN Number";
    } else if (pass == null || pass == "") {
      document.getElementById("msg13").innerHTML = "Please enter valid password";
    } else if (re_pass == null || re_pass == "") {
      document.getElementById("msg13").innerHTML = "Please enter valid password";
    } else if (pass != re_pass ) {
      document.getElementById("msg13").innerHTML = "Your passwords are not match";
    // } else if (check == false) {
    //   alert("please Check Term and condition");
    } else {
      formData.push({
        'Form':13,
        'company_date':company_date,
        'company_email':company_email,
        'pass':pass,
        'NIN':NIN,
        'BVN':BVN,
        // 'check':check
      })
      formData2.append('company_date',company_date)
      formData2.append('company_email',company_email)
      formData2.append('pass',pass)
      formData2.append('NIN',NIN)
      formData2.append('BVN',BVN)
      nextFunction();
    }
  });

  $(".btn-register-14").click(function () {
    var phone = document.getElementById("company_phone").value;
    var house_number = document.getElementById("company_house_number").value;
    var street_name = document.getElementById("company_street_name").value;
    var city = document.getElementById("company_city").value;
    var state = document.getElementById("company_state").value;
    var country = document.getElementById("company_country").value;
    if (
      phone == null ||
      phone == "" ||
      phone.length < 11 ||
      phone.length > 11
    ) {
      document.getElementById("msg14").innerHTML = "Please Enter valid Phone Number";
    } else if (house_number == null || house_number == "") {
      document.getElementById("msg14").innerHTML = "Please Enter Valid House Number";
    } else if (street_name == null || street_name == "") {
      document.getElementById("msg14").innerHTML = "Please Enter valid Street Name";
    } else if (city == null || city == "") {
      document.getElementById("msg14").innerHTML = "Please Enter valid City Name";
    } else if (state == null || state == "") {
      document.getElementById("msg14").innerHTML = "Please Enter valid State Name";
    } else if (country == null || country == "") {
      document.getElementById("msg14").innerHTML = "Please Enter valid Country Name";
    } else {
      formData.push({
        'Form':14,
        'phone':phone,
        'house_number':house_number,
        'street_name':street_name,
        'city':city,
        'state':state,
        'country':country
      })
      formData2.append('phone',phone)
      formData2.append('house_number',house_number)
      formData2.append('street_name',street_name)
      formData2.append('city',city)
      formData2.append('state',state)
      formData2.append('country',country)
      nextFunction();
    }
  });

  $(".btn-register-15").click(function () {
    var name1 = document.getElementById("exetive_name1").value;
    var name2 = document.getElementById("exetive_name2").value;
    var name3 = document.getElementById("exetive_name3").value;
    var name4 = document.getElementById("exetive_name4").value;
    if (name1 == null || name1 == "") {
      document.getElementById("msg15").innerHTML = "Please enter name 1";
    } else if (name2 == null || name2 == "") {
      document.getElementById("msg15").innerHTML = "Please enter name 2";
    } else if (name3 == null || name3 == "") {
      document.getElementById("msg15").innerHTML = "Please enter name 3";
    } else if (name4 == null || name4 == "") {
      document.getElementById("msg15").innerHTML = "Please enter name 4";
    } else {
      formData.push({
        'Form':15,
        'name1':name1,
        'name2':name2,
        'name3':name3,
        'name4':name4
      })
      formData2.append('name1',name1)
      formData2.append('name2',name2)
      formData2.append('name3',name3)
      formData2.append('name4',name4)
      nextFunction();
    }
  });

  $(".btn-register-16").click(function () {
    // var signature = document.getElementById("company_signature").value;
    // var photo = document.getElementById("company_photo").value;
    var signature = $('#company_signature')[0].files[0]
    var photo = $('#company_photo')[0].files[0]
    var check1 = document.querySelector("#check_term16:checked") !== null;
    var check2 = document.querySelector("#check_sign16:checked") !== null;
    var check3 = document.querySelector("#check_telefax16:checked") !== null;
    if (signature == null || signature == "") {
      document.getElementById("msg16").innerHTML = "Please Upload Signature";
    } else if (photo == null || photo == "") {
      document.getElementById("msg16").innerHTML = "Please Upload Photo";
    } else if (check1 == false) {
      document.getElementById("msg16").innerHTML = "Please Check Term and condition";
    } else if (check2 == false) {
      document.getElementById("msg16").innerHTML = "Please Check Term and condition";
    } else if (check3 == false) {
      document.getElementById("msg16").innerHTML = "Please Check Term and condition";
    } else {
      formData.push({
        'Form':16,
        'signature':signature,
        'photo':photo,
        'check1':check1,
        'check2':check2,
        'check3':check3
      })
      
      
      formData2.append('signature',  signature)
      formData2.append('photo',  photo)
      formData2.append('csrfmiddlewaretoken', $("input[name=csrfmiddlewaretoken]").val())
      
      formData.push({'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()})

    $.ajax({
        method: 'POST',
        url: '/signup',
        data: formData2,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
    })
        .done(function (response) {
            window.location.href = '/signin';

        })
        .fail(function (response) {
            console.log(response)
        })
    }
    
  });

  const validateEmail = (email) => {
    return String(email)
      .toLowerCase()
      .match(
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      );
  };

  function nextFunction() {
    if (child <= length) {
      child++;
    }
    var currentSection = $("section .register-usr:nth-of-type(" + child + ")");
    currentSection.fadeIn();
    currentSection.css("transform", "translateX(0)");
    currentSection
      .nextAll("section .register-usr")
      .css("transform", "translateX(100px)");
    $("section .register-usr").not(currentSection).hide();
  }

  $(".prev-sec").click(function () {
    formData.pop();
    console.log(formData);
    if (child == 13) {
      child = 1;
    } else if (child == 11) {
      child = 6;
    }
    if (child > 1) {
      child--;
    }
    
    // let xhr = new XMLHttpRequest();
    // let url = "/signup";
    // xhr.open("POST", url, true);
    // xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded;charset=UTF-8");
    // xhr.send(formData);
    // $.ajax({
    //   url:"./signup2",
    //   type:"POST", 
    //   contentType:"application/json",
    //   data: JSON.stringify(formData)
    // });
    
    var currentSection = $("section .register-usr:nth-of-type(" + child + ")");
    currentSection.fadeIn();
    currentSection.css("transform", "translateX(0)");
    currentSection
      .nextAll("section .register-usr")
      .css("transform", "translateX(100px)");
    $("section .register-usr").not(currentSection).hide();
  });
  
});
