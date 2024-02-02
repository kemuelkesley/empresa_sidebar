// form.js
$(document).ready(function() {
    $('#id_cep').on('blur', function() {
        let cep = $(this).val().replace(/\D/g, '');
        if (cep) {
            $.ajax({
                url: `https://viacep.com.br/ws/${cep}/json/`,
                dataType: 'json',
                success: function(data) {
                    if ('erro' in data) {
                        alert("CEP: " + cep + " não encontrado.");
                    } else {
                        // Preencha automaticamente os campos de endereço
                        $('#id_logradouro').val(data.logradouro);
                        $('#id_bairro').val(data.bairro);
                        $('#id_localidade').val(data.localidade);
                        $('#id_uf').val(data.uf);
                    }
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    console.error('Erro na requisição:', textStatus, errorThrown);
                }
            });
        }
    });
});
