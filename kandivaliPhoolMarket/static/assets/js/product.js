$(document).ready(function () {
    $.ajax({
        url: "http://127.0.0.1:8000/all/products/",
        type: "GET",
        dataType: "json",
        success: function (data) {
            const productList = $("#product-list");
            productList.empty(); // Clear existing cards

            data.forEach(product => {
                const productCard = $(`
    <div class="bg-white rounded-lg shadow-sm overflow-hidden border border-gray-100 hover:shadow-md transition h-full flex flex-col">
        <a href="/products/${product.product_id}/" class="no-underline text-inherit flex flex-col h-full">
            <div class="h-48 overflow-hidden flex-shrink-0">
                <img  src="${product.image || 'https://via.placeholder.com/300x200'}" 
                     alt="${product.name}" 
                     class="w-full h-full object-contain">
            </div>
            <div class="p-4 flex-grow flex flex-col">
                <h3 class="font-semibold text-lg mb-2">${product.name}</h3>
                 <p class="text-gray-600 text-sm mb-4 truncate" title="${product.description || 'No description available.'}">
                    ${product.description ? product.description.substring(0, 60 ) + (product.description.length > 60 ? '...' : '') : 'No description available.'}
                </p>
                <div class="mt-auto">
                    <span class="bg-gray-900 text-white px-3 py-2 rounded text-sm hover:bg-gray-800 transition flex items-center justify-center gap-2">
                        <i class="ri-whatsapp-line ri-lg"></i>
                        Get a Quote
                    </span>
                </div>
            </div>
        </a>
    </div>
`);

                productList.append(productCard);
            });
        },
        error: function (xhr, status, error) {
            console.error("AJAX error:", status, error);
            $("#product-list").html("<p class='text-red-500'>Failed to load products.</p>");
        }
    });
});
