function togglePassword() {
    const pwd = document.getElementById('password');
    const toggle = document.querySelector('.toggle-password');
    if (pwd.type === 'password') {
      pwd.type = 'text';
      toggle.textContent = 'Hide';
    } else {
      pwd.type = 'password';
      toggle.textContent = 'Show';
    }
  }



// Simple placeholder script for clickable links
document.querySelectorAll('.calendar-links span').forEach(item => {
    item.addEventListener('click', () => {
        alert(item.textContent.trim());
    });
});

