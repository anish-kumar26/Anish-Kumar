

document.addEventListener('DOMContentLoaded', function () {
    var loadingScreen = document.getElementById('loadingScreen');
    var content = document.getElementById('content');

    loadingScreen.style.display = 'flex';
    setTimeout(function () {
        loadingScreen.style.display = 'none';
        content.style.display = 'block';
    }, 1000); 
});
