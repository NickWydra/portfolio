var current_frame, total_frames, path, length, handle;

var init = function() {
  current_frame = 0;
  total_frames = 100;
  path = new Array();
  length = new Array();
  i = 0;
  path[i] = document.getElementById('i'+i);
  l = path[i].getTotalLength();
  length[i] = l;
  path[i].style.strokeDasharray = l + ' ' + l;
  path[i].style.strokeDashoffset = l;
  handle = 0;
}

var draw = function() {
   var progress = current_frame/total_frames;
   if (progress > 1) {
     window.cancelAnimationFrame(handle);
   } else {
     current_frame++;
     for(var j=0; j<path.length;j++){
         path[j].style.strokeDashoffset = Math.floor(length[j] * (1 + progress));
     }
     handle = window.requestAnimationFrame(draw);
   }
};

init();
draw();

window.setTimeout(function() {
  $('#solidN').fadeIn();
  $('#i0').fadeOut();
}, 1500);
