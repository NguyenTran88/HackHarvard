document.getElementById('upload-audio').addEventListener('click', function (event) {
    document.getElementById('input').click();
});

document.getElementById('input').addEventListener('change', function (event) {
    if (this.files.length !== 1) {
        alert('Please select only one file');
        return;
    }

    var file = this.files[0];

    // check if file <= 20 MB
    if (file.size > 20971520) {
        alert('File size must be less than 20 MB');
        return;
    }

    console.log(file.type)
    // check if file is audio
    if (!file.type.match('audio.mpeg')) {
        alert('Please select a .mp3 audio file');
        return;
    }

    document.getElementById('response-overall').innerHTML = `
    <h4>Response:</h4>
    <div id="response">Processing... (this may take a few minutes)</div>`;
    var reader = new FileReader();
    reader.onload = function () {
        fetch('/api/upload-audio', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                audio: reader.result
            })
        }).then(response => response.json())
        .then(response => response.text)
        .then(function (response) {
            console.log(response);
            // let id = response.substring(0, response.indexOf('\n'));
            // id = id.substring(4);
            // console.log(id);
            document.getElementById('response').innerHTML = response
            .replace(/\n/g, '<br>')
            .replace(/\033\[91m/g, '<span class="text-danger">')
            .replace(/\033\[92m/g, '<span class="text-success">')
            .replace(/\033\[93m/g, '<span class="text-warning">')
            .replace(/\033\[94m/g, '<span class="text-primary">')
            .replace(/\033\[95m/g, '<span style="color: purple;">')
            .replace(/\033\[96m/g, '<span class="text-info">')
            .replace(/\033\[0m/g, '</span>');
        });
    }

    reader.readAsDataURL(file);
});
