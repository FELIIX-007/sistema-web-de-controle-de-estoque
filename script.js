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

// Função para editar um item da tabela
function editItem(row) {
  const code = row.cells[0].textContent;
  const name = row.cells[1].textContent;
  const quantity = row.cells[2].textContent;

  editForm.querySelector('#editCode').value = code;
  editForm.querySelector('#editName').value = name;
  editForm.querySelector('#editQuantity').value = quantity;

  editModal.style.display = 'block';

  editForm.currentEditedItem = row;
}

// Função para deletar um item da tabela
function deleteItem(row) {
  if (confirm('Deseja deletar este item?')) {
    tableBody.removeChild(row);
  }
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