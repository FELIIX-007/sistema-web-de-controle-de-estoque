// Seleciona elementos do DOM
const searchInput = document.querySelector('.search-bar input');
const tableBody = document.querySelector('table tbody');
const newItemButton = document.querySelector('.new-item');

// Modais
const editModal = document.getElementById('editModal');
const addModal = document.getElementById('addModal');

// Formulários
const editForm = document.getElementById('editForm');
const addForm = document.getElementById('addForm');

// Botões de fechar os modais
const closeEditModalButton = editModal.querySelector('.close-button');
const closeAddModalButton = addModal.querySelector('.close-button');

// Função para buscar itens na tabela
function searchItems() {
  const searchTerm = searchInput.value.toLowerCase();

  const tableRows = tableBody.querySelectorAll('tr');

  tableRows.forEach(row => {
    const code = row.cells[0].textContent.toLowerCase();
    const name = row.cells[1].textContent.toLowerCase();

    if (code.includes(searchTerm) || name.includes(searchTerm)) {
      row.style.display = 'table-row';
    } else {
      row.style.display = 'none';
    }
  });
}


// Função para adicionar um novo item à tabela
function addNewItem() {
  addModal.style.display = 'block';
}

// Função para salvar as alterações no modal de edição
function saveEditChanges(event) {
  event.preventDefault();

  const code = editForm.querySelector('#editCode').value;
  const name = editForm.querySelector('#editName').value;
  const quantity = editForm.querySelector('#editQuantity').value;

  const row = editForm.currentEditedItem;
  row.cells[0].textContent = code;
  row.cells[1].textContent = name;
  row.cells[2].textContent = quantity;

  editModal.style.display = 'none';
}

// Função para cadastrar um novo item no modal de cadastro
function addNewItemToList(event) {
  event.preventDefault();

  const code = addForm.querySelector('#addCode').value;
  const name = addForm.querySelector('#addName').value;
  const quantity = addForm.querySelector('#addQuantity').value;

  const newRow = tableBody.insertRow();

  const codeCell = newRow.insertCell();
  const nameCell = newRow.insertCell();
  const quantityCell = newRow.insertCell();
  const editCell = newRow.insertCell();
  const deleteCell = newRow.insertCell();

  codeCell.textContent = code;
  nameCell.textContent = name;
  quantityCell.textContent = quantity;

  const editButton = document.createElement('button');
  editButton.className = 'edit';
  editButton.innerHTML = '<i class="fas fa-edit"></i>';
  editButton.addEventListener('click', () => editItem(newRow));
  editCell.appendChild(editButton);

  const deleteButton = document.createElement('button');
  deleteButton.className = 'delete';
  deleteButton.innerHTML = '<i class="fas fa-trash-alt"></i>';
  deleteButton.addEventListener('click', () => deleteItem(newRow));
  deleteCell.appendChild(deleteButton);

  addModal.style.display = 'none';
  addForm.reset();
}

// Eventos para elementos estáticos
searchInput.addEventListener('input', searchItems);
newItemButton.addEventListener('click', addNewItem);

// Eventos para modais
closeEditModalButton.addEventListener('click', () => editModal.style.display = 'none');
closeAddModalButton.addEventListener('click', () => addModal.style.display = 'none');

// Eventos para formulários
editForm.addEventListener('submit', saveEditChanges);
addForm.addEventListener('submit', addNewItemToList);

// Eventos para botões existentes (delegação de eventos)
tableBody.addEventListener('click', (event) => {
  if (event.target.classList.contains('edit')) {
    const row = event.target.parentNode.parentNode;
    editItem(row);
  } else if (event.target.classList.contains('delete')) {
    const row = event.target.parentNode.parentNode;
    deleteItem(row);
  }
});



document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll(".delete").forEach(button => {
      button.addEventListener("click", function(event) {
          event.preventDefault();  // Impede o comportamento padrão de navegação

          let produtoId = this.getAttribute("data-id");
          if (!produtoId) {
              console.error("Erro: Produto ID não encontrado.");
              return;
          }

          // Exibe a confirmação antes de proceder
          let confirmacao = confirm("Tem certeza que deseja excluir este produto??");
          if (confirmacao) {
              // Envia a requisição de exclusão apenas se o usuário confirmar
              fetch(`/produtos/excluir/${produtoId}/`, {
                  method: "POST", 
                  headers: {
                      "X-CSRFToken": getCookie("csrftoken"),  // Para garantir que a requisição POST seja segura
                  }
              })
              .then(response => {
                  if (response.ok) {
                      // Se a exclusão for bem-sucedida, remove a linha da tabela
                      this.closest("tr").remove();
                  } else {
                      alert("Erro ao excluir o produto.");
                  }
              })
              .catch(error => console.error("Erro:", error));
              location.reload();
          } else {
              // Se o usuário cancelar, apenas loga a ação
              console.log("Exclusão cancelada.");
          }
      });
  });
});


// Função para pegar o CSRF token (necessário para requisições POST no Django)
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
