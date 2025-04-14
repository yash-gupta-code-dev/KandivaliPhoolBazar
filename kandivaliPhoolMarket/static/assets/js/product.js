$(document).ready(function () {
    $.ajax({
        url: "http://127.0.0.1:8000/kpm/all/products/",
        type: "GET",
        dataType: "json",
        success: function (data) {
            const productList = $("#product-list");
            productList.empty(); // Clear existing cards

            data.forEach(product => {
                const productCard = $(`
                    <div class="bg-white rounded shadow-sm overflow-hidden border border-gray-100 hover:shadow-md transition w-full max-w-xs mx-auto">
                        <a href="/products/${product.id}/" class="no-underline text-inherit block h-full w-full product-link">
                            <div>
                                <div class="h-48 overflow-hidden">
                                  <img src="${product.image || 'https://via.placeholder.com/300x200'}" alt="${product.name}" class="w-full h-full object-contain">

                                </div>
                                <div class="p-4">
                                    <h3 class="font-semibold text-lg">${product.name}</h3>
                                    <p class="text-gray-600 text-sm mt-1">${product.description || 'No description available.'}</p>
                                    <div class="mt-4 flex items-center justify-between">
                                        <span class="bg-gray-900 text-white px-3 py-1.5 rounded text-sm whitespace-nowrap hover:bg-gray-800 transition flex items-center gap-2 w-fit">
                                            <i class="ri-whatsapp-line ri-lg"></i>
                                            Get a Quote
                                        </span>
                                    </div>
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
