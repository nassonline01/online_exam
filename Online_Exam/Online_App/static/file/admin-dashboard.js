
document.querySelectorAll('.dropdown').forEach(dropdown => {
    dropdown.addEventListener('click',function() {
        this.classList.toggle('active');
    });
});

document.querySelectorAll('.sub-dropdown').forEach(subDropdown => {
    subDropdown.addEventListener('click', function (e) {
      e.stopPropagation(); 
      this.classList.toggle('active');
    });
});