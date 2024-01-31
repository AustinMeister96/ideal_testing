/** Generic success message handler for all pages. **/
function checkForSuccessMessage() {
  var urlParams = new URLSearchParams(window.location.search);

  //If the URL has a submitted parameter, add a success message to the page. Then fade it in and out.
  if (urlParams.get('submitted') === 'True') {
    var flashMessage = document.createElement('div');
    flashMessage.classList.add('flash-message');
    flashMessage.innerText = 'Data saved successfully.';
    document.body.appendChild(flashMessage);
    
    setTimeout(function () {
      flashMessage.classList.add('!opacity-100');
    }, 500); 

    setTimeout(function () {
      flashMessage.classList.remove('!opacity-100');
    }, 4500); 
  }
}

/** Initialize all datepickers on the page. **/
function initializeDatepickers() {
  let $datepickers = $('.datepicker');

  if ($datepickers.length == 0) {
    $datepickers.each(function() {
      $(this).datepicker({
        format: 'yyyy-mm-dd',
        autoclose: true,
      });
    })
  }
}

$(function() {
  checkForSuccessMessage();
  initializeDatepickers();

  //data-toggle-input="id_still_smoking_pipe_" data-target-class="smoke_pipe" data-visible-value="True"

  // Toggle fields based on the value of a checkbox or radio button.
  $('.field-toggler.checkbox-toggler').each(function() {
    let $toggler = $(this);
    let visible_value = $toggler.data('visible-value');

    //If the user clicks on the checkbox, toggle the visibility of the target based on the value matching the visible-value data attribute in the parent wrapper.
    $toggler.find('input[name="' + $toggler.data('input-name') + '"]').on('click', function () {      
      if ($(this).val() == visible_value) {
        $($toggler.data('target-selector')).show();
      } else {
      $($toggler.data('target-selector')).show();
      }
    });

    /*** DEBUG NOTICE: For now we always show the targets ***/
    //On load set the visibility of the target based on the value matching the visible-value data attribute in the parent wrapper.
    if ($toggler.find('input[name="' + $toggler.data('input-name') + '"]:checked').val() == $(this).data('visible-value')) {
      $($toggler.data('target-selector')).show();
    } else {
      $($toggler.data('target-selector')).show();
    }
  });
});