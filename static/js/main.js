var $dropzone = $('.image_picker'),
    $droptarget = $('.drop_target'),
    $dropinput = $('#inputFile'),
    $dropimg = $('.image_preview'),
    $remover = $('[data-action="remove_current_image"]');




$dropzone.on('dragover', function() {
  $droptarget.addClass('dropping');
  return false;
});

$dropzone.on('dragend dragleave', function() {
  $droptarget.removeClass('dropping');
  return false;
});

$dropzone.on('drop', function(e) {
  $droptarget.removeClass('dropping');
  $droptarget.addClass('dropped');
  $remover.removeClass('disabled');
  e.preventDefault();
  
  var file = e.originalEvent.dataTransfer.files[0],
      reader = new FileReader();

  reader.onload = function(event) {
    $dropimg.css('background-image', 'url(' + event.target.result + ')');
  };
  
  console.log(file);
  reader.readAsDataURL(file);

  return false;
});

$dropinput.change(function(e) {
  $droptarget.addClass('dropped');
  $remover.removeClass('disabled');
  $('.image_title input').val('');
  
  var file = $dropinput.get(0).files[0],
      reader = new FileReader();
  
  reader.onload = function(event) {
    $dropimg.css('background-image', 'url(' + event.target.result + ')');
  }
  
  reader.readAsDataURL(file);
});


$remover.on('click', function() {
  $dropimg.css('background-image', '');
  $droptarget.removeClass('dropped');
  $remover.addClass('disabled');
  $('.image_title input').val('');
});




$('.image_title input').blur(function() {
  if ($(this).val() != '') {
    $droptarget.removeClass('dropped');
  }
});




//second section

var $dropzone2 = $('.image_picker2'),
    $droptarget2 = $('.drop_target2'),
    $dropinput2 = $('#inputFile2'),
    $dropimg2 = $('.image_preview2'),
    $remover2 = $('[data-action="remove_current_image2"]');



$dropzone2.on('dragover', function() {
  $droptarget2.addClass('dropping');
  return false;
});

$dropzone2.on('dragend dragleave', function() {
  $droptarget2.removeClass('dropping');
  return false;
});

$dropzone2.on('drop', function(e) {
  $droptarget2.removeClass('dropping');
  $droptarget2.addClass('dropped');
  $remover2.removeClass('disabled2');
  e.preventDefault();
  
  var file = e.originalEvent.dataTransfer.files[0],
      reader = new FileReader();

  reader.onload = function(event) {
    $dropimg2.css('background-image', 'url(' + event.target.result + ')');
  };
  
  console.log(file);
  reader.readAsDataURL(file);

  return false;
});

$dropinput2.change(function(e) {
  $droptarget2.addClass('dropped');
  $remover2.removeClass('disabled2');
  $('.image_title input').val('');
  
  var file = $dropinput2.get(0).files[0],
      reader = new FileReader();
  
  reader.onload = function(event) {
    $dropimg2.css('background-image', 'url(' + event.target.result + ')');
  }
  
  reader.readAsDataURL(file);
});


$remover2.on('click', function() {
  $dropimg2.css('background-image', '');
  $droptarget2.removeClass('dropped');
  $remover2.addClass('disabled2');
  $('.image_title input').val('');
});


var i = 0;
function move() {
  if (i == 0) {
    i = 1;
    var elem = document.getElementById("myBar");
    var progbar=document.getElementById("myProgress");
    progbar.hidden=false;
    var width = 1;
    var id = setInterval(frame, 30);
    function frame() {
      if (width >= 100) {
        clearInterval(id);
        i = 0;
      } else {
        width++;
        elem.style.width = width + "%";
      }
    }
  }
}

