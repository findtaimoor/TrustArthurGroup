let check = false;

function get_quat(quantity, put_quantitiy, available_pro , sum_q )
{
  var starting_date = null;
  var frequency = null;

  var get_start_date = document.getElementById("start_date")
  if(get_start_date!= null){
    document.getElementById("starting_date_O").value = get_start_date.value;
  }
  
  var get_frequency = document.getElementById("frequency")
  if(get_frequency!= null){
    var value = get_frequency.options[get_frequency.selectedIndex].text;
    document.getElementById("frequency_O").value = value;
  }

  if(quantity != null){
  
    var get_quantity = document.getElementById(quantity)
   
    if(get_quantity!=null){
      get_quantity =get_quantity.value;
      document.getElementById(put_quantitiy).value = get_quantity;
    }else{
      get_quantity = 0
      document.getElementById(put_quantitiy).value = get_quantity;

    }
    
    

    var get_availablePro = document.getElementById(available_pro)
    if(get_availablePro!= null){
      get_availablePro = get_availablePro.innerText.replace ( /[^\d.]/g, '' );
      document.getElementById('avail_pro2').value = get_availablePro
    }else{
      get_availablePro = 0;
      document.getElementById('avail_pro2').value = get_availablePro

    }
    
  
    console.log('farhan Ali'+document.getElementById('avail_pro2').value)
  
    sum_product = get_availablePro - get_quantity ;
    document.getElementById(sum_q).value = sum_product;
    check = true;
  }  
}

function for_ofline_wadiah(){
  var starting_date = null;
  var frequency = null;

  var get_start_date = document.getElementById("start_date")
  if(get_start_date!= null){
    document.getElementById("starting_date_OF").value = get_start_date.value;
  }
  
  var get_frequency = document.getElementById("frequency")
  if(get_frequency!= null){
    var value = get_frequency.options[get_frequency.selectedIndex].text;
    document.getElementById("frequency_OF").value = value;
  }
}


function validate_value()
{
  var input_val = null;
  // var minimum_val = parseInt(document.getElementById('minimum_lable').innerText.replace ( /[^\d.]/g, '' ))
  var minimum_val = document.getElementById('minimum_lable');
  if(minimum_val!=null){
    minimum_val = parseInt(minimum_val).innerText
    input_val = document.getElementById('_quantity').value;
  }
  
  var _date = null;
    var start_date = document.getElementById("start_date")
  if(start_date!=null){
    _date = start_date.value;
  }

  maximum_val =document.getElementById('a-pro')
  if(maximum_val!=null){
    maximum_val = parseInt(maximum_val).innerText
    input_val = document.getElementById('_quantity').value;
  }
  document.getElementById('quan').value = input_val
  console.log(document.getElementById('quan').value)
  if(input_val < minimum_val || input_val > maximum_val)
  {
    
    document.getElementById("quantity_error").innerText=('Your quantity must be between Minimum or Available Product!')
    document.getElementById('checkout_btn').setAttribute('data-target', '#')
  }else if(_date == ""){
    document.getElementById("quantity_error").innerText=('Select Starting Date!')
    document.getElementById('checkout_btn').setAttribute('data-target', '#')
  }
  else{
    document.getElementById('checkout_btn').setAttribute('data-target', '#exampleModalCenter')
    get_quat('_quantity','put_quantitiy','a-pro','sum_q');
  }
  
}

function validateForm() {
  let x = document.forms["quote_form"]["starting_date_q"].value;
  if (x == "") {
    return false;
  }
}

function validation_date(){
  
      var valid_span = document.getElementById("quantity_error")
      if(valid_span != null){
        valid_span.innerText = '';
      }
    
  
}

function calc() 
{
  var quantity = null;
  var _frequecy = null;
  var price = document.getElementById("price_pu");
  if(price != null){
    price = price.innerText.replace ( /[^\d.]/g, '' )
  }
  var noTickets = document.getElementById("_quantity")
  if(noTickets!=null){
    quantity = noTickets.value
  }
  var frequency = document.getElementById("frequency")
  if(frequency != null){
    var value = frequency.options[frequency.selectedIndex].text;
    if(value == "Select..."){
      quantity= 1;
      _frequecy = value
    }
    if(value == "Monthly"){
      quantity= 1;
      _frequecy = value

    }
    if(value == "Quarterly"){
      quantity= 3;
      _frequecy = value

    }
    if(value == "Annually"){
      quantity= 12;
      _frequecy = value

    }
    console.log("this is frequency: " + value)
  }
  var _date = null;
  
  var starting_date = document.getElementById("start_date")
  if(starting_date!=null){
    _date = starting_date.value;
    console.log("This is starting date: " + _date)
  }
  
  var total = parseFloat(price) * quantity
  console.log("total price: " + total)
  if (!isNaN(total)){
    document.getElementById("total").innerText = total
    document.getElementById("total_p").value = total
    document.getElementById("total_price").value = total
    document.getElementById("starting_date_q").value = _date
    document.getElementById("frequency_q").value = _frequecy
    console.log(document.getElementById("total_p").value) 
  }
  
}
calc()




