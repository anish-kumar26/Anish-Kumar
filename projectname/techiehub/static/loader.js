// loader.js

document.addEventListener('DOMContentLoaded', function () {
    var loadingScreen = document.getElementById('loadingScreen');
    var content = document.getElementById('content');

    // Show loading screen
    loadingScreen.style.display = 'flex';

    // Simulate loading (replace this with actual AJAX calls)
    setTimeout(function () {
        // Hide loading screen after a delay (simulating content loading)
        loadingScreen.style.display = 'none';
        // Show content
        content.style.display = 'block';
    }, 2000); // Replace 2000 with the actual time your content takes to load
});
