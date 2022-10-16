const express = require('express');
const app = express();
const server = require('http').createServer(app);
const port = process.env.PORT || 3000;

const fs = require('fs');

// app.use(express.json());

app.use(express.json({ limit: 20971520 }));

app.get('/', (req, res) => {
    res.sendFile('index.html', { root: __dirname });
});

app.post('/api/upload-audio', processAudio);

function processAudio(req, res) {
    console.log('Processing audio...');
    fs.writeFileSync(__dirname + '/audio.mp3', req.body.audio, 'base64');
    var spawn = require('child_process').spawn;
    var process = spawn('python', ['./main.py', 'website/audio.mp3', '--local']);

    var output = '';
    process.stdout.on('data', function (data) {
        console.log(data.toString());
        output += data.toString();

        if (output.includes('Done.')) {
            res.send(JSON.stringify({ text: output }));
            fs.unlinkSync(__dirname + '/audio.mp3');
        }
    });
}

app.use((req, res) => {
    res.sendFile(req.url, { root: __dirname });
});

server.listen(port, () => {
    console.log(`listening at port=${port}`);
});
