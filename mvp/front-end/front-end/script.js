
function getList() {
  let url = 'https://fakestoreapi.com/products';
  fetch(url)
      .then((response) => response.json())
      .then((data) => {
          const tableBody = document.querySelector('#myTable tbody');
          tableBody.innerHTML = '';

          data.forEach((item) => {
              insertList(item.title, item.quantity, item.price);
          });
      })
      .catch((error) => {
          console.error('Error:', error);
      });
}


function insertList(nameProduct, quantity, price) {
  var item = [nameProduct, quantity, price];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
      var cel = row.insertCell(i);
      cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1));
  document.getElementById('newInput').value = '';
  document.getElementById('newQuantity').value = '';
  document.getElementById('newPrice').value = '';

  removeElement();
}


function insertButton(parent) {
  let span = document.createElement('span');
  let txt = document.createTextNode('\u00D7');
  span.className = 'close';
  span.appendChild(txt);
  parent.appendChild(span);
}


function removeElement() {
  let close = document.getElementsByClassName('close');
  let i;
  for (i = 0; i < close.length; i++) {
      close[i].onclick = function () {
          let div = this.parentElement.parentElement;
          const nomeItem = div.getElementsByTagName('td')[0].innerHTML;
          if (confirm('Você tem certeza?')) {
              div.remove();
              deleteItem(nomeItem);
              alert('Removido!');
          }
      };
  }
}


function deleteItem(item) {
  let url = 'http://127.0.0.1:5000/produto?nome=' + item;
  fetch(url, {
      method: 'delete',
  })
      .then((response) => response.json())
      .catch((error) => {
          console.error('Error:', error);
      });
}


function newItem() {
  let inputProduct = document.getElementById('newInput').value;
  let inputQuantity = document.getElementById('newQuantity').value;
  let inputPrice = document.getElementById('newPrice').value;

  if (inputProduct === '') {
      alert('Escreva o nome de um item!');
  } else if (isNaN(inputQuantity) || isNaN(inputPrice)) {
      alert('Quantidade e valor precisam ser números!');
  } else {
      insertList(inputProduct, inputQuantity, inputPrice);
      postItem(inputProduct, inputQuantity, inputPrice);
      alert('Item adicionado!');
  }
}


function postItem(inputProduct, inputQuantity, inputPrice) {
  const formData = new FormData();
  formData.append('nome', inputProduct);
  formData.append('quantidade', inputQuantity);
  formData.append('valor', inputPrice);

  let url = 'http://127.0.0.1:5000/produto';
  fetch(url, {
      method: 'post',
      body: formData,
  })
      .then((response) => response.json())
      .catch((error) => {
          console.error('Error:', error);
      });
}


document.querySelector('button').addEventListener('click', getList);


getList();





