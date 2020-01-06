const fs = require("fs");
const Path = require("path");
const Axios = require("axios");
let urls;

fs.readFile("./test.json", 'utf8', function(err, data) {
    if (err) throw err;
    urls = JSON.parse(data);
    Object.keys(urls).forEach(function(i) {
        download(urls[i], Path.resolve(__dirname, './', i + '.mp4'))
            .then(data => console.info('finished: ', i))
            .catch(err => console.info(err))
    })
});

async function download(url, path) {
        const response = await Axios({
            method: 'GET',
            url: url,
            responseType: 'stream'
        });

        response.data.pipe(fs.createWriteStream(path));
        return new Promise((resolve, reject) => {
            response.data.on('end', () => {resolve()});
            response.data.on('error', err => {reject(err)})
        });
}
