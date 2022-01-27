cartContainer = document.getElementsByClassName('cartContainer')[0];

window.addEventListener('load', () => {
    productImage = localStorage.getItem('productImage');
    productTitle = localStorage.getItem('productTitle');
    productPrize = localStorage.getItem('productPrize');

    div = document.createElement('div');
    div.classList.add('row');
    insideDiv = `<div class="col-xs-3 cartImage"> <img src="${productImage}"></div>
    <div class="col-xs-3 cartTitle"> ${productTitle} </div>
    <div class="col-xs-3 cartPrice"> ${productPrize}</div>
    <div class="col-xs-3 removeButton"> Remove</div>`;

    div.innerHTML = insideDiv;
    cartContainer.appendChild(div);

    removeButton = document.getElementsByClassName('removeButton');
    for(var i=0; i<removeButton.length; i++){
        removeButton[i].addEventListener('click', removeFromCart);
    }
})
function removeFromCart(e){
    e.target.parentElement.remove();
}
