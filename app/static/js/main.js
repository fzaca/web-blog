window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple,{
            perPage: 20,
            perPageSelect: false,
            hiddenHeader: true,
            labels: {
                placeholder: "Search...",
                noRows: "No entries found",
                info: "",
                noResults: "No results match your search query",
            }
        });
    }
    // https://fiduswriter.github.io/simple-datatables/documentation/Options

});