let adjust_4_menu_admin = inputs => {
    inputs.forEach(input => {
        $(input).parent().addClass(input.value);
    })
}

let openPanel = (body, title, close = true, footer = null, idmodal="modal-panel-message" ) => {
    let template = Handlebars.compile( $( "#modal-panel-message-template" ).html() );
    let html = template( { title, body, footer, close, idmodal } );
    $( `#${idmodal}` ).remove();
    $( document.body ).append( $( html ) );
    let modal = new bootstrap.Modal(document.getElementById(idmodal));
    modal.show();
};

let closePanel = (idmodal="modal-panel-message") => {
   let modal = new bootstrap.Modal(document.getElementById(idmodal));
   modal.hide
   modal.dispose()
};

let showDeletingConfirmation = (url, elemento="elemento", pre_elemento="el") => {
    let template = Handlebars.compile( $( "#deleting-confirmation-template" ).html() );
    let html = template( { url, elemento, pre_elemento } );
    openPanel( html, "Confirmación de Eliminación");
    return false;
};

let update_many_records = () => {
    let ids = Array.from($(`#main-data-table input[type="checkbox"]:checked`)).map(item => item.value);
    if(ids.length > 0) {
        location.href = update_url.replace(`/0`,`/${ids[0]}`);
    }
}

let delete_many_records = () => {
    let ids = Array.from($(`#main-data-table input[type="checkbox"]:checked`)).filter(item => item.name === "pk" && !isNaN(item.value));
    if(ids.length > 0) {
        openPanel($(`#deleting-many-confirmation-template`).html(), "Confirmación de Eliminación");
    }
}

let delete_many_records_excecute = () => {
    let ids = Array.from($(`#main-data-table input[type="checkbox"]:checked`)).filter(item => item.name === "pk" && !isNaN(item.value)).map(item => item.value).join(",");
    if(ids.length > 0) {
        $.post(delete_many_url, {
            ids,
            'csrfmiddlewaretoken': $(`#frm-csrfmiddlewaretoken input[name="csrfmiddlewaretoken"]`).val()
        }, response => {
            if (ids == response) {
                location.reload();
            } else {
                alert(`Error en el procesamiento de eliminación:
            ------------------------------------------------
            enviado: ${ids}
            recibido: ${response}
            `);
            }
        }, "text").fail(ajax_failure);
    }
}

let create_tipo_opcion = () => {
    openPanel($(`#opcion-form-template`).html(), "Nueva Opción");
    $(`#main-form-option input[name="action"]`).val('create')
}

let delete_tipo_opcion = () => {
    cbk = Array.from($(`#main-data-table input[type="checkbox"]`)).filter(item => item.checked);
    if(cbk.length > 0) {
        delete_many_records();
        let btn = $(`#modal-panel-message button[type="submit"]`);
        let lbl = btn.html();
        let cell = btn.parent();
        btn.remove();
        cell.append($(`<button type="button" onclick="delete_tipo_opcion_execute()" class="btn btn-outline-secondary" title="Aceptar">${lbl}</button>`));
    }
}

let delete_tipo_opcion_execute = () => {
    cbk = Array.from($(`#main-data-table input[type="checkbox"]`)).filter(item => item.checked).map(item => item.value);
    let token = $(`#frm-csrfmiddlewaretoken input[name="csrfmiddlewaretoken"]`).val();
    let frm = $(`
        <form method="post" enctype="multipart/form-data">
            <input type="hidden" name="csrfmiddlewaretoken" value="${token}">
            <input type="hidden" name="action" value="delete" />
            <input type="hidden" name="extra" id="extra" value="${cbk.join(',')}" />
        </form>`);
    $(document.body).append(frm);
    frm.submit();
}

let ajax_failure = (jqXHR, textStatus, errorThrown) => {
    let message = `Error en el procesamiento de eliminación:
        ------------------------------------------------
        readyState: ${jqXHR.readyState}
        status: ${jqXHR.status}
        statusText: ${jqXHR.statusText}
        textStatus: ${textStatus}
        errorThrown: ${errorThrown}
        `;
    alert(message);
    return message;
}

window.addEventListener('DOMContentLoaded', evt => {

    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
            document.body.classList.toggle('sb-sidenav-toggled');
        }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

    const mainDataTable = document.body.querySelector('#main-data-table');
    if (mainDataTable) {
        new simpleDatatables.DataTable(mainDataTable, {
            language: {url: '//cdn.datatables.net/plug-ins/2.0.8/i18n/es-MX.json'},
            perPage: 50,
            perPageSelect: [50, 100, ["Todo", 0]],
            firstLast: true,
            labels: {
                placeholder: "Buscar ...",
                searchTitle: "Buscar en la tabla",
                pageTitle: "Página {page}",
                perPage: "registros por página",
                noRows: "No se encontraron entradas",
                info: "Mostrando entradas {start} a {end} de {rows}",
                noResults: "No hay resultados que coincidan con la búsqueda"
            }});
        let inputs = mainDataTable.querySelectorAll(`input[type="hidden"]`);
        let rows = mainDataTable.querySelectorAll(`tbody tr`);
        if(inputs.length === rows.length){
            adjust_4_menu_admin(Array.from(inputs));
        }
    }

    const mainForm = document.body.querySelector('form#main-form');
    if(mainForm) {
        if(read_only) {
            Array.from(mainForm.querySelectorAll(
                "input, textarea, button, select")).forEach(
                    control => {
                        control.disabled = true;
                        control.readonly = true;
                    });
        }
    }
});
