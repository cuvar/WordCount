console.log('main process working');

const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require('path');
const url = require('url');

let win;

function createWindow () {
    win = new BrowserWindow();
    win.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file',
        slashes: true
    }));

    win.on('closed', () => {
        win = null
    });

}

app.on('ready', createWindow);


function go () {

    output = count();
    var s = "";
    for (var entry in output) {
        s = entry + "\n";
    }
    document.getElementById('lbl').innerHTML = s;
}

function count () {
    var frequency = {};
    var text = document.getElementById('ta').value;
    var uneditedWords = text.split("(\\r\\n|\\r|\\n|\\s|['(),;.:]+)");

    //rearrange words for looking nice
    editedWords = [];
    for (word in uneditedWords) {
        word = word.toLowerCase();

        //remove all symbols
        var w = word.replace("[^-/§$%€a-zA-Z0-9]", "");
        if (w.localeCompare("")) {
            editedWords.remove(w);
        } else if (w.localeCompare("m")) {
            editedWords.add("am");
        } else if (w.localeCompare("re")) {
            editedWords.add("are");
        } else {
            editedWords.add(w);
        }

    }

    //put words in hashmap
    for (w in editedWords) {
        //int j = 1;
        var match = false;
        for (var key in frequency) {
        if(w.localeCompare(key)) {
                match = true;
            }
        }
        if(match) {
            frequency[w] = frequency[w] + 1;
        }
        else {
            frequency[w] = 1;
        }

    }

    //put HashMap in array for JList
    var list = [];
    var i = 0;
    for (var key in frequency) {
        list[i] = key + ": " + frequency[key];
        i++;
    }
    //sort list by quantity
    list = sortByQuantity(list);
    return list;

}



function sortByQuantity(arr) {
    for (var i = arr.length - 1; i >=1; i--) {
        for (var j = 0; j < arr.length - 1; j++){
            var s1 = arr[j].substring(arr[j].lastIndexOf(":") + 2);
            var s2 = arr[j+1].substring(arr[j+1].lastIndexOf(":") + 2);
            var f1 = parseInt(s1);
            var f2 = parseInt(s2);
            if(f1 < f2){
                var h = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = h;
            }
        }
    }
    return arr;
}