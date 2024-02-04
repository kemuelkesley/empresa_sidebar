$(document).ready(function() {
    $('#tabela').DataTable({
        paging: true,  // Ativar paginação
        searching: true,  // Ativar a barra de pesquisa
        ordering: true,  // Ativar a ordenação
        responsive: true,  // Tornar a tabela responsiva
        autoWidth: false,  // Desativar o ajuste automático da largura
        lengthChange: true,  // Ativar a seleção de quantidade de registros por página
        lengthMenu: [5, 10, 25, 50, 100],  // Quantidade de registros por página
        pageLength: 5,  // Quantidade de registros por página inicial
        

        // Tradução para português
        language: {
            "url": "//cdn.datatables.net/plug-ins/1.10.25/i18n/Portuguese-Brasil.json"
        }
        // ... outras opções conforme necessário
    });
});
