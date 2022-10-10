function get_quat(quantity, put_quantitiy, available_pro, sum_q){
    get_quantity = document.getElementById(quantity).value;
    document.getElementById(put_quantitiy).value = get_quantity;

    get_availablePro = document.getElementById(available_pro).innerText.replace ( /[^\d.]/g, '' );;
    document.getElementById('avail_pro2').value = get_availablePro
    
    sum_product = get_availablePro - get_quantity ;
    document.getElementById(sum_q).value = sum_product;
  
    
    
  }



