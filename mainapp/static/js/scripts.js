/* console.log('entrei js v3');*/

$( document ).ready(function() {

    // configuração do filtro
    var filter     = $('#filteruf');
    var baseUrl   = 'http://localhost:8000/';

    // configuração da busca
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    // Ação do filtro (change)
    $(filteruf).change(function() {
        var filteruf = $(this).val();
        window.location.href = baseUrl + '?filteruf=' + filteruf;
    });

    // Ação da busca (click)
    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

});
