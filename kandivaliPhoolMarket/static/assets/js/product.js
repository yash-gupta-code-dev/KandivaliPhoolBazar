$(document).ready(function () {
    $.ajax({
        url: "http://127.0.0.1:8000/kpm/all/products/",
        type: "GET",
        dataType: "json",
        success: function (data) {


            console.log(data)
            const productList = $("#product-list");
            const template = $("#product-card-template");
            
            data.forEach(product => {
                // Clone template
                let card = template.clone().removeAttr("id").removeClass("hidden");
           
                // Fill in data
                card.find(".product-title").text(product.name);
                card.find(".product-description").text(product.description || "No description available.");
                card.find(".product-image").attr("src", product.image || "No Image Found");

                // Append to the list
                productList.append(card);
            });
        },
        error: function (xhr, status, error) {
            console.error("AJAX error:", status, error);
            $("#product-list").html("<p class='text-red-500'>Failed to load products.</p>");
        }
    });
});

