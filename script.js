document.addEventListener('DOMContentLoaded', function() {
 
    const searchButton = document.getElementById('search-button');
    const clientDetails = document.getElementById('client-details');
    const clientSearch = document.getElementById('client-search');
    const clientDropdown = document.getElementById('client-dropdown');
    const clientList = document.getElementById('client-list');
    const imageContainer = document.getElementById('image-container'); // Add this line

    searchButton.addEventListener('click', function() {
        const clientName = clientSearch.value;
        fetch('/get_client_details', {
            method: 'POST',
            body: new URLSearchParams({
                'client_name': clientName
            }),
        })
        .then(response => response.json())
        .then(data => {
            clientDetails.innerHTML = `Name: ${data.name}<br>Email: ${data.email}`;
        });
    });
});


