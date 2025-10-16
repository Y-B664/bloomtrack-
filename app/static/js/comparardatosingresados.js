 const plantaSelect = document.getElementById('planta');
    const sensoresDiv = document.getElementById('inputs-sensores');

    plantaSelect.addEventListener('change', function() {
        if (this.value) {
            sensoresDiv.style.display = 'block';
        } else {
            sensoresDiv.style.display = 'none';
        }
    });