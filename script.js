<script>
    document.addEventListener('DOMContentLoaded', function() {
        const themeSwitch = document.getElementById('theme-switch');

        // Check for saved user preference in localStorage
        const isDarkMode = localStorage.getItem('darkMode') === 'true';

        // Set the initial theme based on user preference
        if (isDarkMode) {
            document.body.classList.add('dark-mode');
            themeSwitch.checked = true; // Set toggle to checked
        }

        // Toggle dark mode on switch change
        themeSwitch.addEventListener('change', function() {
            document.body.classList.toggle('dark-mode');
            // Save preference in localStorage
            localStorage.setItem('darkMode', themeSwitch.checked);
        });
    });
</script>
