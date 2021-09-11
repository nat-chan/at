// ==UserScript==
// @name         AtCoder Beep
// @namespace    https://github.com/nat-chan
// @version      0.1
// @description  AtCoder Beep
// @author       nat-chan
// @match        https://atcoder.jp/contests/*/submissions/*
// @grant        none
// ==/UserScript==

const short = 100;
const long = 1000;
const wa = 100;
const ac = 800;

function square(hz, ms){
    let audioCtx = new AudioContext();
    let osc = audioCtx.createOscillator();
    osc.frequency.value = hz;
    osc.type = "square";
    osc.connect(audioCtx.destination);
    osc.start(audioCtx.currentTime);
    osc.stop(audioCtx.currentTime + ms *0.001);
}

function parse(text){
//    let S = "CE,MLE,TLE,RE,OLE,IE,WA,AC,WJ,WR".split(',');
    let S = "CE,MLE,TLE,RE,OLE,IE,WA".split(',');
    let status = "AC";
    for(const s of S){
        if(text.includes(s)){
            text = text.replace(s, "");
            status = s;
            break;
        }
    }
    return status;
}

function main(){
    let target = document.getElementById("judge-status");
    if(document.referrer == document.URL){
        if(target.innerText == "AC"){
            square(ac, long);
        }else{
            square(wa, long);
        }
    }else if(target.innerText == "WJ"){
        let observer = new MutationObserver(records => {
            console.log(target.innerText);
            if(parse(target.innerText) == "AC"){
                square(ac, short);
            }else{
                square(wa, short);
            }
        });
        observer.observe(target, {
            childList: true
        });
    }
}
main();