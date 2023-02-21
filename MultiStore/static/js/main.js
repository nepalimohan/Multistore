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


    // Product Quantity
    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 1) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 1;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });

    
    $('.plus-cart').click(function(){
        var id = $(this).attr("pid").toString();
        var eml = this.parentNode.children[2] //gives the main object data of the parent node child
        var url = $('#cart').attr('url');
        console.log('plus cart') 

        $.ajax({
            type:"GET",
            url: url,
            data:{
                prod_id: id 
            },
            success: function(data) {
                // $(eml).text(data.quantity)
                // $(document.getElementById("quantity")).val(data.quantity)
                console.log(data.quantity)
                $(document.getElementById("amount")).text(data.amount)
                $(document.getElementById("totalamount")).text(data.totalamount)
                //  eml.innerText = data.quantity
                //  document.getElementById("amount").innerText = data.amount
                //  document.getElementById("totalamount").innerText = data.totalamount
            }
        })
    });

    $('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    // var eml = this.parentNode.children[2] //gives the main object data of the parent node child
    console.log(id) 
    console.log('minus cart') 
    var url = $('#minus-cart').attr('url');
    $.ajax({
        type:"GET",
        url:url,
        data:{
            prod_id: id 
        },
        success: function(data) {
            //  eml.innerText = data.quantity
             document.getElementById("amount").innerText = data.amount
             document.getElementById("totalamount").innerText = data.totalamount
        }
    })
})

$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this
    var url = $('#remove-cart').attr('url');
    console.log(url)
    console.log('remove cart') 

    $.ajax({
        type:"GET",
        url:url,
        data:{
            prod_id: id 
        },
        success: function(data) {
            console.log("Delete")
            document.getElementById("amount").innerText = data.amount
            document.getElementById("totalamount").innerText = data.totalamount
            eml.parentNode.parentNode.remove() 
            // whole rows of divs are deleted using multiple parent node 5:33:17
        }
    })
})

$('.mohan').click(function (e){
    e.preventDefault();
    var id = $(this).attr("pid").toString();
    var quantity = $("#quantity").val();
    var url = $("#data").val();
    console.log(url)

    $.ajax({
        type: "GET",
        url: url,
        data:{
            id:id,
            quantity:quantity,
        },
        success: function(data) {
            console.log('success')
            alert("Added to cart successfully");
        }
    })

    

})
    
})(jQuery);

