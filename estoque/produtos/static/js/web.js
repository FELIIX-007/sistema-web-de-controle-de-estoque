const forgotPasswordLink = document.querySelector('.adiciona-produtos');
        const modal = document.getElementById('recoverModal');
        const closeModalButton = document.getElementById('closeModal');

        // Abrir o modal ao clicar no link
        forgotPasswordLink.addEventListener('click', (e) => {
            e.preventDefault(); // Evita o redirecionamento padrão
            modal.style.display = 'flex'; // Mostra o modal
        });

        // Fechar o modal ao clicar no botão de fechar
        closeModalButton.addEventListener('click', () => {
            modal.style.display = 'none'; // Esconde o modal
        });

        // Fechar o modal ao clicar fora dele
        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.style.display = 'none';
            }
        });