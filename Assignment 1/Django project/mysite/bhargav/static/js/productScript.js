

function updateCartContainer(){
    productImage = document.getElementById('ProductImage').src;
    productTitle = document.getElementsByClassName('productTitle')[0].innerText;
    productPrize = document.getElementsByClassName('productPrice')[0].innerText;
    localStorage.setItem("productImage", productImage);
    localStorage.setItem("productTitle", productTitle);
    localStorage.setItem("productPrize", productPrize);
}

