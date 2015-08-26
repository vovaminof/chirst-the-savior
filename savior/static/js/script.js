/*
---------------------------------------------------------------
  CUSTOM SCRIPT FOR CHURCH TEMPLATE
  Author	: SURJITH S M
  URI		: http://theemforest.net/user/surjithctly
  Updated	: 26 May 2015
---------------------------------------------------------------
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(document).ready(function() {

 
/* --------------------
  EVENT CAROUSEL 
----------------------- */

if(jQuery().owlCarousel) {
$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
	navText: [
      "<span class='nav-arrow left'></i>",
      "<span class='nav-arrow right'></i>"
      ],
    responsive:{
        0:{
            items:1
        },
		550:{
            items:2
        },
        768:{
            items:3
        },
        992:{
            items:4
        }
    }
})

$('.owl-carousel2').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
	navText: false,
    responsive:{
        0:{
            items:1
        }
    }
})
}

 
/* --------------------
   IMAGE GALLERY 
----------------------- */
 
if(jQuery().fancybox) {
 $('.fancybox').fancybox();			
}	
		
 
/* --------------------
   SHRINK HEADER 
----------------------- */
 
$(function(){
 var shrinkHeader = 300;
  $(window).scroll(function() {
    var scroll = getCurrentScroll();
      if ( scroll >= shrinkHeader ) {
           $('.navbar').addClass('shrink');
        }
        else {
            $('.navbar').removeClass('shrink');
        }
  });
function getCurrentScroll() {
    return window.pageYOffset || document.documentElement.scrollTop;
    }
});

 
/* --------------------
   PRAYER FORM 
----------------------- */
   
 
$('#prayerForm').ketchup().submit(function() {
	if ($(this).ketchup('isValid')) {
    $('.prayer-result').hide();
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $('#prayerForm input[name=csrfmiddlewaretoken]').val());
            }
        }
    });
		$.ajax({
			url: 'savior/send-request/',
			type: 'POST',
			data: {
        name: $('#pray-name').val(),
        text: $('#pray-text').val()
			},
			success: function(data){
        if (data.error) {
          $('#prayer-error').text(data.error.msg);
          $('#prayer-error').show();
        } else {
          $('#prayer-success').show().delay(3000).fadeOut();
          $('#pray-name').val('');
          $('#pray-text').val('');
        }
			},
			error: function() {
				$('#prayer-error').html('Sorry, an error occurred.');
			}
		});
	}
	return false;
});
	
	

}); /*End Document Ready*/
 