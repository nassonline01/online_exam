// Add click event listener to all dropdown items
document.querySelectorAll('.dropdown').forEach(item => {
    item.addEventListener('click', (event) => {
        event.stopPropagation(); // Prevent event bubbling to the document
        
        // Toggle the 'active' class on the clicked dropdown
        const isActive = item.classList.contains('active');
        document.querySelectorAll('.dropdown').forEach(dropdown => dropdown.classList.remove('active'));

        if (!isActive) {
            item.classList.add('active');
        }
    });
});

// Close all dropdowns when clicking outside
document.addEventListener('click', () => {
    document.querySelectorAll('.dropdown').forEach(dropdown => dropdown.classList.remove('active'));
});
