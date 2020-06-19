function getCSRFToken(str){
    let cookies = str.split(';')
    let token = ""

    cookies.forEach(cookie => {
        if( cookie.includes('csrftoken='))
            token = cookie.replace('csrftoken=','')
    })

    return token
}

function populateTable(tableId,data,urls){
    table = $('#'+tableId).empty()
    table.append(`
        <tr>
            <th>Product</th>
            <th>Date Ordered</th>
            <th>Status</th>
            <th>Update</th>
            <th>Remove</th>
        </tr>
    `)

    data.forEach(elem => {
        let updateURL = urls.update.replace('1',elem.id)
        let deleteURL = urls.delete.replace('1',elem.id)

        table.append(`
        <tr>
            <td>${elem.product}</td>
            <td>${elem.date_created}</td>
            <td>${elem.status}</td>
            <td><a href="${updateURL}" class="btn btn-sm btn-info">Update</a></td>
            <td><a href="${deleteURL}" class="btn btn-sm btn-danger">Delete</a></td>
        </tr>
        `)
    });
}

