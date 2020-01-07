const async = require('async')
const Axios = require("axios");
const fs = require("fs");
const Path = require("path");
let urls;

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

fs.readFile("./The Complete Node.js Course.json", 'utf8', function(err, data) {
    if (err) throw err;
    urls = JSON.parse(data);
    let idx = 0;
    async.each(urls, function(i) {
        let k = Object.keys(urls)[idx];
        idx++;
        download(i, Path.resolve(__dirname, './vids/', k + '.mp4'))
            .then(data => console.info('finished: ', i))
            .catch(err => console.info(err));
    })
});
