/* console.log('entrei js v3');*/

$( document ).ready(function() {

    // configuração do filtro uf
    var filteruf     = $('#filteruf');
    var baseUrl   = 'http://localhost:8000/';

    // configuração do filtro status
    var filterstatus     = $('#filterstatus');
    var baseUrlIrmaos   = 'http://localhost:8000/irmaos/';

    // configuração da busca
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    // configuração da busca irmao
    var searchBtnIrmao = $('#searchirmao-btn');
    var searchFormIrmao = $('#searchirmao-form');

    // configuração da busca local de interesse
    var searchBtnLocalInteresse = $('#search-btn-localinteresse');
    var searchFormLocalInteresse = $('#searchlocalinteresse-form');

    // Ação do filtro uf (change)
    $(filteruf).change(function() {
        var filteruf = $(this).val();
        window.location.href = baseUrl + '?filteruf=' + filteruf;
    });

    // Ação do filtro status (change)
    $(filterstatus).change(function() {
        var filterstatus = $(this).val();
        window.location.href = baseUrlIrmaos + '?filterstatus=' + filterstatus;
    });

    // Ação da busca Local (click)
    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    // Ação da busca Irmao (click)
    $(searchBtnIrmao).on('click', function() {
        searchFormIrmao.submit();
    });

    // Ação da busca Local de Interesse (click)
    $(searchBtnLocalInteresse).on('click', function() {
        searchFormLocalInteresse.submit();
    });

});
