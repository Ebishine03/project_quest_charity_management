

  const n=document.querySelector('.navbar');
  window.addEventListener('scroll',() =>{
      if(window.scrollY >= 500){
          n.classList.add('navbar-scrolled')
      }
      else if (window.scrollY < 500){
          n.classList.remove('navbar-scrolled')
      }
   })
 

  