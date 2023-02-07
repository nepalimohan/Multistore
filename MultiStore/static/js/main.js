(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            }
        }
    });


    //Product Quantity
    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });

    // Get all quantity inputs
// Get all quantity inputs
    // const quantityInputs = document.querySelectorAll(".quantity input");

    // // Get the total amount display element
    // const totalAmountDisplay = document.querySelector("#total-amount");

    // // Loop through each quantity input and add event listeners for minus and plus buttons
    // quantityInputs.forEach(input => {
    // const minusButton = input.previousElementSibling;
    // const plusButton = input.nextElementSibling;

    // // Decrease value when minus button is clicked
    // minusButton.addEventListener("click", function() {
    //     let value = parseInt(input.value);
    //     if (value > 1) {
    //     input.value = value - 1;
    //     calculateTotalAmount();
    //     }
    // });

    // // Increase value when plus button is clicked
    // plusButton.addEventListener("click", function() {
    //     let value = parseInt(input.value);
    //     input.value = value + 1;
    //     calculateTotalAmount();
    // });
    // });

    // // Function to calculate total amount based on quantity inputs
    // function calculateTotalAmount() {
    // let totalAmount = 0;
    // quantityInputs.forEach(input => {
    //     let quantity = parseInt(input.value);
    //     let price = parseInt(input.dataset.price);
    //     totalAmount += quantity * price;
    // });

    // // Update the total amount display
    // totalAmountDisplay.textContent = totalAmount;
    // // $('#total').html(data)
    // }
    $('.plus-cart').click(function(){
        var id = $(this).attr("pid").toString();
        var eml = this.parentNode.children[2] //gives the main object data of the parent node child
        var url = $('#cart').attr('url');
        console.log(id) 
        $.ajax({
            type:"GET",
            url: url,
            data:{
                prod_id: id 
            },
            success: function(data) {
                $(eml).text(data.quantity)
                $(document.getElementById("amount")).text(data.amount)
                $(document.getElementById("totalamount")).text(data.totalamount)
                //  eml.innerText = data.quantity
                //  document.getElementById("amount").innerText = data.amount
                //  document.getElementById("totalamount").innerText = data.totalamount
            }
        })
    });
    
})(jQuery);

