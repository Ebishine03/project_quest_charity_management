

  const n=document.querySelector('.navbar');
  window.addEventListener('scroll',() =>{
      if(window.scrollY >= 500){
          n.classList.add('navbar-scrolled')
      }
      else if (window.scrollY < 500){
          n.classList.remove('navbar-scrolled')
      }
   })
 
function toggleSidebar(ref){
    document.getElementById("sidebar").classList.toggle('active');
    // var togglerButton = document.querySelector('.toggle-btn');
    // togglerButton.classList.add('hidden');
  }


