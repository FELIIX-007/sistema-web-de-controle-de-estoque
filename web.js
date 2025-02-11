const forgotPasswordLink = document.querySelector('.adiciona-produtos');
        const modal = document.getElementById('recoverModal');
        const closeModalButton = document.getElementById('closeModal');
        const bntfechaModal = document.getElementById('bnt-fechaModal')
        const bntfechaCadrastro = document.querySelector('.bnt-cadastrar')

        // Abrir o modal ao clicar no link
        forgotPasswordLink.addEventListener('click', (e) => {
            e.preventDefault(); // Evita o redirecionamento padrão
            modal.style.display = 'flex'; // Mostra o modal
        });

        // Fechar o modal ao clicar no botão de fechar
        closeModalButton.addEventListener('click', () => {
            modal.style.display = 'none'; // Esconde o modal
        });

        // Fechar o modal ao clicar no botão de fechar
        bntfechaCadrastro.addEventListener('click', () => {
            modal.style.display = 'none'; // Esconde o modal
        });

        bntfechaModal.addEventListener('click', () => {
            modal.style.display = 'none'; // Esconde o modal
        });

        // Fechar o modal ao clicar fora dele
        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        });



        // modal de editar produtos

        const EditaProdutos = document.getElementById('bi-pencil-fill');
        const modalEditarProdutos = document.getElementById('recoverModalEditar');
        const closeModalEditar = document.getElementById('closeModalEditar');
        const bntEditarModal = document.getElementById('bnt-fechaEditar')
        const bntfechaCadrastroEditar = document.querySelector('.bnt-editar')

        // Abrir o modal ao clicar no link
        EditaProdutos.addEventListener('click', (e) => {
            e.preventDefault(); // Evita o redirecionamento padrão
            modalEditarProdutos.style.display = 'flex'; // Mostra o modal
        });

        // Fechar o modal ao clicar no botão de fechar
        closeModalEditar.addEventListener('click', () => {
            modalEditarProdutos.style.display = 'none'; // Esconde o modal
        });

        // Fechar o modal ao clicar no botão de salvar
        bntfechaCadrastroEditar.addEventListener('click', () => {
            modalEditarProdutos.style.display = 'none'; // Esconde o modal
        });

        bntEditarModal.addEventListener('click', () => {
            modalEditarProdutos.style.display = 'none'; // Esconde o modal
        });

        // Fechar o modal ao clicar fora dele
        window.addEventListener('click', (e) => {
            if (e.target === modalEditarProdutos) {
                modalEditarProdutos.style.display = 'none';
            }
        });