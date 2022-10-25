function get_quat(quantity, put_quantitiy, available_pro , sum_q)
{
  get_quantity = document.getElementById(quantity).value;
  document.getElementById(put_quantitiy).value = get_quantity;

  get_availablePro = document.getElementById(available_pro).innerText.replace ( /[^\d.]/g, '' );
  document.getElementById('avail_pro2').value = get_availablePro
  
  console.log('farhan Ali'+document.getElementById('avail_pro2').value)
  
  sum_product = get_availablePro - get_quantity ;
  document.getElementById(sum_q).value = sum_product;
    
}


function validate_value()
{
  minimum_val = parseInt(document.getElementById('minimum_lable').innerText.replace ( /[^\d.]/g, '' ))
  input_val = document.getElementById('_quantity').value;


  maximum_val =parseInt(document.getElementById('a-pro').innerText.replace( /[^\d.]/g, ''))
  document.getElementById('quan').value = input_val
  console.log(document.getElementById('quan').value)
  if(input_val < minimum_val || input_val > maximum_val)
  {
    
    alert('Your quantity must be between Minimum or Available Product!')
    document.getElementById('checkout_btn').setAttribute('data-target', '#')
  }else{
    document.getElementById('checkout_btn').setAttribute('data-target', '#exampleModalCenter')
    get_quat('_quantity','put_quantitiy','a-pro','sum_q');
  }
  
}

function calc() 
{
  var price = document.getElementById("price_pu").innerText.replace ( /[^\d.]/g, '' );
  var noTickets = document.getElementById("_quantity").value;
  var total = parseFloat(price) * noTickets
  console.log("total price: " + total)
  if (!isNaN(total))
    document.getElementById("total").innerText = total
    document.getElementById("total_p").value = total
    document.getElementById("total_price").value = total
    console.log(document.getElementById("total_p").value) 
}

setTimeout(function(){
  
}, 1000); 
calc();



