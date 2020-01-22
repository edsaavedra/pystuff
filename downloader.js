const async = require('async')
const Axios = require("axios");
const fs = require("fs");
const Path = require("path");
let urls;
let paths = [];

fs.readdirSync('./').forEach(file => {
    if (file.match(/^\d.+(\.json)/g)){
        paths.push(file);
        fs.mkdirSync(file.replace('.json', ''));
    };
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

for (dir in paths) {
    const cu = "./" + paths[dir];
    console.info('%c 💩 ', 'background: #ffbf27', cu);
/*     fs.readFile(cu, 'utf8', function(err, data) {
        if (err) throw err;
        urls = JSON.parse(data);
        let idx = 0;

        async.mapLimit(urls, 5, async function(i) {
            let k = Object.keys(urls)[idx];
            idx++;
            let path = k + '.mp4';
            return download(i, Path.resolve(__dirname, cu.replace('.json', ''), path))
                .then(data => console.info('finished: ', k))
                .catch(err => console.info(err, '⚡'));
        }, (err, results) => {
            if (err) throw err
        })
    }); */
}
